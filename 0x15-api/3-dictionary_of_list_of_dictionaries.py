#!/usr/bin/python3
"""
Script to export data from JSONPlaceholder REST API
and save it in JSON format.
"""

import json
import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1] if len(sys.argv) == 2 else None
    base_url = 'https://jsonplaceholder.typicode.com'

    if user_id:
        url = f'{base_url}/users/{user_id}'
        response = requests.get(url)
        username = response.json().get('username')
        url = f'{base_url}/todos?userId={user_id}'
    else:
        url = f'{base_url}/todos'

    tasks = requests.get(url).json()

    if user_id:
        data = {user_id: []}
        for task in tasks:
            data[user_id].append({
                "username": username,
                "task": task['title'],
                "completed": task['completed']
            })
    else:
        data = {}
        for task in tasks:
            user_id = task['userId']
            if user_id not in data:
                data[user_id] = []
            user_url = f'{base_url}/users/{user_id}'
            username = requests.get(user_url).json()['username']
            data[user_id].append({
                "username": username,
                "task": task['title'],
                "completed": task['completed']
            })

    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(data, json_file)
