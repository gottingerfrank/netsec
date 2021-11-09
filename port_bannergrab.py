#! /usr/bin/python3

import socket

host = "192.168.1.101"
ports = [21, 22, 25, 3306]

for i in range(len(ports) - 1):

    with socket.socket() as sock:
        port = ports[i]
        print(f"This is the Banner for Port {port}")

        sock.connect("192.168.1.101", port)
        data = sock.recv(1024)
        print(data)

