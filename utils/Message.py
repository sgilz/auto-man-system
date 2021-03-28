import json

class Message:
    """
    A simple class for parsing messages with this format:
    {
        cmd:send, 
        src:GUI, 
        dst:GestorArc, 
        msg:”Log:13/11/2020-08:00->Error en App1”
    }
    """
    def __init__(self, msg_string):
        msg_dict = json.loads(msg_string)
        self.__cmd = msg_dict["cmd"]
        self.__src = msg_dict["src"]
        self.__dst = msg_dict["dst"]
        self.__msg = msg_dict["msg"]

    def get_cmd(self):
        return self.__cmd

    def get_src(self):
        return self.__src

    def get_dst(self):
        return self.__dst

    def get_msg(self):
        return self.__msg

    def set_cmd(self, cmd):
        self.__cmd = cmd

    def set_src(self, src):
        self.__src = src

    def set_dst(self, dst):
        self.__dst = dst

    def set_msg(self, msg):
        self.__msg = msg

    