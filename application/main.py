import json
import socket
import sys
from application.AppHandler import AppHandler
from utils.Message import Message

class Server:
    """
    This class will represent a Server entity which allows access from remote kernel via
    sockets.
    """
    def __init__(self, address = None, port = 6543):
        #main handler for control operations
        self.__app_handler = AppHandler()
        self.__app_handler.run() # run the initial subprocesses

        #socket service comands
        self.__BUFFER_SIZE = 1024
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
                self.__socket.close()
                sys.exit()
            except:
                print(f"# Disconnected due interrupted connection. :(")
                self.__socket.close()
                sys.exit(1)

    def __session(self, client, address):
        print(f"# Connected: {address}")
        while True:
            bin_msg = client.recv(self.__BUFFER_SIZE)
            if bin_msg:
                msg = msg.decode('UTF-8').replace('\n','') # convert to string (Python 3 only)
                print(f"< {address}: {msg}")
                response = self.__execute(msg)
                client.send(response.encode())
            else:
                print(f"# Disconnected: {address}")
                break
        client.close()

    def __execute(self, msg):
        msg_obj = Message(msg)
        cmd = msg_obj.get_cmd()
        response = ""
        if cmd == "info":
            body = json.loads(msg_obj.get_msg())
            method = body["method"]
            params = body["params"]
            if method == "stat":
                response = self.__app_handler.get_processes_info()
            elif method == "prior":
                pid = params["pid"]
                priority_id =  params["priority_id"]
                response = self.__app_handler.set_priority(priority_id, pid)
            elif method == "term":
                pid = params["pid"]
                response = self.__app_handler.terminate(pid)
            else:
                response = f"error: no such method {method}"
        elif cmd == "stop":
            try:
                self.__app_handler.terminate_all()
                return "BYE"
            finally:
                sys.exit(0)
        response_str = Message.format("send", "APP", msg_obj.get_src(), response)
        return response_str

if __name__ == "__main__":
    server = Server()
    server.start()