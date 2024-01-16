#! /usr/bin/python3


host = "192.168.0.1"
ports = (20, 21, 22, 80, 143, 443)


def grab_banners(host, ports):
    """simple banner grabber for a set IP Address and set ports
    param host: str
    param ports: tuple
    """
    import socket

    BUFFERSIZE = 1024

    for port in ports:
        with socket.socket() as s:
            result = s.connect_ex((host, port))
            if result != 0:
                print(f"[-] Could not connect to host {host} on port {port}")
            print(f"[+] Connecting to host {host} on port {port}")
            print(f"********** Data **********")
            while True:
                data = s.recv(BUFFERSIZE)
                if not data:
                    break
                print(data)
            print(f"*********** End **********")


if __name__ == "__main__":
    grab_banners(host, ports)
