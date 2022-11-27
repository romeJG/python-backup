import sys, socket, select

HOST=''
SOCKET_LIST=[]
RECV_BUFFER = 4096
PORT = 9009

def chat_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SQL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((HOST, PORT))
    server_socket.listen(10)
    
    SOCKET_LIST.append(server_socket)
    print(f"chat server started on port{str(PORT)}")