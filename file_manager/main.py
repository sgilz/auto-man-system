import os

class FileManager:
    """
    Class to manage files of logs 
    """

    def __init__(self, file):
        self.file = file

    def create(self):
        open("%s/logs/%s" %(os.getcwd(), self.file), 'a').close()
    
    def delete(self):
        if os.path.exists("%s/logs/%s" %(os.getcwd(), self.file)):
            os.remove("%s/logs/%s" %(os.getcwd(), self.file))
        else:
            print("File does not exit")
    
    def addLine(self, info = ""):
        file = open("%s/logs/%s" %(os.getcwd(), self.file), 'a')
        file.write(info + "\n")
        file.close()
    
    def readLogFile(self):
        file = open("%s/logs/%s" %(os.getcwd(), self.file), 'r')
        lines = file.readlines()

        count = 0
        for line in lines:
            count += 1
            print("[{}]: {}".format(count, line.strip()))

    def listLogs(self):
        os.system("ls %s/logs/" %(os.getcwd()))

