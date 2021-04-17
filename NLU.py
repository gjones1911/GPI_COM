from sys import argv
from os import system
# open the file and get the thing

class PI_OPR:
    def __init__(self, ):
        # get this systems wlan/lan ip
        self.wlan = self.getWlanFromFile()

    def getWlanFromFile(self,substr='WPN' ):
        f = open("../NT/{}.txt".format(substr), "r")
        lines = f.readlines()
        wIP = lines[0].split("\n")[0].strip()
        return wIP

    def generateCmdStrOut(self, filelist, destIP, destUsr, packetFile):
        fstr = ""
        print(filelist)
        for f in filelist:
            fstr += f + " "
        cmdstr = "scp {} {}@{}:{}".format(fstr, destUsr, destIP, packetFile)
        return cmdstr

    def generateCmdStrIn(self, filelist, destIP, newfile, destUsr='pi',):
        fstr = ""
        for f in filelist:
            fstr += fstr + " "
        cmdstr = "scp {}@{}:{} {}".format(destUsr, destIP, fstr, newfile)
        return cmdstr
    
    # use scp to send some files to a destination
    def push_files(self, filelist, destIP, destUsr='pi'):
        cmd_str = self.generateCmdStr(filelist, destIP)
        system(cmd_str)
        return
    
    # use scp to send some files to a destination
    def pull_file(self, filed, sourceIP):
        cmd_str = self.generateCmdStr(filelist, sourceIP)
        system(cmd_str)
        return
cdd = ""
if len(argv) > 1:
    cdd = argv[1]

operator_pi = PI_OPR()
file_list = ['test.txt',]

destUsr = 'gjonesy'
destIp = operator_pi.getWlanFromFile(substr="NQ")
path = "~\gjonesy\python_worker\comms_link\GPI_COM" 
todo = operator_pi.generateCmdStrOut(file_list, destIp, destUsr, path )

print(todo)

