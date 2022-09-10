import socket


def client_program():
    host = socket.gethostname()  # as both code is running on same pc
    port = 5000                   # socket server port number

    client_socket = socket.socket()       # create a new socket
    client_socket.connect((host, port))   # connect to the server

    message = input(" -> ")               # enter your message

    while message.lower().strip() != 'bye':
        client_socket.send(message.encode())      # send encoded message
        data = client_socket.recv(1024).decode()  # receive response and decode

        print('Server -> ' + data)  # show in terminal

        message = input("Me -> ")  # again take input

    client_socket.close()  # close the connection


if __name__ == '__main__':
    client_program()