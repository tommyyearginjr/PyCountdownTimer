#!/usr/bin/python3.5

import time
import os

seconds = input("How many seconds to BLAST OFF? ")

os.system('clear')

def abc():
    for i in range(int(seconds),0,-1):
        os.system('clear')
        print(":{}".format(str(i).zfill(2)))
        time.sleep(1)

abc()
os.system('clear')
print('BLAST OFF!!!')
