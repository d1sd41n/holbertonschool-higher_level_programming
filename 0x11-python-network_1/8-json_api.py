#!/usr/bin/python3
"""sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter.
"""
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("No result")
    else:
        try:
            url = 'http://0.0.0.0:5000/search_user'
            re = requests.post(url, data={'q': sys.argv[1]}).json()
            if re:
                print("[{}] {}".format(re.get("id"), re.get("name")))
            else:
                print("No result")
        except Exception:
            print("Not a valid JSON")
