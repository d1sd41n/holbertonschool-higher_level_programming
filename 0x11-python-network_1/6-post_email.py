#!/usr/bin/python3
"""Sends a request to the URL and displays the value of the
variable X-Request-Id
"""
import sys
import requests

if __name__ == "__main__":
    response = requests.post(sys.argv[1], data={'email': sys.argv[2]})
    print(response.text)
