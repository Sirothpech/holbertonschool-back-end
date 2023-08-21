#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress and exports it to a CSV file.
"""
import requests
import sys
import csv  # Ajoutez l'importation du module csv

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

    # Create a CSV file for the employee
    csv_filename = f'{employee_id}.csv'
    with open(csv_filename, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)

        # Write the task data
        for task in todos:
            csv_writer.writerow([user['id'], user['username'],
                                str(task['completed']), task['title']])

    print(f"Data exported to {csv_filename}")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python3 gather_data_and_export_to_CSV.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_list(employee_id)
