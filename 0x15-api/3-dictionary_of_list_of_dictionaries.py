#!/usr/bin/python3
"""Exports to-do list information of all employees to JSON format."""
import json
import requests


def main():
    """Exports to-do list information of all employees to JSON format.
    """
    base_url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(base_url + "users").json()

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump({
            u.get("id"): [{
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": u.get("username")
            } for t in requests.get(base_url + "todos",
                                    params={"userId": u.get("id")}).json()]
            for u in users}, jsonfile)


if __name__ == "__main__":
    main()
