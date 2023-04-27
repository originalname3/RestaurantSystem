# Slave pi needs to be connected with the printer code. It needs to display and then then send storedvalue to the printer after it is displayed.

import socket

host = '192.0.0.2'  # I need to add whatever the ip of the slave pi is
port = 5000  # Add the open/used port number for the slave pi 0000 is placeholder

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

while True:
    command = input("Enter your command: ")
    if command == 'EXIT':
        # Send EXIT request to other end
        s.send(str.encode(command))
        break
    elif command == 'KILL':
        # Send KILL command
        s.send(str.encode(command))
        break
    s.send(str.encode(command))
    reply = s.recv(1024)
    print(reply.decode('utf-8'))

s.close()
