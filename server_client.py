import socket

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Definesthe host Ip and port number
host = ''  # Host IP
port = 12345  # port number

# Binds the socket to the host and port
server_socket.bind((host, port))

# Listens for other commands
server_socket.listen(5)

print("Server is ready to receive connections...")

while True:
    # Connect/Accept
    client_socket, client_address = server_socket.accept()
    print("Connection from: ", client_address)

    # Receive data
    data = client_socket.recv(1024).decode()
    print("Received data: ", data)

    # Prints the output of selected options
    print(variable)

    # Send a response to the client
    response = "Received data: " + data
    client_socket.send(response.encode())

    # Close the client socket
    client_socket.close()
