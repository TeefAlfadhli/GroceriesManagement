import argparse
import json
import os
from datetime import datetime, timedelta

# Files to store the list and receipts
FILE_NAME = "groceries.json"
RECEIPT_FILE = "receipts.json"
USERS_FILE = "users.json"

# Load the list from the JSON file (or initialize it if the file doesn't exist)
def load_json(file_name):
    if os.path.exists(file_name):
        with open(file_name, "r") as file:
            return json.load(file)
    return []

# Save the list to the JSON file
def save_json(data, file_name):
    with open(file_name, "w") as file:
        json.dump(data, file, indent=4)

# Simple login function
def login():
    users = load_json(USERS_FILE)
    username = input("Enter username: ")
    password = input("Enter password: ")

    for user in users:
        if user["username"] == username and user["password"] == password:
            print(f"Login successful as {username}!")
            return user["role"]
    print("Invalid username or password!")
    return None

# Save an action to the receipts log
def log_receipt(action, item):
    receipts = load_json(RECEIPT_FILE)
    receipts.append({
        "action": action,
        "item": item,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })
    save_json(receipts, RECEIPT_FILE)

# Define functions
def add(item, quantity, category, expiry_date):
    inventory = load_json(FILE_NAME)
    existing_item = next((i for i in inventory if i["name"] == item), None)

    if existing_item:
        existing_item["quantity"] += quantity
        existing_item["updated_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    else:
        new_item = {
            "name": item,
            "quantity": quantity,
            "category": category,
            "expiry_date": expiry_date,
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "updated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        inventory.append(new_item)

    save_json(inventory, FILE_NAME)
    log_receipt("add", item)
    print(f"Added/Updated {item}. Current list:")
    for i in inventory:
        print(f"- {i['name']} (Quantity: {i['quantity']}, Category: {i['category']}, Expiry: {i['expiry_date']})")

def delete(item):
    inventory = load_json(FILE_NAME)
    inventory = [i for i in inventory if i["name"] != item]
    save_json(inventory, FILE_NAME)
    log_receipt("delete", item)
    print(f"Deleted {item}. Current list:")
    for i in inventory:
        print(f"- {i['name']} (Quantity: {i['quantity']})")

def view():
    inventory = load_json(FILE_NAME)
    if inventory:
        print("Current list:")
        for item in inventory:
            print(f"- {item['name']} (Quantity: {item['quantity']}, Category: {item['category']}, Expiry: {item['expiry_date']})")
    else:
        print("The list is empty.")

def view_receipts():
    receipts = load_json(RECEIPT_FILE)
    if receipts:
        print("Receipt Log:")
        for receipt in receipts:
            print(f"{receipt['timestamp']}: {receipt['action']} - {receipt['item']}")
    else:
        print("No receipts found.")

def check_low_stock(threshold=5):
    inventory = load_json(FILE_NAME)
    low_stock_items = [item for item in inventory if item["quantity"] <= threshold]
    if low_stock_items:
        print("Low stock notification:")
        for item in low_stock_items:
            print(f"- {item['name']} (Quantity: {item['quantity']})")
    else:
        print("No items with low stock.")

def search_items(query):
    inventory = load_json(FILE_NAME)
    matching_items = [item for item in inventory if query.lower() in item["name"].lower()]
    if matching_items:
        print("Search results:")
        for item in matching_items:
            print(f"- {item['name']} (Quantity: {item['quantity']}, Category: {item['category']}, Expiry: {item['expiry_date']})")
    else:
        print("No matching items found.")

def check_expired_items():
    inventory = load_json(FILE_NAME)
    today = datetime.now().strftime("%Y-%m-%d")
    expired_items = [item for item in inventory if item["expiry_date"] < today]
    if expired_items:
        print("Expired items:")
        for item in expired_items:
            print(f"- {item['name']} (Expired on {item['expiry_date']})")
    else:
        print("No expired items found.")

def generate_report():
    inventory = load_json(FILE_NAME)
    total_items = len(inventory)
    total_quantity = sum(item["quantity"] for item in inventory)
    print("Inventory Report:")
    print(f"Total items: {total_items}")
    print(f"Total quantity of all items: {total_quantity}")
    print("Detailed items:")
    for item in inventory:
        print(f"- {item['name']} (Quantity: {item['quantity']}, Expiry: {item['expiry_date']})")

# User authentication setup
def setup_users():
    if not os.path.exists(USERS_FILE):
        users = [
            {"username": "manager1", "password": "managerpass", "role": "manager"},
            {"username": "worker1", "password": "workerpass", "role": "worker"}
        ]
        save_json(users, USERS_FILE)

# Create the parser
parser = argparse.ArgumentParser(description="Groceries Management System with Enhanced Features")
subparsers = parser.add_subparsers(dest="command", help="Commands")

# Add subcommands
add_parser = subparsers.add_parser("add", help="Add an item to the inventory")
add_parser.add_argument("item", type=str, help="Name of the item")
add_parser.add_argument("quantity", type=int, help="Quantity of the item")
add_parser.add_argument("category", type=str, help="Category of the item")
add_parser.add_argument("expiry_date", type=str, help="Expiry date (YYYY-MM-DD)")

delete_parser = subparsers.add_parser("delete", help="Delete an item from the inventory")
delete_parser.add_argument("item", type=str, help="Name of the item to delete")

view_parser = subparsers.add_parser("view", help="View all items in the inventory")

receipts_parser = subparsers.add_parser("view_receipts", help="View receipts of added/deleted items")

low_stock_parser = subparsers.add_parser("check_low_stock", help="Check for low stock items")
low_stock_parser.add_argument("--threshold", type=int, default=5, help="Threshold for low stock")

search_parser = subparsers.add_parser("search", help="Search for items by name")
search_parser.add_argument("query", type=str, help="Search query")

expired_parser = subparsers.add_parser("check_expired", help="Check for expired items")

report_parser = subparsers.add_parser("report", help="Generate a report of the inventory")

# Parse arguments
args = parser.parse_args()

# User login and role verification
setup_users()  # Ensure users are set up
role = login()
if role is None:
    exit("Exiting due to failed login.")

# Restrict command access based on role
if args.command == "add" and role in ["manager", "worker"]:
    add(args.item, args.quantity, args.category, args.expiry_date)
elif args.command == "delete" and role in ["manager", "worker"]:
    delete(args.item)
elif args.command == "view" and role == "manager":
    view()
elif args.command == "view_receipts" and role == "manager":
    view_receipts()
elif args.command == "check_low_stock" and role == "manager":
    check_low_stock(args.threshold)
elif args.command == "search" and role == "manager":
    search_items(args.query)
elif args.command == "check_expired" and role == "manager":
    check_expired_items()
elif args.command == "report" and role == "manager":
    generate_report()
else:
    parser.print_help()
