import os
import sys
import socket
from utils.Message import Message

class Server:
    """
    A class which manages 
    """
    def __init__(self, address = None, port = 6541):

        #socket service comands
        self.__BUFFER_SIZE = 1024
        self.__server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.__kernel_port = 6541
        self.__kernel_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def start(self):
        """
        Connects to each module (FILE and APP) and start listening on server socket
        """
        self.__connect()
        self.__session()

    def __connect(self):
        #Connecting to APP socket
        try:
            print(f"# Connecting to KERNEL on {self.__address}:{self.__app_port}")
            self.__kernel_socket.connect((self.__address, self.__app_port))
            print("# Connected!")
        except ConnectionRefusedError:
            print(f"# Connection refused, please make sure there's a server running.")
            sys.exit(1)
        except InterruptedError as e:
            print(f"# Connection interrupted: {e}")
            sys.exit(1)

    def __session(self):
        msg = Message.format(
            "send", 
            "GUI",
            "APP", 
            {
                "body": "",
                "method": "stat",
                "params": {
                }
            })
        self.__kernel_socket.send(msg.encode())
        data = self.__kernel_socket.recv(self.__BUFFER_SIZE)
        if data:
            line = data.decode('UTF-8')    # convert to string (Python 3 only)
            print("< " + line )
        else: raise InterruptedError

    def createDir(self, nameDir):
        msg = Message.format(
            "send", 
            "GUI",
            "FILE_MAN", 
            {
                "body": "",
                "method": "createDir",
                "params": {
                    "nameDir": nameDir
                }
            })
        self.__kernel_socket.send(msg.encode())
        data = self.__kernel_socket.recv(self.__BUFFER_SIZE)
        if data:
            line = data.decode('UTF-8')    # convert to string (Python 3 only)
            print("< " + line )
        else: raise InterruptedError

    def deleteDir(self, nameDir):
        msg = Message.format(
            "send", 
            "GUI",
            "FILE_MAN", 
            {
                "body": "",
                "method": "deleteDir",
                "params": {
                    "nameDir": nameDir
                }
            })
        self.__kernel_socket.send(msg.encode())
        data = self.__kernel_socket.recv(self.__BUFFER_SIZE)
        if data:
            line = data.decode('UTF-8')    # convert to string (Python 3 only)
            print("< " + line )
        else: raise InterruptedError


    def setFileName(self, fileName):
        msg = Message.format(
            "send", 
            "GUI",
            "FILE_MAN", 
            {
                "body": "",
                "method": "setFileName",
                "params": {
                    "fileName": fileName
                }
            })
        self.__kernel_socket.send(msg.encode())
        data = self.__kernel_socket.recv(self.__BUFFER_SIZE)
        if data:
            line = data.decode('UTF-8')    # convert to string (Python 3 only)
            print("< " + line )
        else: raise InterruptedError

    def listLogs(self):
        msg = Message.format(
            "send", 
            "GUI",
            "FILE_MAN", 
            {
                "body": "",
                "method": "listLogs",
                "params": {
                }
            })
        self.__kernel_socket.send(msg.encode())
        data = self.__kernel_socket.recv(self.__BUFFER_SIZE)
        if data:
            line = data.decode('UTF-8')    # convert to string (Python 3 only)
            print("< " + line )
        else: raise InterruptedError

    def listDirectoriesInDirectory(self):
        msg = Message.format(
            "send", 
            "GUI",
            "FILE_MAN", 
            {
                "body": "",
                "method": "listDirectoriesInDirectory",
                "params": {
                }
            })
        self.__kernel_socket.send(msg.encode())
        data = self.__kernel_socket.recv(self.__BUFFER_SIZE)
        if data:
            line = data.decode('UTF-8')    # convert to string (Python 3 only)
            print("< " + line )
        else: raise InterruptedError

    def setPriority(self, priority_id):
        msg = Message.format(
            "send", 
            "GUI",
            "APP", 
            {
                "body": "",
                "method": "prior",
                "params": {
                    "priority_id": priority_id
                }
            })
        self.__kernel_socket.send(msg.encode())
        data = self.__kernel_socket.recv(self.__BUFFER_SIZE)
        if data:
            line = data.decode('UTF-8')    # convert to string (Python 3 only)
            print("< " + line )
        else: raise InterruptedError

    def terminateProcess(self, pid):
        msg = Message.format(
            "send", 
            "GUI",
            "APP", 
            {
                "body": "",
                "method": "term",
                "params": {
                    "pid": pid
                }
            })
        self.__kernel_socket.send(msg.encode())
        data = self.__kernel_socket.recv(self.__BUFFER_SIZE)
        if data:
            line = data.decode('UTF-8')    # convert to string (Python 3 only)
            print("< " + line )
        else: raise InterruptedError

    def updateProcess(self):
        msg = Message.format(
            "send", 
            "GUI",
            "APP", 
            {
                "body": "",
                "method": "stat",
                "params": {
                }
            })
        self.__kernel_socket.send(msg.encode())
        data = self.__kernel_socket.recv(self.__BUFFER_SIZE)
        if data:
            line = data.decode('UTF-8')    # convert to string (Python 3 only)
            print("< " + line )
        else: raise InterruptedError