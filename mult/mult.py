#!/usr/bin/python

import random
import openal

youpie = openal.oalOpen("cheer.wav")
fail = openal.oalOpen("glass.wav")

while True:
    a = random.randrange(0, 12)
    b = random.randrange(0, 12)
    print("How much is {} * {} ?".format(a, b))
    c = input()
    if (a*b) == int(c):
        print("Well done!")
        youpie.play()
    else:
        print("No, sorry it is wrong...")
        fail.play()
