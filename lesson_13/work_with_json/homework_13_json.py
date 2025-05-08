import os
import json
import logging

print(os.getcwd())

logging.basicConfig(
    filename='invalid_json.log',
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def is_valid_json(file_path):
    try:
        with open(file_path, 'r') as f:
            json.load(f)
        return True
    except Exception as e:
        logging.error(f"Invalid JSON in file: {file_path} | Error: {e}")
        return False

def validate_json_files_in_directory(directory_path):
    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)
        if os.path.isfile(file_path) and filename.endswith('.json'):
            is_valid_json(file_path)

validate_json_files_in_directory(r'C:\Users\kiril\PycharmProjects\hillel_aqa_python_HW\lesson_13\work_with_json')
