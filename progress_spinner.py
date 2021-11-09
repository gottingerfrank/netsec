#! /usr/bin/python3

import time

spinner="\\|/-"
print ("----------\r", end='', flush=True)
for pos in range(10):
    print ("-", end='', flush=True)
    for spin in range(25):
        #here should be a break as soon as some task proceeded further
        time.sleep(0.1)
        print ("\b" + spinner[spin % 4], end='', flush=True)
    print ("\b*", end='', flush=True)
print ()