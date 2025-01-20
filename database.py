import json
import os

def save_json(data, json_file_name):
    """
    Save the provided data as a JSON file in the 'data' subfolder.

    Parameters:
    - data: The Python object (e.g., dictionary) to be serialized to JSON.
    - json_file_name: The name of the JSON file (without extension) to save the data.
    """
    data_file_path = os.path.join(data, json_file_name + ".json")
    with open(data_file_path, 'w') as file:
        json.dump(data, file, indent=4)

def load_json(data_file_name):



def main():
    users = {
    "+491244347937": {
        "type": "smoothie",
        "delivery_frequency": "on_demand",
        "delivery_time": "18:00",
        "messages_id": 1,
        "active": False,
        "created_at_": "2025-01-14 23:54:43",
        "updated_at_": "2025-01-15 01:28:41",
    }
}

    messages = {
        1:{"text":"message 1", "type": "received", "date": "2025-01-14 23:54:43"}
    }


    users_json = json.dumps(users, indent=4)
    messages_json = json.dumps(messages, indent=4)

