#!/usr/bin/python3
"""Script that uses JSONPlaceholder API to get information about employee"""
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
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
    employee_name = user_data.get('name')

    todos_url = '{}todos?userId={}'.format(url, employee_id)
    todos_response = requests.get(todos_url)
    todos = todos_response.json()

    completed_tasks = [task for task in todos if task.get('completed')]
    number_of_done_tasks = len(completed_tasks)
    total_number_of_tasks = len(todos)

    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, number_of_done_tasks, total_number_of_tasks))
    for task in completed_tasks:
        print("\t {}".format(task.get('title')))
