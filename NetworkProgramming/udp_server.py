from socket import *


server = socket(AF_INET, SOCK_DGRAM)
print('server created')


HOST = '127.0.0.1'
PORT = 6401
SOCKADDR = (HOST, PORT)

server.bind(SOCKADDR)

while True:
    data, addr = server.recvfrom(2048)
    print(data.decode('utf-8'))
    print('Sending message...')
    server.sendto(bytes(input('>>>'), 'utf-8'), (HOST, 6400))
