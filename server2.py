import socket
HOST = 'localhost'
PORT = 1234
SEND_SIZE=1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST,PORT))
s.listen()
print("server listening on port",PORT)

def send_music(conn,n):
    if n=='1':
        with open('1.mp3', 'rb') as f:
            while True:
                data = f.read(SEND_SIZE)
                if not data:
                    break
                conn.sendall(data)
    elif n=='2':
        with open('2.mp3', 'rb') as f:
            while True:
                data = f.read(SEND_SIZE)
                if not data:
                    break
                conn.sendall(data)
    elif n=='3':
        with open('3.mp3', 'rb') as f:
            while True:
                data = f.read(SEND_SIZE)
                if not data:
                    break
                conn.sendall(data)
    elif n=='4':
        with open('4.mp3', 'rb') as f:
            while True:
                data = f.read(SEND_SIZE)
                if not data:
                    break
                conn.sendall(data)
    elif n=='5':
        with open('5.mp3', 'rb') as f:
            while True:
                data = f.read(SEND_SIZE)
                if not data:
                    break
                conn.sendall(data)
    else:
        print("invalid input")
while True:
    conn, addr = s.accept()
    print(f"Connected by {addr}")
    n=conn.recv(1024).decode()
    send_music(conn,n)
    conn.close()