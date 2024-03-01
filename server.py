import socket

host, port = ('', 5566)

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind((host,port))
("Le serveur est démarré !")

while True: 
    socket.listen()
    