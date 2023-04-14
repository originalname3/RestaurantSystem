import socket

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Defines the host and port
host = '107.0.0.1'  # Pi IP
port = 12345  # Port

# Connects to the server
client_socket.connect((host, port))

# Sends the data to the server
data = "Hello, server!"  # Data is sent through pis and received to the client
client_socket.send(data.encode())

# Receives a response from the server
response = client_socket.recv(1024).decode()
print("Response from server: ", response)

# Close the client socket
client_socket.close()
