from protocol_app.business_logic import fetch_protocols_by_role
from django.http import HttpRequest, JsonResponse
from rest_framework.request import Request
from decouple import Config
from typing import cast
import os
import logging
import openai

# Initialize logging
logging.basicConfig(level=logging.DEBUG)

# Load API key from environment file
config = Config("C:/Users/paulm/Desktop/Github/MyRetailProtocolProject/.env")
api_key = config("GPT3_API_KEY")
openai.api_key = api_key

def read_protocol_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def fetch_protocols_from_files(role):
    directory = r'C:\Users\paulm\Desktop\Github\MyRetailProtocolProject\protocols\{}'.format(role)
    formatted_protocols = ""
    
    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            file_path = os.path.join(directory, filename)
            protocol_content = read_protocol_file(file_path)
            formatted_protocols += f"{filename}:\n{protocol_content}\n\n"
            
    return formatted_protocols.strip()

def chat_with_gpt3_function(request: Request):
    if request.method == 'POST':
        logging.debug("Received POST request.")

        payload = cast(dict, request.data)
        prompt: str = payload.get("user_input", "")
        user_role: str = payload.get("user_role", "worker")
        protocols: str = fetch_protocols_from_files(user_role)
        prompt = f"Protocols:\n{protocols}\n\nUser Question: {prompt}"

        logging.debug(f"Received user_input: {prompt}, user_role: {user_role}")
        
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
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
        return JsonResponse({"error": "Only POST method is allowed."})
