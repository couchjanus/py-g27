import socket

# srv_sock = socket.socket()

# print(socket.AF_INET)
# print(socket.SOCK_STREAM)

# print(srv_sock.fileno())
# print(srv_sock.proto)
HOST = '127.0.0.1' 
PORT = 80
with socket.socket() as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    
    with conn:
        print('Connected by ', addr)
        print('IP-address ', addr[0])
        print('TCP PORT ', addr[1])
        
        while True:
            data = conn.recv(1024)
            if not data:
                break
            else:
                print("Data: " + data.decode('utf-8'))
    
