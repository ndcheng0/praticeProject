from socketserver import BaseRequestHandler, TCPServer
from _thread import *

from socket import socket, AF_INET, SOCK_STREAM

class Server():

    def __init__(self):
        pass
    def start(self,address):
        sock = socket(AF_INET, SOCK_STREAM)
        sock.bind(address)
        sock.listen(3)
        print('Socket now listening')

        while True:
            client_sock, client_addr = sock.accept()
            start_new_thread(self.echo_handler(), (client_addr, client_sock))

    def echo_handler(self,address, client_sock):
        print('Got connection from {}'.format(address))
        client_sock.send(b'Hello')
        while True:
            msg = client_sock.recv(8192)
            if not msg:
                break
            # client_sock.sendall(msg)
            print(msg)
            if (msg == b'Version=1.0'):
                print('A')
        client_sock.close()










if __name__ == '__main__':
    ser=Server()
    ser.start(('', 20000))