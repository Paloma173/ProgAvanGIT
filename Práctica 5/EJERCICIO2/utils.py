# utils.py
import uuid
from typing import List, Dict

def leer_int(prompt: str) -> int:
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Error: Please enter a valid integer.")

def leer_float(prompt: str) -> float:
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Error: Please enter a valid float.")

def crear_menu(options: List[str]) -> int:
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    return leer_int("Please choose an option: ")

def generate_unique_id() -> str:
    return str(uuid.uuid4())[:8]

