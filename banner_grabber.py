#! /usr/bin/python3

# Simple SSH Banner Grabber

import socket

# set host ssh connection tuple (IP_ADDR, PORT), protocol = TCP
host_ip = ("192.168.0.15", 22)

s = socket.socket()
s.connect(host_ip)

answer = s.recv(1024)

print(f"[+] Received Banner Information of host {host_ip}")
print(f"************************ SSH Banner {host_ip} ************************\n")
print(answer, "\n")
print(f"************************ Banner END **********************************\n")

s.close()