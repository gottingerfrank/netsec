#! /usr/bin/python3

import os
import sys
import pty
import time
import platform # need this?

"""
Python3 script to detect the local operating system (OS)
and processor architecture (ARCH),
then spawn an appropriate shell
on the system ...
"""

def get_platform() -> str:
    """Finds the OPERATING SYSTEM platform/family:
    e.g: 'win32' | 'darwin' | 'linux' | [...] 
    Returns system platform found, as a String."""

    platform_found = False

    # platform eg.: 'darwin' | 'win32' | 'linux' | 'aix' | ...
    try:
        OS_PLATFORM = sys.platform
        print(f'[+] Operating System identified as: *** {OS_PLATFORM} ***')

        platform_found = True

        return OS_PLATFORM

    except OSError as PlatformError:
        print('[-] There was a problem identifying this systems OS-Platform...')
        print(str(PlatformError.errno))

    sys.exit(1)


def get_arch() -> str:
    """Finds the PROCESSOR ARCHITECTURE of the systems OS.
    e.g: 'x86' | 'x86-64' | 'arm64' | [...] 
    Returns Architecture found, as a String"""

    arch_found = False

    # architecture eg.: 'x86' | 'x86-64' | 'arm64' | 'arm32'
    try:
        OS_ARCH = os.uname().machine
        print(f'[+] Processor Architecture identified as: *** {OS_ARCH} ***')
        arch_found = True

        if arch_found:
            return OS_ARCH

    except OSError as ArchError:
        print('[-] There was a problem identifying this systems Processor Architecture...')
        print(str(ArchError.errno))

    sys.exit(2)


def main() -> object:
    platform = get_platform()
    arch = get_arch()
    # shell_spawned = False

    if platform == 'linux' or platform == 'darwin' or platform == 'aix':
        shell = 'bash'

        try:
            print(f'[*] Spawning {shell} shell on {platform} {arch} ...')
            time.sleep(1)
            pty.spawn(shell)

        except FileNotFoundError:
            try:
                old_shell = shell
                shell = 'sh'

                print(f'[-] {old_shell} not found on system. Trying {shell} shell ...')
                print(f'[*] Spawning {shell} shell on {platform} {arch} ...')
                time.sleep(1)
                pty.spawn(shell)

            except FileNotFoundError:
                try:
                    old_shell = shell
                    shell = 'zsh'

                    print(f'[-] {old_shell} not found on system. Trying {shell} shell ...')
                    print(f'[*] Spawning {shell} shell on {platform} {arch} ...')
                    time.sleep(1)
                    pty.spawn(shell)

                except FileNotFoundError:
                    try:
                        old_shell = shell
                        shell = 'ksh'

                        print(f'[-] {old_shell} not found on system. Trying {shell} shell ...')
                        print(f'[*] Spawning {shell} shell on {platform} {arch} ...')
                        time.sleep(1)
                        pty.spawn(shell)

                    except:
                        print('')
                        print(f'[-] bash/sh/zsh/ksh ALL FAILED')

        finally:
            print(f'[-] Could not spawn any common {platform} shell on system')
            time.sleep(1)
            print('')
            print(f'*** Spawning Shell FAILED. Exiting script ... ***')


            for i in range(11):
                print('(x_x) ', end='')
                time.sleep(0.5)

            sys.exit(-1)

    elif platform == 'win32':
        shell = 'cmd.exe'

        try:
            print(f'[*] Spawning {shell} shell on {platform} {arch} ...')
            time.sleep(1)
            pty.spawn(shell)

        except FileNotFoundError:
            try:
                old_shell = shell
                shell = 'powershell.exe'

                print(f'[-] {old_shell} not found on system. Trying {shell} shell ...')
                print(f'[*] Spawning {shell} shell on {platform} {arch} ...')
                time.sleep(1)
                pty.spawn(shell)

            except FileNotFoundError:
                try:
                    old_shell = shell
                    shell = 'git-bash.exe'

                    print(f'[-] {old_shell} not found on system. Trying {shell} shell ...')
                    print(f'[*] Spawning {shell} shell on {platform} {arch} ...')
                    time.sleep(1)
                    pty.spawn(shell)

                except FileNotFoundError:
                    try:
                        old_shell = shell
                        shell = 'bash.exe'

                        print(f'[-] {old_shell} not found on system. Trying {shell} shell ...')
                        print(f'[*] Spawning {shell} shell on {platform} {arch} ...')
                        time.sleep(1)
                        pty.spawn(shell)

                    except:
                        print('')
                        print(f'[-] cmd.exe/powershell.exe/git-bash.exe/bash.exe ALL FAILED')

        finally:
            print(f'[-] Could not spawn any common {platform} shell on system')
            time.sleep(1)
            print('')
            print(f'*** Spawning Shell FAILED. Exiting script ... ***')
            sys.exit(-1)

    else:
        print(f'[-] Functions for {platform} on {arch} not implemented yet ...')
        time.sleep(1)

        for i in range(11):
            print('[o_0] ', end='')
            time.sleep(0.5)

        sys.exit(-2)

# Run as script (if not imported as module):
if __name__ == '__main__':
        main()