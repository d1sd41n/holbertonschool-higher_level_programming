#!/usr/bin/python3
""" 6-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(10, 6, 3, 5)
    r1.display()

    print("---")

    r2 = Rectangle(3, 2, 1, 0)
    r2.display()
