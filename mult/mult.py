#!/usr/bin/python

import random

print(random.randrange(0, 12))

while True:
    a = random.randrange(0, 12)
    b = random.randrange(0, 12)
    print("How much is {} * {} ?".format(a, b))
    c = input()
    if (a*b) == int(c):
        print("Well done!")
    else:
        print("No, sorry it is wrong...")
