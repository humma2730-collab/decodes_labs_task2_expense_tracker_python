"""
****************************************
Expense Tracker System
Expense Manager
Developed By: Huma Fatima
****************************************
"""
from datetime import datetime
from file_handler import load_expenses, save_expenses

# Add Expense
def add_expense():
    
    expenses = load_expenses()

    print("\n********* ADD EXPENSE *********")

    title = input("Enter Expense Title: ").strip()
    if not title:
        print("Title cannot be empty.")
        return
    try:
        amount = float(input("Enter Expense Amount (Rs.): "))
        if amount <= 0:
            print("Amount must be greater than zero.")
            return
    except ValueError:
        print("Invalid amount. Please enter a valid number.")
        return
    expense = {
        "id": len(expenses) + 1,
        "title": title,
        "amount": amount,
        "date": datetime.now().strftime("%d-%m-%Y %I:%M %p")
    }
    expenses.append(expense)
    save_expenses(expenses)
    print("\nExpense added successfully!")

# View Expenses
def view_expenses():
    expenses = load_expenses()
    print("\n******** ALL EXPENSES ********")
    if not expenses:
        print("No expenses found.")
        return
    total = 0
    for expense in expenses:
        print("-" * 45)
        print(f"ID     : {expense['id']}")
        print(f"Title  : {expense['title']}")
        print(f"Amount : Rs. {expense['amount']}")
        print(f"Date   : {expense['date']}")
        total += expense["amount"]
    print("-" * 45)
    print(f"Total Expenses : Rs. {total}")
# Search Expense
def search_expense():

    expenses = load_expenses()
    if not expenses:
        print("\nNo expenses found.")
        return
    keyword = input("\nEnter Expense Title to Search: ").strip().lower()
    found = False
    print("\n********* SEARCH RESULT **********")
    for expense in expenses:
        if keyword in expense["title"].lower():
            print("-" * 45)
            print(f"ID     : {expense['id']}")
            print(f"Title  : {expense['title']}")
            print(f"Amount : Rs. {expense['amount']}")
            print(f"Date   : {expense['date']}")
            found = True
    if not found:
        print("No matching expense found.")

# Update Expense

def update_expense():
    
    expenses = load_expenses()
    if not expenses:
        print("\nNo expenses available.")
        return
    try:
        expense_id = int(input("\nEnter Expense ID to Update: "))
    except ValueError:
        print("Invalid ID.")
        return
    for expense in expenses:
        if expense["id"] == expense_id:
            print(f"\nCurrent Title  : {expense['title']}")
            print(f"Current Amount : Rs. {expense['amount']}")
            new_title = input("Enter New Title: ").strip()
            if new_title:
                expense["title"] = new_title
            try:
                new_amount = float(input("Enter New Amount (Rs.): "))
                if new_amount <= 0:
                    print("Amount must be greater than zero.")
                    return
                expense["amount"] = new_amount
            except ValueError:
                print("Invalid amount.")
                return
            expense["date"] = datetime.now().strftime("%d-%m-%Y %I:%M %p")
            save_expenses(expenses)
            print("\nExpense updated successfully!")
            return
    print("Expense ID not found.")

# Delete Expense

def delete_expense():
    
    expenses = load_expenses()

    if not expenses:
        print("\nNo expenses available.")
        return
    try:
        expense_id = int(input("\nEnter Expense ID to Delete: "))
    except ValueError:
        print("Invalid ID.")
        return
    for expense in expenses:
        if expense["id"] == expense_id:
            confirm = input(
                f"Are you sure you want to delete '{expense['title']}'? (y/n): "
            ).lower()
            if confirm == "y":
                expenses.remove(expense)
                # Reassign IDs
                for index, item in enumerate(expenses, start=1):
                    item["id"] = index
                save_expenses(expenses)

                print("\nExpense deleted successfully!")
            else:
                print("\nDeletion cancelled.")

            return

    print("Expense ID not found.")

# Statistics

def show_statistics():
    
    expenses = load_expenses()

    if not expenses:
        print("\nNo expense data available.")
        return
    amounts = [expense["amount"] for expense in expenses]

    print("\n********* EXPENSE STATISTICS **********")
    print(f"Total Records   : {len(expenses)}")
    print(f"Total Expense   : Rs. {sum(amounts):.2f}")
    print(f"Highest Expense : Rs. {max(amounts):.2f}")
    print(f"Lowest Expense  : Rs. {min(amounts):.2f}")
    print(f"Average Expense : Rs. {sum(amounts) / len(amounts):.2f}")
    print("*" * 40)