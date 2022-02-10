#!/usr/bin/python3

from socket import *

def send_back_index():
    f = open("index.html", "r")
    html = f.read()
    return html

def send_back_test():
    f = open("test.html", "r")
    html = f.read()
    return html

server_port = 80
server_socket = socket(AF_INET,SOCK_STREAM)
#server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
server_socket.bind(('',server_port))
server_socket.listen(1)
print("The server is ready to receive")
while True:
    conn_socket,client_address = server_socket.accept()
    try:
        modified_message = conn_socket.recv(2048).decode().upper()
        #conn_socket.send(modified_message.encode())
        print("incoming ip:",client_address)
        print("connection received from {}, and {} is sent back".format(client_address[1],modified_message))
        conn_socket.send(('HTTP/1.0 200 OK\r\n\r\n').encode())
        conn_socket.send(send_back_index().encode())
    except:
        conn_socket.send(('404 Not Found').encode())
        #Close client socket
        conn_socket.close()
        print("connection closed")


    conn_socket.close()
server_socket.close()
