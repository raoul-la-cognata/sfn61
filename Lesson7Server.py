import socket

#create socket IPV4, TCP
server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#bind the socket to the IP address and port number
server_socket.bind(("127.0.0.1",49156))

#wait for clients
server_socket.listen()

#accept connection from client
client_socket, client_address = server_socket.accept()
print(f"A new client connected using {client_address}")

server_byte = client_socket.recv(1024) #receives data from clients
server_string = server_byte.decode() #changes to string
print(f"Received from client: {server_string}")

server_string_string = "GOODMORNING" #ascii 
server_byte = server_string_string.encode() #change to UTF-8
client_socket.send(server_byte) #send data to client

while True:
    #receive from client
    server_byte = client_socket.recv(1024) #receives data from clients
    server_string = server_byte.decode() #changes to string
    print(f"Received from client: {server_string}")

    if server_string == "EXIT":
        client_socket.close()
        break

    #send to client
    server_string_string = input("Enter a message: ") #ascii 
    server_byte = server_string_string.encode() #change to UTF-8
    client_socket.send(server_byte) #send data to client

    
