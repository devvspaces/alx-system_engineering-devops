#!/usr/bin/python3
"""
Write a Python script that, using this REST API,
for a given employee ID, returns information about his/her TODO list progress.
"""

import requests
from sys import argv


def main():
    """Returns information about his/her TODO list progress.
    """
    url = "https://jsonplaceholder.typicode.com/todos"
    r = requests.get(url)
    data = r.json()
    completed = 0
    total = 0
    tasks = []
    employee_id = argv[1]
    for task in data:
        if task.get('userId') == int(employee_id):
            total += 1
            if task.get('completed'):
                completed += 1
                tasks.append(task.get('title'))

    url = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    name = requests.get(url).json().get('name')

    print("Employee {} is done with tasks({}/{}):".format(
        name, completed, total))
    for task in tasks:
        print("\t {}".format(task))


if __name__ == "__main__":
    main()
