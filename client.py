import socket
import threading
class ListeningThread(threading.Thread):
    def __init__(self,client,socket):
        threading.Thread.__init__(self)
        self.client = client
        self.socket = socket
    def run(self):
        self.client.Listen(self.socket)
        pass

class client():
    active = False
    def __init__(self,PrivateKey,PublicKey):
        self.PrivateKey = PrivateKey
        self.PublicKey = PublicKey
        
    def RunClient(self,IP,Port=5005):
        self.active = True
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((IP,Port))
        ListenThread = ListeningThread(self,sock)
        ListenThread.start()
        self.Sender(sock)
        self.active = False
#        Message = raw_input("Write message and press enter\n")
        

    def RunServer(self):
        self.active = True
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(("0.0.0.0",5005))
        sock.listen(1)
        
        conn, addr = sock.accept()
        ListenThread = ListeningThread(self,conn)
        ListenThread.start()
        self.Sender(conn)
        self.active = False

    def Sender(self, socket):
        while socket:
            Message = raw_input()
            if Message == "exit":
                socket.close
                break
            if socket == False:
                break
            socket.send(self.PublicKey.public_encrypt(Message,1))

    def Listen(self, socket):
        if self.active == True:
            while socket:
                data = socket.recv(4096)
                print self.PrivateKey.private_decrypt(data,1)
        else:
            socket.close()
