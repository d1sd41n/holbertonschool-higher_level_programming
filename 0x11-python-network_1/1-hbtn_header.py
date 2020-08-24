#!/usr/bin/python3
"""gets X-Request-Id of the header
"""
import sys
import urllib.request


if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as re:
        print(re.getheader('X-Request-Id'))
