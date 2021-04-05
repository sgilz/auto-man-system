import os
import sys
import socket
import json
from utils.Message import Message

class Client:
    """
    A class which manages 
    """
    def __init__(self, address = None, port = 6541):

        #socket service comands
        self.__BUFFER_SIZE = 2048

        self.__kernel_port = port
        self.__kernel_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.__address = socket.gethostname() if address == None else address 


    def connect(self):
        #Connecting to APP socket
        try:
            print(f"# Connecting to KERNEL on {self.__address}:{self.__kernel_port}")
            self.__kernel_socket.connect((self.__address, self.__kernel_port))
            print("# Connected!")
        except ConnectionRefusedError:
            print(f"# Connection refused, please make sure there's a server running.")
            sys.exit(1)
        except InterruptedError as e:
            print(f"# Connection interrupted: {e}")
            sys.exit(1)

    def status(self):
        msg = Message.format(
            "info", 
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
            response = Message(line)
            msge = response.get_msg()
            body = json.loads(msge["body"])
            return [tuple(d.values()) for d in body ]
        else: raise InterruptedError

    def createDir(self, nameDir):
        msg = Message.format(
            "info", 
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
            "info", 
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
            "info", 
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

    def readLogFile(self):
        msg = Message.format(
            "info", 
            "GUI",
            "FILE_MAN", 
            {
                "body": "",
                "method": "readLogFile",
                "params": {
                }
            })
        self.__kernel_socket.send(msg.encode())
        data = self.__kernel_socket.recv(self.__BUFFER_SIZE)
        if data:
            line = data.decode('UTF-8')    # convert to string (Python 3 only)
            print("< " + line )
            response = Message(line)
            msge = response.get_msg()
            return json.loads(msge["body"])
            
        else: raise InterruptedError

    def listDirectoriesInDirectory(self):
        msg = Message.format(
            "info", 
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

    def setPriority(self, priority_id, pid):
        msg = Message.format(
            "info", 
            "GUI",
            "APP", 
            {
                "body": "",
                "method": "prior",
                "params": {
                    "priority_id": priority_id,
                    "pid": pid
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
            "info", 
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

    def halt(self):
        msg = Message.format(
            "info", 
            "GUI",
            "APP", 
            {
                "body": None,
                "method": "halt",
                "params": None
            })
        self.__kernel_socket.send(msg.encode())
        data = self.__kernel_socket.recv(self.__BUFFER_SIZE)
        if data:
            line = data.decode('UTF-8')    # convert to string (Python 3 only)
            print("< " + line )
        else: raise InterruptedError

    def launch(self):
        msg = Message.format(
            "info", 
            "GUI",
            "APP", 
            {
                "body": None,
                "method": "launch",
                "params": None
            })
        self.__kernel_socket.send(msg.encode())
        data = self.__kernel_socket.recv(self.__BUFFER_SIZE)
        if data:
            line = data.decode('UTF-8')    # convert to string (Python 3 only)
            print("< " + line )
        else: raise InterruptedError

    def stopProcess(self):
        msg = Message.format(
            "stop", 
            "GUI",
            "KERNEL", 
            {
                "body": None,
                "method": None,
                "params": None
            })
        self.__kernel_socket.send(msg.encode())
        data = self.__kernel_socket.recv(self.__BUFFER_SIZE)
        if data:
            line = data.decode('UTF-8')    # convert to string (Python 3 only)
            print("< " + line )
        else: raise InterruptedError