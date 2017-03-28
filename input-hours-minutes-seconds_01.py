#!/usr/bin/python3.5

import os
import time

def SpaceSeparator():
    print("\n")

os.system('clear')

print("Welcome to PyCountdownTimer!\n\nLet's set up that countdown timer...\n\n")

hours = input("How many hours? ")
SpaceSeparator()
minutes = input("How many minutes? ")
SpaceSeparator()
seconds = input("How many seconds? ")

hours = int(hours)
minutes = int(minutes)
seconds = int(seconds)

hrsToSec = (hours * 60) * 60
mnsToSec = (minutes * 60)
seconds = seconds

seconds = hrsToSec + mnsToSec + seconds

print(seconds)

os.system('clear')

for i in range(seconds, -1, -1):
    displayHours = int(seconds / 3600)
    displayMinutes = int(seconds / 60)
    displaySeconds = int(seconds % 60)
    os.system('clear')
    print("{}:{}:{}".format(str(displayHours).zfill(2), str(displayMinutes).zfill(2), str(displaySeconds).zfill(2)))
    seconds -= 1
    time.sleep(1)

os.system('clear')

print('Timer ended.')
