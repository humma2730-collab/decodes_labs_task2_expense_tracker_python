"""
***************************************
Expense Tracker System
Developed By: Huma Fatima
***************************************
"""
from expense_manager import (
    add_expense,
    view_expenses,
    search_expense,
    update_expense,
    delete_expense,
    show_statistics
)
# Display the main menu
def display_menu():

    print("\n" + "*" * 50)
    print(" EXPENSE TRACKER SYSTEM")
    print("*" * 50)
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Search Expense")
    print("4. Update Expense")
    print("5. Delete Expense")
    print("6. Show Statistics")
    print("7. Exit")
    print("*" * 50)
def main():
    #Main Program
    while True:
        display_menu()
        choice = input("Enter your choice (1-7): ").strip()
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            search_expense()
        elif choice == "4":
            update_expense()
        elif choice == "5":
            delete_expense()
        elif choice == "6":
            show_statistics()
        elif choice == "7":
            print("\n*****************************************")
            print(" Thank you for using Expense Tracker!")
            print(" Goodbye!")
            print("*******************************************")
            break
        else:
            print("\nInvalid choice! Please enter a number between 1 and 7.")

if __name__ == "__main__":
    main()