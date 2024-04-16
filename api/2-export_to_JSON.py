#!/usr/bin/python3
""""Python script to export data in the JSON format."""

import json
import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]

    url = "https://jsonplaceholder.typicode.com/"

    user = requests.get(url + "users/{}".format(user_id)).json()
    username = user.get("username")

    params = {"userId": user_id}
    todos = requests.get(url + "todos", params).json()

    data_to_export = {
        user_id: [
            {
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": task.get("user").get("username")
            }
            for task in todos
        ]
    }

    with open("{}.json".format(user_id), "w") as jsonfile:
        json.dump(data_to_export, jsonfile, indent=4)
