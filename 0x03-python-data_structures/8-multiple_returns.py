#!/usr/bin/python3


def multiple_returns(sentence):
    if len(sentence):
        t = (len(sentence), sentence[0])
    else:
        t = (0, None)
    return t
