#!/usr/bin/env python3
from prompt_toolkit.output.flush_stdout import flush_stdout

isfound = False


def toggle_spin():
    """Function to stop the spinner"""
    global isfound
    if isfound == True:
        isfound = False
    isfound = True


def spin(bars=10):
    """Displays a spinning progress bar using ASCII chars"""
    import time

    # Global variable to control when to stop the spinner
    global isfound

    spinner = r"\\|/-"
    printed = 0

    while not isfound and printed != bars:
        print("-", end='', flush=True)

        for i in range(25):
            time.sleep(0.1)
            print("\b" + spinner[i % 4], end='', flush=True)

        print("\b|", end='', flush=True)
        printed += 1

    if printed:
        return printed

    return None


# test spinner
spin(7)
