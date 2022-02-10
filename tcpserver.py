#!/usr/bin/python3

from socket import *
from datetime import *

def send_back_index():
    f = open("index.html", "r")
    html = f.read()
    return html

def send_back_test():
    f = open("test.html", "r")
    html = f.read()
    return html

#ikke færdig
def logging(response_code):
    f = open("logfile.log", "a")
    ip_from_client = client_address[1]

    #man får HOST: med, dette er ikke godt!!!
    response = modified_message.split(" ")[0:3]
    print(response)

    #Ligner ikke ip-adresse
    f.write(str(ip_from_client))
    f.write(str(datetime.now()))
    f.write(str(response))
    f.write(response_code)


server_port = 80
server_socket = socket(AF_INET,SOCK_STREAM)
#server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
server_socket.bind(('',server_port))
server_socket.listen(1)
print("The server is ready to receive")
while True:
    conn_socket,client_address = server_socket.accept()
    modified_message = conn_socket.recv(2048).decode().upper()
    #conn_socket.send(modified_message.encode())
    print("incoming ip:",client_address)
    print("connection received from {}, and {} is sent back".format(client_address[1],modified_message))
    print(modified_message.split(" ")[1])
    response_200 = "HTTP/1.1 200 OK\r\n\r\n"
    response_404 = "HTTP/1.1 404 Not Found\r\n\r\n"
    if modified_message.split(" ")[1] == "/":
        conn_socket.send((response_200).encode())
        conn_socket.send(send_back_index().encode())
        logging(response_200)
    elif modified_message.split(" ")[1] == "/TEST":
        conn_socket.send((response_200).encode())
        conn_socket.send(send_back_test().encode())
        logging(response_200)
    else:
        conn_socket.send((response_404).encode())
        conn_socket.send(('<html><body><h1>404 Not Found</h1></body></html>').encode())
        logging(response_404)

    conn_socket.close()
server_socket.close()
