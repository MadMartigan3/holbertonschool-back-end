#!/usr/bin/python3
"""Write a Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress."""

import requests
import sys
import json

if __name__ == "__main__":
    EMPLOYEE_ID = sys.argv[1]

    url = "https://jsonplaceholder.typicode.com/"

    TODOS = requests.get("{}/users/{}/todos".format(url, EMPLOYEE_ID),
                         params={"userId": EMPLOYEE_ID})

    data = TODOS.json()

    EMPLOYEE_NAME = data[0].get("name")
    TOTAL_NUMBER_OF_TASKS = len(data)
    NUMBER_OF_DONE_TASKS = 0
    TASK_TITLE = []

    for task in data:
        if task.get("completed") is True:
            NUMBER_OF_DONE_TASKS += 1
            TASK_TITLE.append(task.get("title"))

    print("Employee {} is done with tasks({}/{}):".format(
        EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))

    for title in TASK_TITLE:
        print("\t {}".format(task))
