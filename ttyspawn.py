#!/usr/bin/python3

import os
import sys
import pty
import time

isfound = False  # Global variable to control spinner


def get_platform():
    try:
        OS_PLATFORM = sys.platform
        print(f"[+] Operating System identified as: {OS_PLATFORM}")
        return OS_PLATFORM
    except os.error as e:
        print("[-] There was a problem identifying this system's OS-Platform: ", e)
        return None


def get_arch():
    try:
        OS_ARCH = os.uname().machine
        print(f"[+] Processor Architecture identified as: {OS_ARCH}")
        return OS_ARCH
    except os.error as e:
        print("[-] There was a problem identifying this system's Processor-Architecture:", e)
        return None


def spin(bars=10):
    """Displays a spinning progress bar using ASCII chars"""
    import time

    global isfound

    spinner = "\\|/-"
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


def toggle_spin():
    """Function to stop the spinner"""
    global isfound
    isfound = not isfound


def main():
    OS_PLATFORM = get_platform()
    OS_ARCH = get_arch()

    if OS_PLATFORM and OS_ARCH:
        print(
            f"""            
            *********************************************************
            *   Starting shell spawner @ {time.ctime()}   *
            *********************************************************
            """
        )

        spin()  # Start the spinner
        time.sleep(1.4)
        print("[+] Found system platform (OS)")
        time.sleep(0.7)
        print("[+] Found processor architecture (SysArch)")
        time.sleep(1.4)
        toggle_spin()  # Stop the spinner

        if OS_PLATFORM == "linux" and "64" in OS_ARCH:
            print("[+] Linux 64-bit detected: Spawning Linux shell.")
            try:
                pty.spawn('/bin/bash')
            except FileNotFoundError:
                try:
                    pty.spawn('/bin/zsh')
                except FileNotFoundError as e:
                    print(f'{e}: Could not find Bash or Zshell')

            exit(2)

        elif OS_PLATFORM == "win32" and "64" in OS_ARCH:
            print("[+] Windows 64-bit detected: Trying Powershell")
            try:
                pty.spawn('C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe')
            except Exception as e:
                print(f'[-] Could not spawn Powershell: {e}')
                try:
                    pty.spawn(r'C:\Windows\System32\cmd.exe')
                except FileNotFoundError as e:
                    print(f'{e}: Could not find any Windows shell: Exiting')

            exit(2)

        elif OS_PLATFORM == "win32" and "32" in OS_ARCH:
            print("[+] Windows 32-bit detected: Trying Powershell...")
            try:
                pty.spawn('C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe')
            except:
                print('[•] Checking other directories for Powershell executables...')
            try:
                pty.spawn('C:\Windows\SysWOW64\WindowsPowerShell\v1.0\powershell.exe')
            except FileNotFoundError as e:
                print(f'{e}')
                print('[-] Could not spawn Powershell')
                print('[+] Trying cmd.exe... ')
                try:
                    pty.spawn('C:\Windows\System32\cmd.exe')
                except FileNotFoundError as e:
                    print(f'{e}: Could not find any Windows shell: Exiting')
            exit(2)

        elif OS_PLATFORM == "darwin":
            print("[+] macOS detected. Spawning macOS shell...")
            try:
                pty.spawn('/bin/bash')  # Use shell of choice for macOS/darwin
            except FileNotFoundError as e:
                print(f'{e}: Could not find specified shell for macOS: Exiting')

            exit(2)

        elif OS_PLATFORM == "solaris":
            print("[+] Solaris Unix detected. Spawning shell...")
            try:
                pty.spawn('/bin/sh')  # Use shell of choice for Solaris
            except FileNotFoundError as e:
                print(f'{e}: Could not find specified shell for Solaris: Exiting')

            exit(2)

        elif OS_PLATFORM == "bsd":
            print("[+] BSD Unix detected. Spawning shell...")
            try:
                pty.spawn('/bin/sh')  # Use shell of choice for BSD
            except FileNotFoundError as e:
                print(f'{e}: Could not find specified shell for BSD: Exiting')

            exit(2)

    else:
        print("[-] Found unsupported OS/CPU Architecture: Exiting")
        exit(1)

    exit(0)


if __name__ == "__main__":
    main()
