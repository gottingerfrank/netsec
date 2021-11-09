#! /opt/homebrew/bin/python3

import socket

TCP_IP = "192.168.0.1"
TCP_PORT = 5555
BUFFER_SIZE = 100 # Adjust Buffer where needed

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((TCP_IP, TCP_PORT))
s.listen(1)

con, addr = s.accept()
print(f"[*] Connection address: ", addr)

while True:
    data = con.recv(BUFFER_SIZE)

    if not data:
        break
    print(f"[+] Received data: ", data)
    cosend(data) #echo back received data (test)

con.close()
print(f"[-] Connection closed ...")