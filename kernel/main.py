import os
import sys
import socket
from utils.Message import Message
from kernel.Kernel import Kernel

class Server:
    """
    Class which manages initialization, communication and completion stages.
    It manages kernel connections to and from any module into its communication stage.
    """
    def __init__(self, address = None, port = 6541):
        self.__kernel = Kernel()

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
        self.__listen()
    
    def __connect(self):
        #Connecting to APP socket
        try:
            print(f"# Connecting to APP on {self.__address}:{self.__app_port}")
            self.__app_socket.connect((self.__address, self.__app_port))
            print("# Connected!")

            print(f"# Connecting to FILE_MAN on {self.__address}:{self.__file_man_port}")
            self.__file_man_socket.connect((self.__address, self.__file_man_port))
            print("# Connected!")
        except ConnectionRefusedError as e:
            print(f"# Connection refused, please make sure all of the servers are running: {e}")
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
                self.__session(client, address)
            except KeyboardInterrupt:
                print("\n# Closing connection")
                self.__server_socket.close()
                sys.exit()
            except:
                print(f"# Disconnected due interrupted connection. :(")
                self.__server_socket.close()
                sys.exit(1)

    def __session(self, client, address):
        while True:
            data = client.recv(self.__BUFFER_SIZE)
            if data:
                request = data.decode('UTF-8').replace('\n','') # convert to string (Python 3 only)
                print(f"< {address}: {request}")
                response = self.__execute(request)
                client.send(response.encode())
            else:
                print(f"# Disconnected: {address}")
                break
        client.close()

    def __execute(self, request):
        request_obj = Message(request)
        
        #send request log
        request_log = self.__kernel.generate_log(request_obj)
        self.__file_man_socket.send(request_log.encode())
        print("< request log response: " + self.__file_man_socket.recv(self.__BUFFER_SIZE).decode('UTF-8').replace('\n',''))

        cmd = request_obj.get_cmd()
        dst = request_obj.get_dst()
        response = ""
        if cmd == "info":
            if dst == "APP":
                self.__app_socket.send(request.encode())
                response = self.__app_socket.recv(self.__BUFFER_SIZE).decode('UTF-8').replace('\n','')
            elif dst == "FILE_MAN":
                self.__file_man_socket.send(request.encode())
                response = self.__file_man_socket.recv(self.__BUFFER_SIZE).decode('UTF-8').replace('\n','')
            else:
                response_msg = {
                    "body":f"error: no such destination {dst} for command {cmd}"
                }
                response = Message.format("send", "KERNEL", request_obj.get_src(), response_msg)
        elif cmd == "stop":
            if dst == "KERNEL":
                pass
            else:
                response_msg = {
                    "body":f"error: you cannot stop single modules"
                }
                response = Message.format("send", "KERNEL", request_obj.get_src(), response_msg)
        else:
            response_msg = {
                "body":f"error: no such command {cmd}"
            }
            response = Message.format("send", "KERNEL", request_obj.get_src(), response_msg)
        
        print(f"< {self.__address}: {response}")
        #Send response log
        response_obj = Message(response)
        response_log = self.__kernel.generate_log(response_obj)
        self.__file_man_socket.send(response_log.encode())
        print("< response log response: " + self.__file_man_socket.recv(self.__BUFFER_SIZE).decode('UTF-8').replace('\n',''))
        
        return response

if __name__ == "__main__":
    kernel = Server()
    kernel.start()
