import select, socket, traceback
from queue import Queue
from database import Database
from cipher import Cipher
import config, protocol
import hashlib, rsa

# Constant for sending messages
FORMAT = 'utf-8'
# TCP
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Non-blocking IO
server.setblocking(0)
# IP, PORT
ADDR = ('localhost', config.PORT) if config.LOCALHOST else (socket.gethostbyname(socket.gethostname()), config.PORT)
server.bind(ADDR)
# Number of Unaccepted connections before refusing new ones (5)
server.listen(5)
# Debug
print("[SERVER] " + str(ADDR))
print("[SERVER] Listening for connections...\n")

# For communication
inputs = [server]
outputs = []
message_queues = {}

# For storing data
db = Database()

#==================================================================================================

""" High level bundle for conn and cipher """
class ClientBundle:
    def __init__(self, conn, cipher):
        self.conn = conn
        self.cipher = cipher
    
    def fileno(self): return self.conn.fileno()
    def send(self, msg): self.conn.send(self.cipher.encrypt(msg))
    def recv(self, bytes): return cipher.decrypt(self.conn.recv(bytes)).decode(FORMAT)
    def close(self): self.conn.close()


""" Disconnect client and remove traces """
def disconnect(s):
    global inputs, outputs, message_queues

    if s in outputs:
        outputs.remove(s)
    inputs.remove(s)
    s.close()
    del message_queues[s]
    print("[CLIENT] Disconnected...")


""" Return hash string for given string """
def compute_hash(data : str) -> str:
    return hashlib.sha224(data.encode(FORMAT)).hexdigest()


""" Sets everything up for message to be sent to socket """
def send_msg(s, msg):
    global message_queues, outputs

    # Add msg to queue
    message_queues[s].enqueue(msg.encode(FORMAT))
    
    # Add socket to write list
    if s not in outputs:
        outputs.append(s)

#==================================================================================================



while inputs:
    readable, writable, exceptional = select.select(
        inputs, outputs, inputs)

    for s in readable:
        if s is server:
            # Accept new client
            connection, client_address = s.accept()

            # Complete cipher handshake
            cipher = Cipher()
            new_key = connection.recv(2048).decode(FORMAT)
            cipher.addKeyFromString(new_key)
            connection.send(cipher.getPublicKey().encode(FORMAT))
            
            # Bundle connection with cipher
            client = ClientBundle(connection, cipher)

            # Set to non-blocking IO
            connection.setblocking(0)
            # Add to list of connected clients
            inputs.append(client)
            # Add queue for client
            message_queues[client] = Queue()
            #Debug
            print("[CLIENT] Got new connection")

        else:
            try:
                # Read msg
                data = s.recv(2048)

                if data:
                    
                    # Print msg
                    print(f"[CLIENT] {data}")
                    
                    #Get code for processing
                    op_code = int ( data.split(":")[0] )
                    data = data.split(":")[1]

                    # Process
                    match (op_code):
                        case protocol.REGISTER_REQ:
                            # Seperate username and password
                            username, password = data.split(",")
                            password = compute_hash(password)
                            # Cannot register, user already exists
                            if db.keyExists(username):
                                send_msg(s, str(protocol.REGISTER_FAIL))
                            else:
                                # Add to database using default values
                                db.addKey(username, [password] + [' ', ' ', ' ', ' '])
                                send_msg(s, str(protocol.REGISTER_SUCCESS))

                        case protocol.LOGIN_REQ:
                            # Seperate username and password
                            username, password = data.split(",")
                            password = compute_hash(password)
                            # Cannot login, user doesn't exist
                            if not db.keyExists(username):
                                send_msg(s, str(protocol.LOGIN_FAIL))
                            else:
                                send_msg(s, str(protocol.LOGIN_SUCCESS))
                                # TODO Send the user the data via 'pickle'


                

                else:
                    # Disconnect client
                    disconnect(s)

            except rsa.pkcs1.DecryptionError:
                # Disconnect client
                disconnect(s)
            except Exception as e:
                # Display error
                print(f"[CLIENT ERROR] {e}")
                print(traceback.format_exc())
                # Disconnect client
                disconnect(s)


    for s in writable:
        if ( not message_queues[s].isEmpty() ):
            # Get next message in queue
            next_msg = message_queues[s].dequeue()

            try:
                # No error, send message
                print(f"[CLIENT] Sending data: {next_msg}")
                s.send(next_msg)

            except Exception as e:
                print(f"[SERVER] Sending failed! {e}")
                outputs.remove(s)

        else:
            outputs.remove(s)


    # Disconnect those that throw errors
    for s in exceptional:
        # Disconnect Client
        disconnect(s)