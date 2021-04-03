import os
from time import sleep
with open("app1_file.log", 'w') as f:
    lines = f"""
    Hi,
    this is a block of lines writen by app1
    in process  {os.getpid()}
    """
    f.write(lines)
while True:
    sleep(1)
