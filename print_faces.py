#! /usr/bin/python3

import sys
import time


def print_faces(face='(x_x) ', num=3):
    """Prints {num} number of Faces after another w/o a newline.
    Returns {num} faces printed"""

    end = num + 1
    count = 0

    for i in range(end):
        print(face, end='')
        time.sleep(1)
        count += 1

        if count == num:
            break

    return count


def main(face='+_+ ', num=5):
    print_faces(face, num)
    sys.exit(num)

# Run as script with ARGS IF ARGS exist AND script NOT imported as module


if __name__ == '__main__':
    # if there are ARGS ...
    if len(sys.argv) > 1:
        args = [print(f"{x}, ", end='') for x in sys.argv[1:]]
        main(args)  # run script with ARGS
    else:
        main()  # else run without ARGS (using default params)