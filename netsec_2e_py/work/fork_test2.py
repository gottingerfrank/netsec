#!/usr/bin/env python3


import os

pid = os.fork()

if pid > 0:
    # Code in this block runs in the parent process
    print("Parent process")
    print(f"Parent PID: {os.getpid()}, Child PID: {pid}")

elif pid == 0:
    # Code in this block runs in the child process
    print("Child process")
    print(f"Child PID: {os.getpid()}")

else:
    # Code in this block runs if fork() failed
    print("Fork failed")
