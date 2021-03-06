#!/usr/bin/python3.5

import os
import time
import random

def SpaceSeparator():
    print("\n")

os.system('clear')

SpaceSeparator()
print("     Welcome to PyCountdownTimer!\n\n     Let's set up that countdown timer...\n\n")

hours = input("     How many hours? ")
SpaceSeparator()
minutes = input("     How many minutes? ")
SpaceSeparator()
seconds = input("     How many seconds? ")

if hours or minutes or seconds == "":
    print("Invalid entry. You must enter a number.")

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
    if displayMinutes >= 60:
        displayMinutes = displayMinutes - (displayHours * 60)
    else:
        displayMinutes = displayMinutes
    displaySeconds = int(seconds % 60)
    os.system('clear')
    print("\n     Your time remaining is: {}:{}:{}".format(str(displayHours).zfill(2), str(displayMinutes).zfill(2), str(displaySeconds).zfill(2)))
    seconds -= 1
    time.sleep(1)

os.system('clear')

randQuot = ('I bid you peace.', 'May the Force be with you.', 'Live long and prosper.', 'May God bless.', 'Happy trails to you, \'til we meet again.')

print('\n     Timer ended. {}\n'.format(random.choice(randQuot)))
