#!/usr/bin/python3
"""sends a request to the URL and displays the body of the response.
"""
import sys
import requests

if __name__ == "__main__":
    request = requests.get(sys.argv[1])
    status = request.status_code
    if status >= 400:
        print('Error code:', status)
    else:
        print(request.text)
