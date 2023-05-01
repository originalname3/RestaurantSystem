import socket


def server_program():
    root = tk.Tk()
    root.geometry("400x600")
    # get the hostname
    host = '169.254.161.194'
    port = 5000

    server_socket = socket.socket()

    server_socket.bind((host, port))

    server_socket.listen(2)
    conn, address = server_socket.accept()
    print("Connection from: " + str(address))
    while True:
        data = conn.recv(1024).decode()
        label = tk.Label(root, text=data)
        label.pack()
        root.mainloop()
        if not data:
            break
        print("from connected user: " + str(data))

    conn.close()


if __name__ == '__main__':
    server_program()
