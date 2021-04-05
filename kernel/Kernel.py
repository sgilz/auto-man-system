from datetime import datetime
from utils.Message import Message
import json

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
        meta = f"Log: {date} -> "
        msg = {
            "method": "addLineLog",
            "params":{
                "meta": meta,
                "info": json.loads(str(msg_obj))
            },
        }
        return Message.format("info", msg_obj.get_src(), "FILE_MAN", msg).replace("\\", "")

