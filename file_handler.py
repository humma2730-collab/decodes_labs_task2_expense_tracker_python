"""
*****************************************
Expense Tracker System
File Handler
Developed By: Huma Fatima
*****************************************
"""
import json
import os
FILE_NAME = "expenses.json"

# Load Expenses

def load_expenses():
    
    if not os.path.exists(FILE_NAME):
        return []
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, FileNotFoundError):
        return []

#  Save Expenses

def save_expenses(expenses):
    
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(expenses, file, indent=4)
