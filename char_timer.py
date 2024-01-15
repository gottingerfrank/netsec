#! /usr/bin/env python3


def char_timer(s):
    """chartimer (Loading/Time bar using ASCII Chars"""
    import time

    end = s + 1
    num = 0

    for i in range(end):
        if i == 0:
            print("[", end='') # start char
            time.sleep(2)
            num += 2
        elif i == s:
            print(']') # end char
            time.sleep(1)
            break
        else:
            print('*', end='') # progress char
            time.sleep(1)
            num += 1
    # print(']')
    return num

char_timer(10)