#!/usr/bin/python3
"""Script that uses REST API to get information about employee
and exports data in JSON format"""
import json
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 2-export_to_JSON.py <employee_id>")
        sys.exit(1)
    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer")
        sys.exit(1)

    url = 'https://jsonplaceholder.typicode.com/'

    user_url = '{}users/{}'.format(url, employee_id)
    user_response = requests.get(user_url)

    if user_response.status_code != 200:
        print("User not found")
        sys.exit(1)

    user_data = user_response.json()
    username = user_data.get('username')

    todos_url = '{}todos?userId={}'.format(url, employee_id)
    todos_response = requests.get(todos_url)
    todos = todos_response.json()

    tasks = []
    for task in todos:
        tasks.append({
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": username
        })

    data = {str(employee_id): tasks}
    json_filename = '{}.json'.format(employee_id)
    with open(json_filename, 'w') as json_file:
        json.dump(data, json_file)
