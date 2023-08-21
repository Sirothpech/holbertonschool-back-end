#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress and exports it to a JSON.
"""
import json
import requests
import sys


def get_employee_todo_list(employee_id):
    base_url = 'https://jsonplaceholder.typicode.com'
    todos_url = f'{base_url}/todos?userId={employee_id}'
    user_url = f'{base_url}/users/{employee_id}'

    todos_response = requests.get(todos_url)
    user_response = requests.get(user_url)

    if user_response.status_code != 200:
        print(f"Error: Employee with ID {employee_id} not found in the API.")
        sys.exit(1)

    todos = todos_response.json()
    user = user_response.json()

    json_filename = f'{employee_id}.json'

    # Create a data structure in JSON format
    data = {str(user['id']): [{
        "task": task['title'],
        "completed": task['completed'],
        "username": user['username']} for task in todos]}

    # Write this JSON data structure to a file
    with open(json_filename, 'w') as jsonfile:
        json.dump(data, jsonfile)

    print(f"Data exported to {json_filename}")


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python3 gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_list(employee_id)
