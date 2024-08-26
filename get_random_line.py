import os
import random

def get_random_line(file_path, encoding='utf-8'):
    try:
        with open(file_path, 'r', encoding=encoding) as file:
            lines = file.readlines()
            valid_lines = [line.rstrip() for line in lines if line and line != '.']
            return random.choice(valid_lines) if valid_lines else None
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
