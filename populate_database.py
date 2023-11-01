import os
import django
import csv  # If you're using CSV files
import json  # If you're using JSON files

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MyRetailProtocolProject.settings')
django.setup()

from protocol_app.models import Protocol


def populate_from_csv(file_path):
    with open(file_path, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            instance = Protocol(**row)  # Replace Protocol with your actual model
            instance.save()


def populate_from_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:  # Added encoding
        data = json.load(f)
        for record in data:
            # Map JSON keys to Django model fields
            mapped_record = {
                'name': record.get('Protocol', 'Default Name'),  # Default to 'Default Name' if not found
                'title': record.get('Protocol', ''),
                'description': record.get('Scop', ''),
                # Add other fields if needed
            }
            
            # Handle nested 'Pasi' field (you can store it as a JSON string or handle it differently)
            pasi = record.get('Pasi', {})
            mapped_record['description'] += "\n\nPasi:\n" + json.dumps(pasi, ensure_ascii=False)
            
            print(f"Record to be inserted: {mapped_record}")  # Debugging line
            
            instance = Protocol(**mapped_record)
            instance.save()

if __name__ == '__main__':
    # For CSV
    # populate_from_csv("C:\\Users\\paulm\\Desktop\\Protocol Raft Produse Neconforme.csv")
    
    # For JSON (comment out the above line if using JSON)
    populate_from_json(r'C:\Users\\paulm\\Desktop\\Github\\MyRetailProtocolProject\\protocols\\worker\\Protocol_Raft_Produse_Neconforme.json')            
    