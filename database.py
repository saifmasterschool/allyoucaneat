import json
import os
from datetime import datetime
import uuid_utils as uuid

# Utility functions
def save_json(data, file_path):
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)


def load_json(file_path):
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


def now():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


# User functions
def user_functions(file_path, phone_number, action, key=None, value=None):
    users = load_json(file_path)

    if action == 'create' and phone_number not in users:
        users[phone_number] = {"id": str(uuid.uuid4()), "created_at": now(), "updated_at": now()}

    elif action == 'update' and phone_number in users:
        users[phone_number][key] = value
        users[phone_number]['updated_at'] = now()

    elif action == 'delete' and phone_number in users:
        users.pop(phone_number)

    else:
        return f"User {phone_number} not found or action invalid."

    save_json(users, file_path)


# Message functions
def message_functions(user_file, message_file, phone_number, action, message=None):
    users = load_json(user_file)
    messages = load_json(message_file)

    if phone_number not in users:
        return "User not found."

    user_id = users[phone_number]['id']

    if action == 'create':
        if user_id not in messages:
            messages[user_id] = []
        messages[user_id].append({"text": message, "type": "sent", "date": now()})

    elif action == 'read':
        return messages.get(user_id, [])

    elif action == 'delete':
        if user_id in messages:
            del messages[user_id]

    save_json(messages, message_file)

# Stock functions
def stock_functions(user_file, stocks_file, phone_number, action, stock_data=None):
    users = load_json(user_file)
    stocks = load_json(stocks_file)

    if phone_number not in users:
        return "User not found."

    user_id = users[phone_number]['id']

    if action == 'add':
        if user_id not in stocks:
            stocks[user_id] = []
        stocks[user_id].append(stock_data)

    elif action == 'delete':
        if user_id in stocks:
            del stocks[user_id]

    save_json(stocks, stocks_file)


# Main function for testing
def main():
    users_file = 'data/users.json'
    messages_file = 'data/messages.json'
    stocks_file = 'data/stocks.json'
    os.makedirs('data', exist_ok=True)

    user_id = str(uuid.uuid4())
    # Sample data
    users_data = {
        "+491244347937": {
            "id":  user_id,
            "stock_of_interest": ["AAPL", "GOOGL"],
            "delivery_frequency": "on_demand",
            "delivery_time": "18:00",
            "active": True,
            "created_at": "2025-01-14 23:54:43",
            "updated_at": "2025-01-15 01:28:41"
        }
    }
    save_json(users_data, users_file)

    messages_data = {
        user_id: [
            {"text": "Hi!", "type": "received", "date": "2025-01-14 23:54:43"},
            {"text": "Hey!", "type": "sent", "date": "2025-01-14 23:55:10"},
            {"text": "How are you?", "type": "received", "date": "2025-01-14 23:55:45"}
        ]
    }
    save_json(messages_data, messages_file)

    stocks_data = {
        user_id: [
            {
                "Company Name": "Test Company",
                "Open Price": 22,
                "Close Price": 33,
                "High Price": 222,
                "Low Price": 22,
                "Current Price": 100,
                "date": now()
            }
        ]
    }
    save_json(stocks_data, stocks_file)


if __name__ == '__main__':
    main()
