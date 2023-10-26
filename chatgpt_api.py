from protocol_app.business_logic import fetch_protocols_by_role
from django.http import HttpRequest, JsonResponse
from rest_framework.request import Request
from decouple import Config
from typing import cast
import os
import logging
import openai
from protocol_app.models import Protocol
from pymongo import MongoClient
import re

# Initialize logging
logging.basicConfig(level=logging.DEBUG)

# Load API key from environment file
config = Config("C:/Users/paulm/Desktop/Github/MyRetailProtocolProject/.env")
api_key = config("GPT3_API_KEY")
openai.api_key = api_key

def read_protocol_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

#def fetch_protocols_from_db(role):
    protocols = Protocol.objects.filter(access_level=role)
    formatted_protocols = ""
    
    for protocol in protocols:
        formatted_protocols += f"{protocol.title}:\n{protocol.description}\n\n"
        
    return formatted_protocols.strip()

def fetch_protocol_from_db(question: str):
    # Connect to MongoDB
    client = MongoClient("mongodb+srv://paulmotorca:Zizou2003@cognisteer.eykykjc.mongodb.net/")
    db = client['CogniSteer']
    collection = db['protocols']
    
    # Prepare the question for regex search (escape special characters)
    question = re.escape(question)
    
    # Query the database based on the user's question
    protocol_data = collection.find_one({"titlul": {"$regex": question, "$options": 'i'}})
    
    if protocol_data:
        # Extract relevant information from the protocol_data dictionary
        responsibilities = protocol_data.get('responsabilitati si sarcini', {}).get('sarcini si atributii ale postului de munca', [])
        return "\n".join(responsibilities)
    else:
        return 'No matching protocol found in the database.'

# Test the function
print(fetch_protocol_from_db("manager adjunct"))

def chat_with_gpt3_function(request: Request):
    if request.method == 'POST':
        logging.debug("Received POST request.")

        payload = cast(dict, request.data)
        user_question: str = payload.get("user_input", "")
        
        # Fetch the relevant protocol information based on the user's question
        protocol_answer = fetch_protocol_from_db(user_question)
        
        if protocol_answer:
            # Use the fetched protocol as part of the prompt for ChatGPT
            prompt = f"Protocol Information: {protocol_answer}\n\nUser Question: {user_question}"
            
            try:
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "You are a helpful assistant knowledgeable about Lelia's protocols."},
                        {"role": "user", "content": prompt}
                    ]
                )
                assert isinstance(response, dict)
                message_content: str = response['choices'][0]['message']['content']
                return JsonResponse({"response": message_content.strip()})
                
            except Exception as e:
                logging.error(f"An error occurred while communicating with the GPT-3 API: {e}")
                return JsonResponse({"error": f"An error occurred while communicating with the GPT-3 API: {e}"})
        else:
            return JsonResponse({"error": "No matching protocol found in the database"})
    else:
        return JsonResponse({"error": "Only POST method is allowed."})