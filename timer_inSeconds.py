import time
import os

os.system('clear')

someNumber = input("How long until BLAST OFF (in seconds)? ")
someNumber = int(someNumber)

os.system('clear')

for i in range(someNumber,-1,-1):
    minutes = int(someNumber / 60)
    seconds = int(someNumber % 60)
    os.system('clear')
    print("{}:{}".format(str(minutes).zfill(2), str(seconds).zfill(2)))
    someNumber -= 1
    time.sleep(1)

os.system('clear')

print('BLAST OFF!')
