#!/usr/bin/python3
""" sends a request to the URL and displays the body of the response
"""
import sys
from urllib.request import Request, urlopen
from urllib.error import HTTPError

if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with urlopen(url) as re:
            print(re.read().decode('utf-8'))
    except HTTPError as e:
        print('Error code: {}'.format(e.code))
