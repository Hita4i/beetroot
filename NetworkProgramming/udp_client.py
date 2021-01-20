from socket import *


client = socket(AF_INET, SOCK_DGRAM)
print('Client created')


HOST = '127.0.0.1'
PORT = 6400
SOCKADDR = (HOST, PORT)

client.bind(SOCKADDR)
print(f'client connected')

while True:
    print('Sending message...')
    client.sendto(bytes(input('>>>'), 'utf-8'), (HOST, 6401))
    data, addr = client.recvfrom(2048)
    print(data.decode('utf-8'))
