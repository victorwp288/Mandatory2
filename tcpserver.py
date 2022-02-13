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

def logging(response_code):
    f = open("logfile.log", "a")
    ip_from_client = client_address[0]

    response = modified_message.split(" ")[0:3]
    last_line_reponse = response[-1][0:10]
    response.pop()
    response.append(last_line_reponse)
    print(response)
    print(client_address)

    if(response_code == response_404):
        lengh_packet = str(len(str(send_back_index().encode() + response_404.encode())))

    if(response_code == response_400):
        lengh_packet = str(len(str(send_back_index().encode() + response_400.encode())))

    if(response_code == response_200):
        lengh_packet = str(len(str(send_back_index().encode() + response_200.encode())))

    f.write(str(ip_from_client + " "))
    f.write("-- ")
    f.write(str(datetime.now()) + " ")
    f.write(str(response) + " ")
    new_respose_code = response_code.strip()
    f.write(new_respose_code)
    f.write(" " + lengh_packet + "\n")

   
server_port = 8142
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


    response_200 = "HTTP/1.1 200 OK\r\n\r\n"
    response_400 = "HTTP/1.1 400 Bad Request\r\n\r\n"
    response_404 = "HTTP/1.1 404 Not Found\r\n\r\n"


    if modified_message.split(" ")[1] == "/":
        conn_socket.send((response_200).encode())
        conn_socket.send(send_back_index().encode())
        logging(response_200)
    elif modified_message.split(" ")[1] == "/TEST":
        conn_socket.send((response_200).encode())
        conn_socket.send(send_back_test().encode())
        logging(response_200)
    elif modified_message.split(" ")[0] != "GET":
        conn_socket.send((response_400).encode())
        logging(response_400)
    else:
        conn_socket.send((response_404).encode())
        conn_socket.send(('<html><body><h1>404 Not Found</h1></body></html>').encode())
        logging(response_404)

    conn_socket.close()
server_socket.close()