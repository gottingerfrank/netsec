#! /opt/homebrew/bin/python3

# Simple SSH Banner Grabber

import socket

host_ip = ("192.168.0.1", 22) # set host ssh connection tuple (IP_ADDR, PORT)

s = socket.socket()
s.connect((host_ip))

answer = s.recv(1024)

print(f"[+] Received Banner Information of host {host_ip}")
print(f"**************************** SSH Banner {host_ip} ****************************")
print(answer)
print(f"**************************** Banner END **************************************")

s.close()
