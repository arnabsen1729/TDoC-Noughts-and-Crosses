import socket
import sys

class Client:
    def __init__(self, ADDR, DISCON_MSG='QUIT'):
        try:
            self.SOCK = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.DISCON_MSG = DISCON_MSG
            self.ADDR = ADDR
            self.SOCK.connect(ADDR)
            print(f'[CONNECTION SUCCESS] Connected to server {ADDR} ...')
        except:
            print('[SOMETHING WENT WRONG]...')
            sys.exit(0)
        

    def send_message(self, message, FORMAT='utf-8'):
        self.SOCK.send(str.encode(message))

        if(message==''):
            print('[EMPTY STRING FOUND!!')
        # print('sending ', len(message))
        if message == self.DISCON_MSG:
            print("[CONNECTION CLOSED]")
            self.SOCK.close()
            sys.exit(0)
        
    def recv_resp(self, CHUNKS=1024, FORMAT='utf-8'):
        data = self.SOCK.recv(CHUNKS).decode(FORMAT)
        print(f'[RESPONSE FROM {self.ADDR}] : {data}')
        return data

HOST = socket.gethostname()
PORT = 3033 # change this to the port client1 is running
ADDR = (HOST, PORT)

client = Client(ADDR, '\x00')

while client.SOCK:
    data = input('[ENTER MESSAGE]: ')
    if data == '':
        data='\x00'
    client.send_message(data)
    client.recv_resp()
    