#!/usr/bin/python3
"""script that takes in a URL, sends a request to the URL and
displays the body of the response (decoded in utf-8)"""

import urllib.request
import urllib.error
import sys

if __name__ == "__main__":
    try:
        url = sys.argv[1]
        with urllib.request.urlopen(url) as response:
            result = response.read().decode(utf-8)
            print(result)
    except urllib.error.HTTPError as err:
        print("Error code: {}".format(err.code))
