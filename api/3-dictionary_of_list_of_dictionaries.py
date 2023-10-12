import csv
import json
import requests
import sys



def get_employee_todo_progress(employee_id):
    # Define the base URL for the API
    base_url = "https://jsonplaceholder.typicode.com"

    # Create the URLs for employee details and their TODO list
    employee_url = f"{base_url}/users/{employee_id}"
    todo_url = f"{base_url}/users/{employee_id}/todos"

    # Send a GET request to the employee details endpoint
    employee_response = requests.get(employee_url)
    employee_data = employee_response.json()

    if employee_response.status_code != 200:
        print(f"Error: Unable to retrieve employee details for ID {employee_id}")
        return

    # Send a GET request to the TODO list endpoint
    todo_response = requests.get(todo_url)
    todo_data = todo_response.json()

    if todo_response.status_code != 200:
        print(f"Error: Unable to retrieve TODO list for employee ID {employee_id}")
        return

    # Calculate the number of completed and total tasks
    completed_tasks = [task for task in todo_data if task["completed"]]
    num_completed_tasks = len(completed_tasks)
    total_tasks = len(todo_data)

    # Display employee TODO list progress
    print(f"Employee {employee_data['name']} is done with tasks({num_completed_tasks}/{total_tasks}):")

    # Display titles of completed tasks
    for task in completed_tasks:
        print(f"\t {task['title']}")

    
    
    # Export data to JSON
    json_filename = "todo_all_employees.json"
    with open(json_filename, "w") as json_file:
        json.dump(all_employee_tasks, json_file, indent=4)

if __name__ == "__main__":
    employee_id = sys.argv[1]
    get_employee_todo_progress(employee_id)
