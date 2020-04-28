#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
numberld = int(str(number)[-1])
if number < 0:
    numberld *= -1
print("Last digit of {} is {} and is".format(number, numberld), end=" ")

if numberld == 0:
    print(numberld)
elif numberld > 5:
    print("greater than 5")
elif numberld < 6:
    print("less than 6 and not 0")
