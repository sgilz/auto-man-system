import os
import sys
import socket
from utils.Message import Message

class Server:

    def __init__(self):

        self.__BUFFER_SIZE = 1024
        self.__server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.__kernel_port = 6541
        self.__kernel_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def start(self):
        """
        Connections
        """
        self.__connect()

    def __connect(self):
        """
        Connection to KERNEL
        """
        try:
            print(f"# Connecting to KERNEL on {self.__address}:{self.__app_port}")
            self.__kernel_socket.connect((self.__address, self.__app_port))
            print("# Connected!")
        except ConnectionRefusedError as e:
            print(f"# Connection refused, please make sure all of the servers are running: {e}")
            sys.exit(1)
        except InterruptedError as e:
            print(f"# Connection interrupted: {e}")
            sys.exit(1)

    def __execute(self, request):
        pass

if __name__ == "__main__":
    client = Server()
    client.start()