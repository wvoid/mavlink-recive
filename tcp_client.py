import socket
import time

if __name__=="__main__":
    host = "127.0.0.1"
    port = 2000
    addr = (host, port)
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(addr)
    buf = client.recv(512)
    print(buf.hex(' '),buf.dtype)
    client.close()
    print("ewq")