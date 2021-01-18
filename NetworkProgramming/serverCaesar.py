import socket

HOST = '127.0.0.1'  # Standard loop-back interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)


def caesar(data):
    alpha = ' abcdefghijklmnopqrstuvwxyz'
    res = ''
    for c in data:
        res += alpha[(alpha.index(c) + 3) % len(alpha)]
    conn.sendall(res.encode('utf-8'))


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            caesar(data.decode('utf-8'))
