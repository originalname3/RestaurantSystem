import socket


def client_program():
    host = socket.gethostname()  # Replace with host IP
    port = 5000  # socket server port number

    client_socket = socket.socket()
    client_socket.connect((host, port))

    # NEEEDS TO BE CHANGED TO WHATEVER THE VARIABLE HAYDEN'S CODE MAKES####
    message = input(" -> ")

    while message.lower().strip() != 'bye':
        client_socket.send(message.encode())
        data = client_socket.recv(1024).decode()

        print('Received from server: ' + data)

        message = input(" -> ")

    client_socket.close()


if __name__ == '__main__':
    client_program()
