# # Program for server side socket script

# import socket

# # loopback interface address of the server (localhost in this case)
# HOST = "127.0.0.1"
# PORT = 2204           # port for listening (any non-privileged port > 1023)

# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#     s.bind((HOST, PORT))
#     s.listen()
#     conn, addr = s.accept()        # maximum 1 client connection
#     with conn:
#         print(f"Connection with {addr} successful!")
#         # bufsize = maximum amount of data that can be received
#         while True:
#           msg = input()
#           conn.send(b'msg')
          
import socket


def server_program():
    HOST = socket.gethostname()   # get the hostname
    PORT = 5000                   # use non-privileged ports i.e. #port > 1023

    server_socket = socket.socket()  # get instance
    # look closely. The bind() function takes tuple as argument
    server_socket.bind((HOST, PORT))  # bind host address and port together

    
    server_socket.listen(2)       # how many clients can the server listen to simultaneously
    conn, address = server_socket.accept()  # accept new connection
    print("Connection from: " + str(address))
    while True:
        # receive data stream of data packet size not exceeding 1024 bytes
        data = conn.recv(1024).decode()
        if not data:         # if data is not received break
            break
        print("Client ->  " + str(data))
        data = input('Me -> ')
        conn.send(data.encode())  # send data to the client

    conn.close()  # close the connection


if __name__ == '__main__':
    server_program()          
            


'''
SOCKET : 
  A socket can be thought of as an endpoint in a two-way communication channel. Socket routines create the communication channel, and the channel is used to send data between application programs either locally or over networks.

socket.gethostname : 
  Return a string containing the hostname of the machine where the Python interpreter is currently executing.

socket.AF_INET : 
  AF_INET == IPv4
  A pair (host, port) is used for the AF_INET address family, where host is a string representing either a hostname in internet domain notation like 'daring.cwi.nl' or an IPv4 address like '100.50.200.5', and port is an integer.

socket.SOCK_STREAM == TCP

socket.accept : 
  conn is a new socket object usable to send and receive data on the connection, and address is the address bound to the socket on the other end of the connection.
  
socket.recv : 
  Receive data from the socket. The return value is a bytes object representing the data received.
'''
