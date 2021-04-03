import os
import sys
import socket
from utils.Message import Message

class Server:
    """
    A class which manages kernel connections to and from any module.
    """
    def __init__(self, address = None, port = 6541):
        
        #socket service comands
        self.__BUFFER_SIZE = 1024
        self.__server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.__app_port = 6543
        self.__app_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.__file_man_port = 6542
        self.__file_man_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        #http_bind_address 
        self.__address = socket.gethostname() if address == None else address #set default address it's not given
        try:
            bind_address = (self.__address, port)
            self.__server_socket.bind(bind_address)
        except OSError as e:
            print(f"# Server bind failed: {e}")
            sys.exit(1)

    def start(self):
        """
        Connects to each module (FILE and APP) and start listening on server socket
        """
        self.__connect()
        self.__session()

        #self.__listen()
    
    def __connect(self):
        #Connecting to APP socket
        try:
            print(f"# Connecting to APP on {self.__address}:{self.__app_port}")
            self.__app_socket.connect((self.__address, self.__app_port))
            print("# Connected!")
        except ConnectionRefusedError:
            print(f"# Connection refused, please make sure there's a server running.")
            sys.exit(1)
        except InterruptedError as e:
            print(f"# Connection interrupted: {e}")
            sys.exit(1)
    
    def __listen(self):
        # become a server socket
        self.__server_socket.listen(10)
        print('# Server listening')
        while True:
            try:
                # accept connections from outside
                client, address = self.__server_socket.accept()
                # Start a session with the client
                # in this case, we'll pretend this is a processed server
                self.__session()
            except KeyboardInterrupt:
                print("\n# Closing connection")
                self.__server_socket.close()
                sys.exit()
            except:
                print(f"# Disconnected due interrupted connection. :(")
                self.__server_socket.close()
                sys.exit(1)

    def __session(self):
        msg = Message.format(
            "stop", 
            "GUI",
            "APP", 
            {
                "body": "",
                "method": "term",
                "params": {
                    "pid":96967
                }
            })
        self.__app_socket.send(msg.encode())
        data = self.__app_socket.recv(self.__BUFFER_SIZE)
        if data:
            line = data.decode('UTF-8')    # convert to string (Python 3 only)
            print("< " + line )
        else: raise InterruptedError



