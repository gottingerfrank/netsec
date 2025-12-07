import socket

HOST = 'www.google.com'
PORT = 80

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

client.send(b'GET / HTTP/1.1\r\nHost: google.com\r\n\r\n')
response = client.recv(4096)
print(response.decode('utf-8'))

client.close()
import socket

def tcp_connect():
    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Define the server address and port
    server_address = ('localhost', 65432)
    
    try:
        # Connect to the server
        client_socket.connect(server_address)
        
        # Send data to the server
        message = 'Hello, Server!'
        client_socket.sendall(message.encode())
        
        # Receive data from the server
        data = client_socket.recv(1024)
        print('Received from server:', data.decode())
    
    finally:
        # Close the connection
        client_socket.close()

if __name__ == "__main__":
    tcp_connect()