#!/usr/bin/python3
"""
send an email in the header
"""
import sys
from urllib.parse import urlencode
from urllib.request import Request, urlopen

if __name__ == "__main__":
    data = urlencode({'email': sys.argv[2]})
    reque = Request(sys.argv[1], data.encode('utf-8'))
    with urlopen(reque) as re:
        print(re.read().decode('utf-8'))
