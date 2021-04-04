import os

class FileManager:
    """
    Class to manage files of logs 
    """

    def __init__(self, file = "", root = ""):
        self.file = file
        self.root = os.path.dirname(os.path.realpath(__file__))

    def createLog(self):
        open("%s/logs/%s" %(self.root, self.file), 'a').close()
        return "Log created"
    
    def deleteLogFile(self):
        if os.path.exists("%s/logs/%s" %(self.root, self.file)):
            os.remove("%s/logs/%s" %(self.root, self.file))
            return "Log deleted"
        else:
            return "File does not exit"
    
    def addLineLog(self, info = ""):
        file = open("%s/logs/%s" %(self.root, self.file), 'a')
        file.write(info + "\n")
        file.close()
        return "Line log added"
    
    def readLogFile(self):
        file = open("%s/logs/%s" %(self.root, self.file), 'r')
        lines = file.readlines()

        count = 0
        lines = lines[-10:] if len(lines) > 10 else lines
        for line in lines:
            count += 1
            print("[{}]: {}".format(count, line.strip()))
        
        return "Logs readed"

    def listLogs(self):
        os.system("ls %s/logs/" %(self.root))
        return "Logs listed"

    def createDir(self, nameDir):
        path = "{}/{}".format(self.root, nameDir)
        try:
            os.mkdir(path)
        except OSError:
            return ("Creation of the directory %s failed" % path)
        else:
            return ("Successfully created the directory %s " % path)

    def deleteDir(self, nameDir):
        path = "{}/{}".format(self.root, nameDir)
        try:
            os.rmdir(path)
        except OSError:
            return ("Delete of the directory %s failed" % path)
        else:
            return ("Successfully deleted the directory %s " % path)

    def addFileInDirectory(self, nameDir):
        open("%s/%s/%s" %(self.root, nameDir,self.file), 'a').close()
        return "File in drectory added"
    
    def addLineInFileDirectory(self, nameDir, info = ""):
        file = open("%s/%s/%s" %(self.root, nameDir,self.file), 'a')
        file.write(info + "\n")
        file.close()
        return "Line in file in directory added"
    
    def listDirectoriesInDirectory(self, nameDir):
        os.system("ls %s/%s/" %(self.root, nameDir))
        return "Directories in directory listed"

    def setFileName(self, fileName):
        self.file = fileName
        return "File name setted"
    
    def getFileName(self):
        return self.file