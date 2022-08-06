import socket
import time
from cipher import Cipher
import protocol

class Network:
    
    """ Constructor """
    def __init__(self):
        # Constant
        self.FORMAT = 'utf-8'
        # Create a TCP/IP socket
        self._sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Cipher for encrypted traffic
        self.cipher = Cipher()



    """ Connects to server, must be done before all other operations """
    def connect_to(self, ip : str, port : int):
        # Connect the socket to the port where the server is listening
        print( f"[CONNECTING] IP: {ip} \t PORT: {port}" )
        self._sock.connect((ip, port))
        self.handshake()
        print(self.cipher.encryptKey)


    """ Exchanges keys with Server """
    def handshake(self):
        self._sock.send(self.cipher.getPublicKey().encode(self.FORMAT))
        new_key = self._sock.recv(2048).decode(self.FORMAT)
        self.cipher.addKeyFromString(new_key)
        

    """ Sends msg to server over socket """
    def send(self, msg : str):
        try:
            self._sock.send(self.cipher.encrypt(msg.encode(self.FORMAT)))
        except Exception as e:
            print(f"[NETWORK] Send failed! {e}")
    

    """ Blocks until message is sent, returns the message """
    def recv(self):
        return self.cipher.decrypt(self._sock.recv(2048)).decode(self.FORMAT)
    
    """ Sends request to register to server, username and password should be well regexed """
    def register(self, username : str, password : str):
        out = str( protocol.REGISTER_REQ ) + ":" + username + "," + password
        self.send(out)
        response = int ( self.recv() )
        
        match (response):
            case protocol.REGISTER_FAIL:
                print("[REGISTER] Failed!")

            case protocol.REGISTER_SUCCESS:
                print("[REGISTER] Successfull!")
        
        return response

    def login(self, username : str, password : str):
        out = str( protocol.LOGIN_REQ ) + ":" + username + "," + password
        self.send(out)
        response = int ( self.recv() )
        
        match (response):
            case protocol.LOGIN_FAIL:
                print("[LOGIN] Failed!")

            case protocol.LOGIN_SUCCESS:
                print("[LOGIN] Successfull!")
        
        return response



net = Network()
net.connect_to("localhost", 9848)

time.sleep(2)

# response = net.register("Test1", "NewPass")
response = net.login("Test1", "NewPass")