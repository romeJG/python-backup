import socket
try:
    s = socket.socket()
    host = socket.gethostname()
    port = 1248
    s.connect((host,port))
    print(s.recv(1024))
    s.close()
except ConnectionRefusedError:
    print("Server not available!")