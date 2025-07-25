import argparse
import csv
import os
import json
import datetime
import tabulate
from colorama import Fore, Style

# GLobal variables
months = ["January","February","March","April","May","June","July","August","September","October","November","December"]


# Get inputs function
def get_user_inputs():
    parser = argparse.ArgumentParser(description='Expense Tracker')
    parser.add_argument("operation", help="Operation to perform", choices=['add', 'list', 'update','delete','summary'])
    parser.add_argument("--description", help="Description of the expense", type=str)
    parser.add_argument("--amount", help="Amount of the expense", type=float)
    parser.add_argument("--id",help="ID of the expense", type=int)
    parser.add_argument("--month", help="Month of the expense", type=int)
    parser.add_argument("--category", type=str, help="Category of the expense")
    parser.add_argument("--budget", type=float, help="Budget for the month")
    return parser.parse_args()

# Utility functions
def read_expenses():
    if os.path.exists("expenses.json"):
        with open("expenses.json", "r") as file:
            return json.load(file)
    return []

def write_expenses(expenses):
    with open("expenses.json", "w") as file:
        json.dump(expenses, file, indent=4)

def find_expense(expenses, expense_id):
    for expense in expenses:
        if expense["ID"] == expense_id:
            return expense
    return None

# Operations

def add_expense(description, amount, category):
    expenses = read_expenses()
    expense_id = len(expenses) + 1
    if amount < 0:
        raise Exception(f"Amount cannot be negative -> {amount} !!!!")
    if description is None or amount is None or category is None:
        raise Exception("Description, Amount and Category are required")
    expense = {
        "ID": expense_id,
        "category": category,
        "Description": description,
        "Amount": amount,
        "Created_at": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    expenses.append(expense)
    write_expenses(expenses)
    return f"Expense added successfully (ID {expense_id})"

def update_expense(expense_id, new_description, new_amount):
    expenses = read_expenses()
    expense = find_expense(expenses, expense_id)
    if new_amount < 0:
        raise Exception(f"Amount cannot be negative -> {new_amount} !!!!")
    if new_description is None or new_amount is None:
        raise Exception("Description and Amount are required to update the expense")
    if expense is not None:
        if new_description is not None and new_amount is not None:
            expense["Description"] = new_description
            expense["Amount"] = new_amount
            expense["Updated_at"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            write_expenses(expenses)
            return f"Expense {expense_id} updated successfully"
        else:
            raise Exception("Description and Amount are required")
    else:
        raise Exception(f"Expense {expense_id} not found")

def list_expenses(category):
    expenses = read_expenses()
    if len(expenses) == 0:
        return "No expenses found"
    result_list = []
    if category is not None:
        for expense in expenses:
            if expense["category"] == category:
                result_list.append(expense)
        if len(result_list) == 0:
            return "No expenses found"
        print(tabulate.tabulate(result_list, headers="keys", tablefmt="grid"))
    else:
        print(tabulate.tabulate(expenses, headers="keys", tablefmt="grid"))       
    return expenses 

def delete_expense(expense_id):
    expenses = read_expenses()
    expense = find_expense(expenses, expense_id)
    if expense is not None:
        expenses.remove(expense)
        write_expenses(expenses)
        return f"Expense {expense_id} deleted successfully"
    else:
        raise Exception(f"Expense {expense_id} not found")
        
        
def summary_expenses(month, budget):
    expenses = read_expenses()
    total = 0
    if expenses is None:
        return "No expenses found"
    if month is None:
        for expense in expenses:
            total += expense["Amount"]
        return f"Total Expenses: {total}"
    else:
        for expense in expenses:
            current_month  = expense["Created_at"].split("-")[1]
            if current_month.startswith("0"):
                current_month = current_month[1]
                if int(current_month) == month:
                    total += expense["Amount"]
            else:
                if int(current_month) == month:
                    total += expense["Amount"]    
        if total > budget:
            return Fore.YELLOW + f"⚠️ Warning: You have exceeded the budget of {months[month-1]}. Your total is {total}. Your budget is {budget}" + Style.RESET_ALL

        return f"Total Expenses for {months[month-1]}: {total}"
    
    
def export_expenses_to_csv():
    expenses = read_expenses()
    if len(expenses) == 0:
        return "No expenses found"
    with open("expenses.csv", "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=expenses[0].keys())
        writer.writeheader()
        writer.writerows(expenses)
    return "Expenses exported to expenses.csv"

# Main Function

def main():
    args = get_user_inputs()
    budget = args.budget
    if args.operation == "add":
        print(add_expense(args.description, args.amount, args.category))
    elif args.operation == "update":
        print(update_expense(args.id, args.description, args.amount))
    elif args.operation == "list":
        list_expenses(args.category)
    elif args.operation == "delete":
        print(delete_expense(args.id))
    elif args.operation == "summary":
        print(summary_expenses(args.month, budget))

if __name__ == "__main__":
    main()
    input("Press Enter to continue...")
    user_res = input("Export to CSV? yes/no")
    if user_res.strip().lower() == "yes":
        print(export_expenses_to_csv())
    else:
        print("Goodbye")