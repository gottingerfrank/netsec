#!/usr/bin/env python3


import os

pid = os.fork()

if pid > 0:
    # This is the parent process
    print(f"Parent process with PID: {os.getpid()}, Child PID: {pid}")

elif pid == 0:
    # This is the child process
    print(f"Child process with PID: {os.getpid()}")

else:
    # Fork failed
    print("Fork failed")
