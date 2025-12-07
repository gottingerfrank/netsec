#!/usr/bin/env python3


# simpleTCP server


import socket


IP = "192.168.0.15"
PORT = 5555
BUFFER_SIZE = 1024  # Adjust Buffersize if needed


# create tcp socket and bind to IP-Address
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((IP, PORT))
s.listen(1)


# accept outside connection
con, addr = s.accept()
print("[*] Connection from address: ", addr)


# receive data and print out
while True:
    data = con.recv(BUFFER_SIZE)
    if not data:  # if there is no more data, stop
        break
    print("[+] Received data: ", data)
    con.send(data)  # echo back received data (test)


con.close()
print("[-] Connection closed ...")
