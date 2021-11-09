#! /usr/bin/python3

import socket

HOST = "192.168.1.101"
PORTS = [21, 22, 25, 3306]
BUFFERSIZE = 1024

for i in range(len(PORTS) - 1):

    with socket.socket() as s:
        port = PORTS[i]
        print(f"This is the Banner for port {port}")

        s.connect("192.168.1.101", port)
        data = s.recv(BUFFERSIZE)
        print(data)

