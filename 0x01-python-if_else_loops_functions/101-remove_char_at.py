#!/usr/bin/python3
def remove_char_at(str, n):
    aux = n + 1
    if n >= 0:
        str = str[:n] + str[aux:]
    return str
