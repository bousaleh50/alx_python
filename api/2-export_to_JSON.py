"""
  fetching data from an api and make it as a json file
"""


import json
import requests
import sys

def get_employee_data(employee_id):
    # Define the API endpoints
    user_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    todos_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos'

    # Get employee details
    user_response = requests.get(user_url)
    user_data = user_response.json()
    employee_name = user_data.get('name')

    # Get TODO list for the employee
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    # Calculate the number of completed tasks and total tasks
    completed_tasks = [task for task in todos_data if task['completed']]
    total_tasks = len(todos_data)

    # Print the employee's progress
    print(f"Employee {employee_name} is done with tasks({len(completed_tasks)}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t{task['title']}")

    # Export data to JSON file
    export_data = {str(employee_id): [
        {
            "task": task["title"],
            "completed": task["completed"],
            "username": employee_name
        }
        for task in todos_data
    ]}

    json_filename = f'{employee_id}.json'
    with open(json_filename, 'w') as json_file:
        json.dump(export_data, json_file, indent=4)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_data(employee_id)