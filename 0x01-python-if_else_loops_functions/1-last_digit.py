#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
numberld = int(str(number)[-1])
if number < 0:
    numberld *= -1

if numberld == 0:
    str1 = numberld
elif numberld > 5:
    str1 = "greater than 5"
elif numberld < 6:
    str1 = "less than 6 and not 0"

print("Last digit of {} is {} and is {}".format(number, numberld, str1))
