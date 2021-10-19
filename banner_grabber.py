#! /opt/homebrew/bin/python3

# Simple Banner Grabber

import socket

host_ip = "192.168.0.1"

s = socket.socket()
s.connect((host_ip))

answer = s.recv(1024)
print(f"[+] Received Banner Information of host {host_ip}\n")
print(answer)

s.close()

