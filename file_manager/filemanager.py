import os

class FileManager:
    """
    Class to manage files of logs 
    """

    def __init__(self, file = ""):
        self.file = file

    def createLog(self):
        open("%s/logs/%s" %(os.getcwd(), self.file), 'a').close()
    
    def deleteLogFile(self):
        if os.path.exists("%s/logs/%s" %(os.getcwd(), self.file)):
            os.remove("%s/logs/%s" %(os.getcwd(), self.file))
        else:
            print("File does not exit")
    
    def addLineLog(self, info = ""):
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

    def createDir(self, nameDir):
        path = "{}/{}".format(os.getcwd(), nameDir)
        try:
            os.mkdir(path)
        except OSError:
            print ("Creation of the directory %s failed" % path)
        else:
            print ("Successfully created the directory %s " % path)

    def deleteDir(self, nameDir):
        path = "{}/{}".format(os.getcwd(), nameDir)
        try:
            os.rmdir(path)
        except OSError:
            print ("Delete of the directory %s failed" % path)
        else:
            print ("Successfully deleted the directory %s " % path)

    def addFileInDirectory(self, nameDir):
        open("%s/%s/%s" %(os.getcwd(), nameDir,self.file), 'a').close()
    
    def addLineInFileDirectory(self, nameDir, info = ""):
        file = open("%s/%s/%s" %(os.getcwd(), nameDir,self.file), 'a')
        file.write(info + "\n")
        file.close()
    
    def listDirectoriesInDirectory(self, nameDir):
        os.system("ls %s/%s/" %(os.getcwd(), nameDir))

    def setFileName(self, fileName):
        self.file = fileName
    
    def getFileName(self):
        return self.file