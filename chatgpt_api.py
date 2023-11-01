from protocol_app.business_logic import fetch_protocols_by_role
from django.http import HttpRequest, JsonResponse
from rest_framework.request import Request
from decouple import Config
from typing import cast
import os
import logging
import openai
from protocol_app.models import Protocol
from django.forms.models import model_to_dict
import re
import json
import logging
from threading import Lock
import sqlite3

# Initialize logging
logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger(__name__)

# Initialize a lock for the conversation_history
conversation_history_lock = Lock()  # Added for concurrency


# Load API key from environment file
config = Config("C:/Users/paulm/Desktop/Github/MyRetailProtocolProject/.env")
api_key = config("GPT3_API_KEY")
openai.api_key = api_key

# Initialize an empty list to hold the conversation history
conversation_history = []

from protocol_app.models import Protocol  # Import your model

def fetch_protocol_from_db(key_terms: str) -> str:
    try:
        protocol_data = Protocol.objects.filter(title__icontains=key_terms).first()
        if protocol_data:
            protocol_data_json = json.dumps(model_to_dict(protocol_data), default=str)
            return protocol_data_json
        else:
            return "No data found"
    except Exception as e:
        return f"An error occurred: {e}"
    
def chat_with_gpt3_function(request: Request):
    logger.debug("This is a debug message in my custom function")
    global conversation_history  # Use the global conversation history
    
    if request.method == 'POST':
        payload = cast(dict, request.data)
        user_question: str = payload.get("user_input", "")
        
        try:
            # Step 1: Interpret User's Question with GPT-3
            interpretation = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": f"Interpret this question: {user_question}"}
                ]
            )
            interpreted_content: str = interpretation['choices'][0]['message']['content']
            key_terms = interpreted_content.split()
            logging.debug("Interpreted Content: %s", interpreted_content)  # Added debug line
            logging.debug("Key Terms: %s", key_terms)  # Added debug line
        except Exception as e:
            return JsonResponse({"error": f"An error occurred while interpreting the question: {e}"})
        
        key_terms = [term for term in interpreted_content.split() if term.lower() in ['protocol']]
        key_terms_str = ' '.join(key_terms)
        
        # Step 2: Dynamic Query Construction & Execution
        protocol_answer = fetch_protocol_from_db(key_terms_str)

        # Parse the string into a dictionary
        protocol_dict = json.loads(protocol_answer)

        # Extract the file path
        file_path = protocol_dict['file']

        # Assuming protocol_answer is the path to the file
        with open(file_path, 'r') as file:
            file_content = file.read()
        
        with conversation_history_lock:  # Added for concurrency
            conversation_history.append({"role": "user", "content": f"User Question: {user_question}"})
        
        # Step 3: Prepare messages for GPT-3 API and generate response
        messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"User Question: {user_question}"},
            {"role": "assistant", "content": f"Database Information: {protocol_answer}"},
            {"role": "assistant", "content": f"File Content: {file_content}"},
            {"role": "user", "content": "Please interpret the content of the file in the language of the file."}        
        ] + conversation_history
        
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=messages
            )
            
            message_content: str = response['choices'][0]['message']['content']
            logging.debug("Message Content: %s", message_content)  # Added debug line
            
            conversation_history.append({"role": "assistant", "content": message_content})
            
            return JsonResponse({"response": message_content.strip(), "conversation_history": conversation_history})
            
        except Exception as e:
            return JsonResponse({"error": f"An error occurred: {e}"})
    else:
        return JsonResponse({"error": "Only POST method is allowed."})

    

def generate_sql_query(interpreted_content: str) -> str:
    try:
        sql_generation = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": f"Generate an SQL query for this: {interpreted_content}"}
            ]
        )
        sql_query: str = sql_generation['choices'][0]['message']['content']
        return sql_query.strip()  # Remove any extra spaces or newlines
    except Exception as e:
        return f"An error occurred while generating the SQL query: {e}"
    


def execute_sql_query(sql_query: str):
    try:
        conn = sqlite3.connect('your_database_name.db')
        cursor = conn.cursor()
        cursor.execute(sql_query)
        results = cursor.fetchall()
        return results
    except Exception as e:
        return f"An error occurred while executing the SQL query: {e}"