import socket
class client():
    def __init__(self,PrivateKey,PublicKey):
        self.PrivateKey = PrivateKey
        self.PublicKey = PublicKey
        
    def RunClient(self,IP,Port=5005):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((IP,Port))
        Message = raw_input("Write message and press enter\n")
        sock.send(self.PublicKey.public_encrypt(Message,1))

    def RunServer(self):
        print "Server not implemented"
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(("0.0.0.0",5005))
        sock.listen(1)
        
        conn, addr = sock.accept()
        print "Connection address:", addr
        while 1:
            data = conn.recv(4096)
            if not data: break
            print "received data:", self.PrivateKey.private_decrypt(data,1)
            #conn.send(data)
        conn.close
