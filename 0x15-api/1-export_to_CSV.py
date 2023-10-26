#!/usr/bin/python3
"""
Using what you did in the task #0, extend your Python script
to export data in the CSV format.
Format must be: "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
"""

import requests
from sys import argv


def main():
    """Exports to-do list information for a given employee ID to CSV format.
    """
    url = "https://jsonplaceholder.typicode.com/todos"
    r = requests.get(url)
    data = r.json()
    employee_id = argv[1]

    employee_name = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    ).json().get('username')

    with open("{}.csv".format(employee_id), "w") as f:
        for task in data:
            if task.get('userId') == int(employee_id):
                f.write('"{}","{}","{}","{}"\n'.format(
                    task.get('userId'),
                    employee_name,
                    task.get('completed'),
                    task.get('title')
                ))


if __name__ == "__main__":
    main()
