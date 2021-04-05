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
        msg_str = str(msg_obj)
        info = f"Log: {date} -> {msg_str}"
        msg = {
            "method": "addLineLog",
            "params":{
                "info": info
            },
        }
        print("BUENAS" + msg_str)
        print("TARDES" + info)
        return Message.format("info", msg_obj.get_src(), "FILE_MAN", msg)

