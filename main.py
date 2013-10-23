from M2Crypto import RSA
import client

def PrintChoice():
    print "1. generate key"
    print "2. Load Private key"
    print "3. Load Public key"
    print "4. start server"
    print "5. start client"
    print "100. exit"

def MakePair(name):
    key = RSA.gen_key(1024,65537)
    key.save_key(name + ".key", cipher=None)
    key.save_pub_key(name + ".key.pub")

while (True):
    PrintChoice()
    choice = input()
    if choice == 1:
        keyname = raw_input("Enter key name:\n")
        MakePair(keyname)
    elif choice == 2:
        keyname = raw_input("Enter keyname:\n")
        PrivateKey = RSA.load_key(keyname + ".key")
        print "private key successfully loaded"
    elif choice == 3:
        keyname = raw_input("Enter keyname:\n")
        PublicKey = RSA.load_pub_key(keyname + ".key.pub")
        print "public key successfully loaded"
    elif choice == 4:
        servclient = client.client(PrivateKey,PublicKey)
        servclient.RunServer()
    elif choice == 5:
        print "client not yet implemented"
        servclient = client.client(PrivateKey,PublicKey)
        IP = raw_input("Choose ip to connect to")
        servclient.RunClient(IP)
    elif choice == 100:
        break
