from datetime import datetime
from utils.Message import Message

class Kernel:
    """
    A class for managing:
        - transaction logs 
        - message retransmission
        - stage management
    """
    def generate_log(self, msg_obj:Message):
        """
        Generates logs based on incoming messages.
        """
        date = str(datetime.now())
        cmd = msg_obj.get_cmd()
        src = msg_obj.get_src()
        dst = msg_obj.get_dst()
        info = f"Log: {date} -> cmd:{cmd}, src:{src}, dst: {dst}"
        msg = {
            "method": "addLineLog",
            "params":{
                "info": info
            },
        }
        return Message.format("info", msg_obj.get_src(), "FILE_MAN", msg).replace("\\", "")

