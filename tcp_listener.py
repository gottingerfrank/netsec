#!/usr/bin/env python3


# imports
import socket


TCP_IP = "192.168.0.15"
TCP_PORT = 5555
BUFFER_SIZE = 100  # Adjust Buffer where needed


# create tcp socket and bind to IP-Address
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)


# accept outside connection
con, addr = s.accept()
print("[*] Connection from address: ", addr)


# receive data and print out
while True:
    data = con.recv(BUFFER_SIZE)
    if not data:  # if there is no data, stop
        break
    print("[+] Received data: ", data)
    con.send(data)  # echo back received data (test)


con.close()
print("[-] Connection closed ...")