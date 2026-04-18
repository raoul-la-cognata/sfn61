import socket

#create socket IPV4, TCP
socket_client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#connect to server
socket_client.connect(("127.0.0.1",49156))

#send HELLO to server
client_string = "HELLO" #ascii 
client_byte = client_string.encode() #change to UTF-8
socket_client.send(client_byte) #send data to server

#receive from server
client_byte = socket_client.recv(1024)
client_string = client_byte.decode()
print(f"Received from server: {client_string}")

while True:
    #send to server
    client_string = input("Enter a message: ") #ascii 
    client_byte = client_string.encode() #change to UTF-8
    socket_client.send(client_byte) #send data to server

    if client_string == "EXIT":
        socket_client.close()
        break

    #receive from server
    client_byte = socket_client.recv(1024)
    client_string = client_byte.decode()
    print(f"Received from server: {client_string}")