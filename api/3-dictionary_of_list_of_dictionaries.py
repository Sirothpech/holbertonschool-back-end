#!/usr/bin/python3
"""
Python script that, using this REST API, for all employees,
returns information about his/her TODO list progress and exports it to a JSON.
"""
import csv
import json
import requests
import sys


def export_to_json():
    base_url = 'https://jsonplaceholder.typicode.com'
    users_url = f'{base_url}/users'

    users_response = requests.get(users_url)

    if users_response.status_code != 200:
        print("Error: Unable to fetch user data from the API.")
        sys.exit(1)

    users = users_response.json()

    data = {}

    for user in users:
        user_id = str(user['id'])
        username = user['username']

        todos_url = f'{base_url}/todos?userId={user_id}'
        todos_response = requests.get(todos_url)

        if todos_response.status_code != 200:
            print(f"Error: Unable to fetch todos data for user {user_id}.")
            continue

        todos = todos_response.json()

        data[user_id] = []

        for todo in todos:
            task_title = todo['title']
            task_completed = todo['completed']

            data[user_id].append({
                "username": username,
                "task": task_title,
                "completed": task_completed
            })

    filename = 'todo_all_employees.json'

    with open(filename, 'w') as json_file:
        json.dump(data, json_file)


if __name__ == '__main__':
    export_to_json()
