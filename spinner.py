#!/usr/bin/env python3


def spin():
    import time
    """Prints spinning timer bar(s)
    Stops when ARG 'found' (global 'isfound') evaluates to True.
    Default: 10 bars + autostop if NO ARGS given"""

    while True:
        spinner = "\\|/-"

        for pos in range(10):
            print("-", end='', flush=True)
            for spin in range(25):
                time.sleep(0.1)
                print("\b" + spinner[spin % 4], end='', flush=True)
            print("\b|", end='', flush=True)


# test spinner
spin()
time.sleep(5)
found = True