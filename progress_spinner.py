#! /usr/bin/env python3

# needs more work

import time
import sys


# noinspection Annotator
def spin(found=False):
    """Prints spinning timer bar(s), with ARG 'bars' #bars.
    Stops when ARG 'found' (global 'isfound') evaluates to True.
    Default: 10 bars + autostop if NO ARGS given"""
    global isfound

    while True:
        spinner = "\\|/-"

        print("----------\r", end="", flush=True)

        for pos in range(10):
            print("-", end="", flush=True)
            for spin in range(25):
                # break statement here when task completed
                found = isfound
                if found:
                    print()
                    break
                time.sleep(0.1)
                print("\b" + spinner[spin % 4], end="", flush=True)
            print("\b*", end="", flush=True)


def main(*args, **kwargs):
    # check out argparse and getopt modules!
    if len(sys.argv) <= 2:
        spin(int(sys.argv[1]))
    elif len(sys.argv) < 2:
        spin()
    else:
        print("[-] There is a problem with use of the spin() function. Exiting ...")
        sys.exit(-3)


if __name__ == "__main__":
    if len(sys.argv) > 3:
        print(f"Usage: python3 spin.py [bars] [found]")
    elif len(sys.argv) == 3:
        try:
            main(sys.argv[1], sys.argv[2])
            main(sys.argv[1], sys.argv[2])
        except:
            print(f"[-] Faulty arguments!")
            print(f"Usage: python3 spin.py [bars] [found]")
            sys.exit(3)
    elif len(sys.argv) == 2:
        try:
            main(sys.argv[1], sys.argv[2])
        except:
            print(f"[-] Faulty arguments!")
            print(f"Usage: python3 spin.py [bars] [found]")
            print(f"With only one ARGUMENT:", f"Usage: python3 spin.py [found]")
            sys.exit(2)
    else:
        main()

# Run
main(10)
