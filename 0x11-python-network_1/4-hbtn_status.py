#!/usr/bin/python3
"""script that fetches https://alx-intranet.hbtn.io/status"""

import requests

if __name__ == "__main__":
    reponse = requests.get("https://alx-intranet.hbtn.io/status")
    content = reponse.text
    print("Body response:")
    print("\t - type: {}".format(type(content)))
    print("\t - content: {}".format(content))
