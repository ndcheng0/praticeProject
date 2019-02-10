from socket import socket, AF_INET, SOCK_STREAM
s = socket(AF_INET, SOCK_STREAM)
s.connect(('localhost', 20000))
s.send(b'Version=1.0')

msg=s.recv(8192)
print(msg)
s.close()

