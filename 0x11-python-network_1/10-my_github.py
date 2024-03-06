#!/usr/bin/python3
"""Python script that takes your GitHub credentials
(username and password) and uses the GitHub API to display your id"""

import requests
import sys

if __name__ == "__main__":
    user_name = sys.argv[1]
    pwrd = sys.argv[2]
    login = requests.get('https://api.github.com/user', auth=(user_name, pwrd))
    print(login.json().get("id"))
