#!/usr/bin/python3
"""
A Python script to fetch and display the TODO list progress of an employee using the JSONPlaceholder API.
"""

import requests
import sys

def fetch_todo_list_progress(employee_id):
    """Fetch and display the TODO list progress for a given employee ID."""
    url = "https://jsonplaceholder.typicode.com/"
    
    # Fetch user information
    user_response = requests.get(f"{url}users/{employee_id}")
    if user_response.status_code != 200:
        print("Failed to retrieve user data. Please check the employee ID.")
        return

    user = user_response.json()
    if not user:
        print("No user found with the provided ID.")
        return

    # Fetch TODO tasks for the user
    todos_response = requests.get(f"{url}todos", params={"userId": employee_id})
    if todos_response.status_code != 200:
        print("Failed to retrieve TODOs.")
        return

    todos = todos_response.json()

    # Filter completed tasks
    completed = [task["title"] for task in todos if task["completed"]]

    # Display results
    print(f"Employee {user['name']} is done with tasks({len(completed)}/{len(todos)}):")
    for title in completed:
        print(f"\t {title}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    fetch_todo_list_progress(sys.argv[1])
