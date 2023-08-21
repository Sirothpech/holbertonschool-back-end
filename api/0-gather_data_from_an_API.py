#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
import requests
import sys


def get_employee_todo_list(employee_id):
    # Define the API URL
    base_url = 'https://jsonplaceholder.typicode.com'
    todos_url = f'{base_url}/todos?userId={employee_id}'
    user_url = f'{base_url}/users/{employee_id}'

    # Send requests to the API
    todos_response = requests.get(todos_url)
    user_response = requests.get(user_url)

    # Check if the employee exists
    if user_response.status_code != 200:
        print(f"Error: Employee with ID {employee_id} not found in the API.")
        sys.exit(1)

    # Parse JSON responses
    todos = todos_response.json()
    user = user_response.json()

    # Calculate the number of completed tasks
    completed_tasks = [todo for todo in todos if todo['completed']]

    EMPLOYEE_NAME = user['name']
    TOTAL_NUMBER_OF_TASKS = len(completed_tasks)
    NUMBER_OF_DONE_TASKS = len(todos)
    # Display the employee TODO list progress
<<<<<<< HEAD
    print(f"Employee {user['name']}\
is done with tasks({num_completed_tasks}/{total_tasks}):")
=======
    print(f"Employee {EMPLOYEE_NAME} \
is done with tasks({TOTAL_NUMBER_OF_TASKS}/{NUMBER_OF_DONE_TASKS}):")
>>>>>>> 502df1e (Update the file 0, change the name of variables)
    for task in completed_tasks:
        print(f"\t {task['title']}")


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python3 gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_list(employee_id)
