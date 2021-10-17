#! /usr/bin/python3

def char_timer(s: int): -> int 
    """chartimer (Loading/Time bar using ASCII Chars"""
    import time
    
    end = s + 1
    num = 0

    for i in range(end):
        if i == 0:
            print("# ", end='')
            time.sleep(2)
            num += 2
        elif i == s:
            print('.')
            time.sleep(1)
            break
        else:
            print('.', end='')
            time.sleep(1)
            num += 1

    return num