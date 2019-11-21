
from socket import socket,AF_INET,SOCK_STREAM
from threading import Thread
from time import sleep
from zlib import compress,decompress

activeUsers = 1232

intro = f'''
  ██████  ▄████▄   ██▀███   ▄▄▄       ██▀███  ▓█████ 
▒██    ▒ ▒██▀ ▀█  ▓██ ▒ ██▒▒████▄    ▓██ ▒ ██▒▓█   ▀ 
░ ▓██▄   ▒▓█    ▄ ▓██ ░▄█ ▒▒██  ▀█▄  ▓██ ░▄█ ▒▒███   
  ▒   ██▒▒▓▓▄ ▄██▒▒██▀▀█▄  ░██▄▄▄▄██ ▒██▀▀█▄  ▒▓█  ▄ 
▒██████▒▒▒ ▓███▀ ░░██▓ ▒██▒ ▓█   ▓██▒░██▓ ▒██▒░▒████▒
▒ ▒▓▒ ▒ ░░ ░▒ ▒  ░░ ▒▓ ░▒▓░ ▒▒   ▓▒█░░ ▒▓ ░▒▓░░░ ▒░ ░
░ ░▒  ░ ░  ░  ▒     ░▒ ░ ▒░  ▒   ▒▒ ░  ░▒ ░ ▒░ ░ ░  ░
░  ░  ░  ░          ░░   ░   ░   ▒     ░░   ░    ░   
      ░  ░ ░         ░           ░  ░   ░        ░  ░
         ░   High Res Screen Sharing
               Private Chat Rooms
            {activeUsers} Active Users
'''

CLIENTS = []

def b(data):
    return (bytes(data, 'utf-8'))

class Server():
    def __init__(self, ip='127.0.0.1', port=6969):
        self.ip = ip
        self.port = port
        self.name = ''
    def setServerName(name):
        self.name = name
    def getServerName():
        return self.name

class ScrareClient():
    def __init__(self, sock, addr):
        self.sock = sock
        self.addr = addr
        self.user = ''
    def interact(self, sock):
        while True:
            try:
                if self.user == '':
                    data = sock.recv(512).decode()
                    self.user = data
                    print(f'{self.addr} was named {self.user}')
                else:
                    data = sock.recv(4096).decode()
                    print(f'{self.user} said {data}')
            except:
                pass

class ScrareServer():
    def __init__(self, host, port):
        self.host = host
        self.port = port
    def startServer(self):
        with socket(AF_INET, SOCK_STREAM) as s:
            s.bind((self.host, self.port))
            print(f'Server bound to {self.host}:{self.port}')

            while True:
                s.listen()
                sock, addr = s.accept()
                client = ScrareClient(sock, addr)
                print(f'New client connection at: {addr}')
                client.interact(sock)

def goodp2p(ui):
    if ui == '':
        return ['127.0.0.1', 6969]
    if len(ui.split(':')) == 2:
        if type(ui.split(':')[0]) == str:
            try:
                int(ui.split(':')[1])
            except:
                pass
            else:
                return [ui.split(':')[0], int(ui.split(':')[1])]
    return False

def helpScreen():
    print('Welcome to the help screen')
    print('Some of the Scrare commands are as follows')
    print('help,p2s-share,p2s-joinshare,p2p-share','p2p-joinshare')
    print('Try a command to get more information about it')

def activeServer(sock, serverName):

    print(f'Joined {serverName}')

    i = ''
    while i != '**disconnect' or i != '**leave' or i != '**quit' or i != '**exit':
        i = input(f'{serverName}$ ')
        sock.send(b(i))
    sock.send(b('disconnect'))
    
def attemptConn(host, port):
    print(f'Attempting to connect to {host}:{port}')
    with socket(AF_INET, SOCK_STREAM) as s:
        try:
            s.connect((host, port))
        except:
            print('Could not connect!')
        else:
            activeServer(s, f'{host}:{port}')

def hostServer(host, port):
    ss = ScrareServer(host, port)
    Thread(target=ss.startServer())

def p2pjoinshare():
    i = ''
    while i != 'exit' or i != 'quit':
        i = input('Please enter IP:HOST you are connecting to (e.g. 123.45.67.89:8675)\n')
        gp2p = goodp2p(i)
        if gp2p != False:
            break
    attemptConn(gp2p[0], gp2p[1])

def p2pshare():
    i = ''
    while i != 'exit' or i != 'quit':
        i = input('Please enter IP:HOST you are hosting from (e.g. 123.45.67.89:8675)\n')
        gp2p = goodp2p(i)
        if gp2p != False:
            break
    hostServer(gp2p[0], gp2p[1])


def processSinput(i):
    if i == 'help' or i == 'man' or i == 'manual':
        helpScreen()
    elif i == 'p2s-share':
        pass
    elif i == 'p2s-joinshare':
        pass
    elif i == 'p2p-share':
        print('Using p2p share CAN BE UNSAFE!\nYour connection will be peer-peer!')
        ii = input("If this is okay type 'start' to continue...\n")
        if ii == 'start':
            p2pshare()
    elif i == 'p2p-joinshare':
        print('Using p2p joinshare CAN BE UNSAFE!\nYour connection will be peer-peer!')
        ii = input("If this is okay type 'start' to continue...\n")
        if ii == 'start':
            p2pjoinshare()
    else:
        print("Command not found - Try 'help' for more information")

def main():
    ni = ''
    for x in intro:
        print(x, end='')
        sleep(0.00001)

    sinput = ''
    while sinput != 'exit' or sinput != 'quit':
        sinput = input('scrare$ ')
        processSinput(sinput)

if __name__ == "__main__":
    main()