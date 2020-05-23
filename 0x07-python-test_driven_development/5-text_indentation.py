#!/usr/bin/python3
"""prints text
"""


def text_indentation(text):
    """[prints text]

    Arguments:
        text {[str]} -- [text]
    """
    if type(text) != str:
        raise TypeError("text must be a string")
    text2 = ""
    for i in text:
        if i in (".:?"):
            text2 += i + "\n\n"
        else:
            text2 += i
    text3 = ""
    for i, c in enumerate(text2.split("\n")):
        if i == 0:
            text3 += c.strip()
            continue
        text3 += "\n" + c.strip()
    print(text3, end="")
