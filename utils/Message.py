import json

class Message:
    """
    A simple class for parsing messages with this format:
    {
        'cmd': 
            'info' (request) |
            'send' (answer)  |
            'stop' (spot system)
        'src': 
            'GUI' |
            'KERNEL', |
            'FILE_MAN' |
            'APP'
        'dst': 
            'GUI' |
            'KERNEL', |
            'FILE_MAN' |
            'APP'
        'msg': {
            'body': str
            'method': str
            'params': 
        }
    }

    example:
    {
        'cmd': 'info',
        'src': 'GUI',
        'dst': 'APP',
        'msg': {
            'body': ”Log:13/11/2020-08:00->Error en App1”
            'method': 'prior'
            'params': {
                'pid': 123
                'priority_id': -10
            }

        }

    }
    """
    def __init__(self, msg_string):
        self.__msg_string = msg_string
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

    def __str__(self):
        return self.__msg_string
    
    @staticmethod
    def format(cmd, src, dst, msg):
        """
        Sets a message to have a unified format for the entire system.
        """
        mgs_dict = {
            "cmd": cmd,
            "src": src,
            "dst": dst,
            "msg": msg
        }
        return json.dumps(mgs_dict).replace("\\\\","\\")

    