#!/usr/bin/python3

"""
Module
export data in the JSON format
"""

import json
import requests


def main():
    todos_url = "https://jsonplaceholder.typicode.com/todos"

    todos = requests.get(todos_url).json()
    output = {}

    for todo in todos:
        user_id = todo.get('userId')
        if user_id not in output.keys():
            output[user_id] = []
            user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(
                user_id)
            user_name = requests.get(user_url).json().get('username')

        output[user_id].append(
            {
                "username": user_name,
                "task": todo.get('title'),
                "completed": todo.get('completed')
            })

    with open("todo_all_employees.json", "w") as f:
        json.dump(output, f)


if __name__ == "__main__":
    main()
