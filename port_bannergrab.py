#! /usr/bin/python3


#set constants
HOST = "192.168.0.1"
PORTS = (20, 21, 22, 80, 143, 443)


def grab_banners(host, ports):
    """simple banner grabber for a set IP Address and set ports
    param host: str
    param ports: tuple
    """
    import socket
    import time

    BUFFERSIZE = 1024

    for port in ports:
        with socket.socket() as s:
            result = s.connect_ex((host, port))
            if result != 0:
                print(f"[-] Could not connect to host {host} on port {port}")
            else:
                print(f"[+] Connecting to host {host} on port {port}")
                print(f"********** Data start: {host}:{port} @ {time.ctime()} **********")
                while True:
                    data = s.recv(BUFFERSIZE)
                    if not data:
                        break
                    print(data.decode())
                print(f"*********** Data end: {host}:{port} @ {time.ctime()} **********")


if __name__ == "__main__":
    grab_banners(HOST, PORTS)
