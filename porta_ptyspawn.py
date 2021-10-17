#! /opt/homebrew/bin/python3

import os
import sys
import platform
import pty
import time


# """ Python3 script to detect the local operating system (OS)
# and processor architecture (ARCH),
# then spawn an appropriate shell
# on the system ... """


def get_platform() -> str:
    """Finds the Operating System platform/family:
    e.g: 'win32' | 'darwin' | 'linux' | [...] 
    Returns system platform found, as a String."""

    platform_found = False

    # platform eg.: 'darwin' | 'win32' | 'linux' | 'aix' | ...
    try:
        OS_PLATFORM = sys.platform
        print(f'[+] Operating System identified as: *** {OS_PLATFORM} ***')

        platform_found = True

    except os.error as PlatformError:
        print('[-] There was a problem identifying this systems OS-Platform...')
        print str(PlatformError)

    sys.exit(1)


def get_arch() -> str:
    """Finds the Processor Architecture of the systems OS.
    e.g: 'x86' | 'x86-64' | 'arm64' | [...] 
    Returns Architecture found, as a String"""

    arch_found = False

    # architecture eg.: 'x86' | 'x86-64' | 'arm64' | 'arm32'
    try:
        OS_ARCH = os.uname().machine
        print(f'[+] Processor Architecture identified as: *** {OS_ARCH} ***')

        arch_found = True

    except os.error as ArchError:
        print('[-] There was a problem identifying this systems Processor-Architecture...')
        print(str(ArchError))

    sys.exit(2)


def char_timer(s:int) -> int:
    """Takes one int: Number of Seconds - as Argument.
    Returns one int: Number of chars printed."""
    end = s + 1
    num = 0
    # start charTimer printing ...
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
    # Return number of chars printed...
    return num


def main():
    get_platform()
    get_arch()

    if get_platform() and get_arch():
        print(
            '''
            ***************************************
            ***  Script executed successfully!  ***
            ***************************************
            ''')
        time.sleep(1.4)
        print('[+] Found system platform (OS)')
        time.sleep(0.7)
        print('[+] Found processor architecture (SysArch)')
        time.sleep(0.7)
        print('[+] *** Now spawning Shell ***\n')
        time.sleep(2)

        char_timer(7)

# case clauses OR if-elif-else clauses:
# to determine specific OS/Arch Combination
# and spawn an appropriate shell ...

# cases: 

# ...
# to be continued ... (18.9.2021 - 8:15am)

def main():
    if __name__ == '__main__':
        main()