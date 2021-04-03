import os
import sys
from kernel.Server import Server

class Kernel:
    """
    Class which manages initialization, communication and completion stages.
    """
    def __init__(self):
        self.server = Server()
        self.server.start()

if __name__ == "__main__":
    kernel = Kernel()
