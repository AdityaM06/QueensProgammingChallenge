import socket
import time
from cipher import Cipher
import protocol
import pickle
from math import ceil

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


    """ Exchanges keys with Server after connecting """
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
        msg = self._sock.recv(2048)
        return self.cipher.decrypt(msg).decode(self.FORMAT)

    """ Returns list of data that server has for the user """
    def recvPersonalData(self):
        # Number of pieces msg has been split into
        num_blocks = int ( self.recv() )
        print(f"[DUMP] Number of Blocks: {num_blocks}")

        # Read all pieces and put together
        buff = b''
        for i in range(num_blocks):
            buff += self.cipher.decrypt ( self._sock.recv(1024) )
        # Return de-serialized
        return pickle.loads( buff )
    
    """ Sends updated data to be stored on server """
    def updatePersonalData(self, data):
        # Turn data into bytes
        out = pickle.dumps ( data )
        # Let server know we are trying to update, along the number of blocks to receive it
        self.send(f"{protocol.UPDATE_INFO}:" + str ( ceil ( len(out) / self.cipher._max_msg ) ) )

        while out:
            # Cut portion to be encrypted
            buff = out[:self.cipher._max_msg]
            out = out[self.cipher._max_msg:]
            # Send portion to Server
            time.sleep(0.005)
            self._sock.send( self.cipher.encrypt ( buff ) )

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

    """ Send login request to server with credentials, returns server response code """
    def login(self, username : str, password : str):
        # Formulate request for server
        out = str( protocol.LOGIN_REQ ) + ":" + username + "," + password
        self.send(out)
        response = int ( self.recv() )

        # Print appropriate response
        match (response):
            case protocol.LOGIN_FAIL:
                print("[LOGIN] Failed!")
                response, None

            case protocol.LOGIN_SUCCESS:
                print("[LOGIN] Successfull!")
                return response, self.recvPersonalData()
    

        return response, None        





#----------------------------------+
# ╭━━━┳━╮╭━┳━━━┳━╮╭━┳━━━┳╮╱╱╭━━━╮  |
# ┃╭━━┻╮╰╯╭┫╭━╮┃┃╰╯┃┃╭━╮┃┃╱╱┃╭━━╯  |
# ┃╰━━╮╰╮╭╯┃┃╱┃┃╭╮╭╮┃╰━╯┃┃╱╱┃╰━━╮  |
# ┃╭━━╯╭╯╰╮┃╰━╯┃┃┃┃┃┃╭━━┫┃╱╭┫╭━━╯  |
# ┃╰━━┳╯╭╮╰┫╭━╮┃┃┃┃┃┃┃╱╱┃╰━╯┃╰━━╮  |
# ╰━━━┻━╯╰━┻╯╱╰┻╯╰╯╰┻╯╱╱╰━━━┻━━━╯  |
#----------------------------------+

net = Network()
net.connect_to("localhost", 9848)

time.sleep(2)

# response, data = net.register("Test1", "NewPass")                    # Register (user already exists?)
response, data = net.login("Test1", "NewPass")                       # Correct Password login
# response, data = net.login("Test1", "NewPass1")                      # Wrong password login

print(data)
time.sleep(1)

if response == protocol.LOGIN_SUCCESS:
    data[0] = "Vaccinated"
    net.updatePersonalData(data)

    time.sleep(1)