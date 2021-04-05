import json 
import socket 
import sys
from file_manager.filemanager import FileManager
from utils.Message import Message

class Server:
    def __init__(self, address = None, port = 6542):
        self.__file_manager = FileManager('Logs-1.log')
        self.__file_manager.createLog()

        #socket service comands
        self.__BUFFER_SIZE = 2048
        self.__socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #http_bind_address 
        address = socket.gethostname() if address == None else address #set default address it's not given
        try:
            bind_address = (address, port)
            self.__socket.bind(bind_address)
        except OSError as e:
            print(f"# Bind failed: {e}")
            sys.exit(1)

    def start(self):
        # become a server socket
        self.__socket.listen(10)
        print('# Server listening')
        while True:
            try:
                # accept connections from outside
                client, address = self.__socket.accept()
                # Start a session with the client
                # in this case, we'll pretend this is a processed server
                self.__session(client, address)
            except KeyboardInterrupt:
                print("\n# Closing connection")
                client.close()
                self.__socket.close()
                sys.exit()
            except Exception as e:
                print(f"# Disconnected due interrupted connection. : {e}")
                client.close()
                self.__socket.close()
                sys.exit(1)

    def __session(self, client, address):
        print(f"# Connected: {address}")
        while True:
            data = client.recv(self.__BUFFER_SIZE)
            if data:
                msg = data.decode('UTF-8').replace('\n','') # convert to string (Python 3 only)
                print(f"< {address}: {msg}")
                response = self.__execute(msg)
                client.send(response.encode())
                if "BYE" in response:
                    client.close()
                    self.__socket.close()
                    sys.exit(0)
            else:
                print(f"# Disconnected: {address}")
                break
        client.close()
    
    def __execute(self, msg):
        msg_obj = Message(msg)
        cmd = msg_obj.get_cmd()
        src = msg_obj.get_src()
        response = ""
        if cmd == "info":
            body = msg_obj.get_msg()
            method = body['method']
            params = body['params']
            if method == "addLineLog":
                infoLog = params["info"]  
                response = self.__file_manager.addLineLog(infoLog)
            elif method == "deleteLog":
                response = self.__file_manager.deleteLogFile()
            elif method == "readLogFile":
                response = self.__file_manager.readLogFile()
            elif method == "listLogs":
                response = self.__file_manager.listLogs()
            elif method == "createDir":
                nameDir = params['nameDir']
                response = self.__file_manager.createDir(nameDir)
            elif method == "deleteDir":
                nameDir = params['nameDir']
                response = self.__file_manager.deleteDir(nameDir)
            elif method == "addFileInDirectory":
                nameDir = params['nameDir']
                response = self.__file_manager.addFileInDirectory(nameDir)
            elif method == "addLineInFileDirectory":
                nameDir = params['nameDir']
                info = params['info']
                response = self.__file_manager.addLineInFileDirectory(nameDir, info)
            elif method == "listDirectoriesInDirectory":
                nameDir = params['nameDir']
                response = self.__file_manager.listDirectoriesInDirectory(nameDir)
            elif method == "setFileName":
                fileName = params['fileName']
                response = self.__file_manager.setFileName(fileName)
            elif method == "getFileName":
                response = self.__file_manager.getFileName()
            else:
                response = f"error: no such method {method}"
        elif cmd == "stop" and src == "KERNEL":
            response = "Closing due to KERNEL request. BYE"
        else:
            response = f"error: no such command {cmd} or access denied"
        response_msg = {
            "body": response
        }
        response_str = Message.format("send", "FILE_MAN", msg_obj.get_src(), response_msg)
        print("RES:  " + response)
        return response_str

if __name__ == "__main__":
    server = Server()
    server.start()