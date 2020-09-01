#!/usr/bin/python3
"""github api
"""
import requests
import sys


if __name__ == "__main__":
    url = 'https://api.github.com'
    agr1 = sys.argv[1]
    arg2 = sys.argv[2]
    url2 = '{}/repos/{}/{}/commits'.format(url, arg2, agr1)
    res = requests.get(url2).json()
    for i in res[0:10]:
        print(i['sha'] + ':', i['commit']['author']['name'])
