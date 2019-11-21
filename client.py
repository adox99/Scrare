
from socket import socket,AF_INET,SOCK_STREAM
from threading import Thread
from time import sleep

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
                 {activeUsers} Active
'''

def helpScreen():
    print('Welcome to the help screen')
    print('Some of the Scrare commands are as follows')
    print('help,p2s-share,p2s-joinshare,p2p-share','p2p-joinshare')
    print('Try a command to get more information about it')

def attemptConn(host, port):
    print(f'Attempting to connect to {host}:{port}')
    with socket(AF_INET, SOCK_STREAM) as s:
        s.connect((host, port))

        s.sendall(bytes(input('Enter username: '), 'utf-8'))

        t = Thread(target=shareScreen, args=(s, ))
        t.start()

        while True:
            inData = s.recv(1024)
            print(inData.decode())

def p2pshare():
    def goodp2p(ui):
        if len(ui.split(':')) == 2:
            if type(ui.split(':')[0]) == str:
                try:
                    int(ui.split(':')[1])
                except:
                    pass
                else:
                    return [ui.split(':')[0], int(ui.split(':')[1])]
        return False
    
    i = ''
    while i != 'exit' or i != 'quit':
        i = input('Please enter IP:HOST you are connecting to\ne.g. 123.45.67.89:8675...\n')
        gp2p = goodp2p(i)
        if gp2p != False:
            break
    attemptConn(gp2p[0], gp2p[1])


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
        pass
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