import socket
print("Ready for connection")
s = socket.socket()
host = socket.gethostname()
port = 1248
s.bind((host, port))
s.listen(5)
while True:
    c, addr = s.accept()
    print(f'Got Connection from {addr}')
    v = b'You are connected!'
    c.send(v)
    c.close()