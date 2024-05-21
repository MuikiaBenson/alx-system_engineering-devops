#!/usr/bin/python3
"""
Export data from JSONPlaceholder API to JSON format
"""
import json
import requests


def export_todo_all_employees():
    """
    Fetches data from JSONPlaceholder API and exports it to JSON format
    """
    # Fetching data from the API
    users_url = "https://jsonplaceholder.typicode.com/users"
    todos_url = "https://jsonplaceholder.typicode.com/todos"

    users_response = requests.get(users_url)
    todos_response = requests.get(todos_url)

    users = users_response.json()
    todos = todos_response.json()

    # Preparing the data
    data = {}
    for user in users:
        user_id = str(user["id"])  # Converting user ID to string
        username = user["username"]
        user_tasks = [
            {
                "username": username,
                "task": todo["title"],
                "completed": todo["completed"]
            }
            for todo in todos if todo["userId"] == user_id
        ]
        data[user_id] = user_tasks

    # Writing data to a JSON file
    with open("todo_all_employees.json", "w") as json_file:
        json.dump(data, json_file, indent=4)

    print("Data exported to todo_all_employees.json")


if __name__ == "__main__":
    export_todo_all_employees()
