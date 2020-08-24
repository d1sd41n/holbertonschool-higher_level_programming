#!/usr/bin/python3
"""get an status
"""
from urllib.request import Request, urlopen


if __name__ == "__main__":
    with urlopen('https://intranet.hbtn.io/status') as re:
        r = re.read()
        print('Body response:')
        print('\t- type: {}'.format(r))
        print('\t- content: {}'.format(r))
        print('\t- utf8 content: {}'.format(r.decode('utf-8')))
