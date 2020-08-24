#!/usr/bin/python3
"""display your id from github.
"""
from sys import argv
import requests


if __name__ == "__main__":
    get = requests.get('https://api.github.com/user',
                       auth=(argv[1], argv[2])).json().get('id')
    print(get)
