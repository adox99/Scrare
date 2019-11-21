
from socket import socket,AF_INET,SOCK_STREAM
from threading import Thread

INIT_CONNECTIONS = {
    'HOST', '127.0.0.1',
    'PORT', 6969
}

CLIENTS = []

class ClientConn():
    self.sock = ''
    self.addr = ''
    self.user = ''
    
    def __init__(self, sock, addr):
        self.sock = sock
        self.addr = addr
    
    def runPrompt(self):
        pass


def incomingConnections():
    host = INIT_CONNECTIONS['HOST']
    port = INIT_CONNECTIONS['PORT']

    with socket(AF_INET, SOCK_STREAM) as s:
        s.bind((host, port))
        print(f'Server binded on {host}:{port}')

        while 1:
            s.listen()
            sock, addr = s.accept()
            newCli = ClientConn(sock, addr)
            newCli.runPrompt()
            CLIENTS.append(newCli)

def main():
    
    Thread(target=incomingConnections)

if __name__ == "__main__":
    main()