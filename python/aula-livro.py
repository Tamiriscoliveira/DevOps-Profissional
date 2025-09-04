#socket uma conexão usada para acessar uma combinação de um endereço de host e uma porta.

import socket

socket.gethostbyname("localhost")

socket.gethostbyaddr()

socket.gethostbyname("www.johnmuellerbooks.com")

socket.getaddrinfo("localhost", 110)

socket.getaddrinfo("johnmuellerbooks.com", 80)

socket.getservbyport(25)

socket.gethostname()

socket.gethostbyname(socket.gethostname())



