#!/usr/bin/python3
"""Script that uses REST API to get information about employee
and exports data in CSV format"""
import csv
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 1-export_to_CSV.py <employee_id>")
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

    csv_filename = '{}.csv'.format(employee_id)
    with open(csv_filename, mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([
                employee_id,
                username,
                task.get('completed'),
                task.get('title')
            ])
