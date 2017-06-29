import random
class Dir:
    def __init__(self,name):
        self.dict={'..':None,'a':File("a",1,1,1)}
        self.name=name
    def lists(self):
        for i in self.dict:
            print(i)
    def get(self,name):
        return self.dict[name]
    def remove(self,name):
        del self.dict[name]
    def put(self,cont):
        self.dict[cont.name]=cont
        self.lists()

class File:
    def __init__(self,name,description,filepointer,privilege):
        self.name=name
        self.description=description
        self.privilege=privilege
        self.filepointer=1
    def readable(self,user):
        return True
class AFD:
    def __init__(self,name,privilege,pointer):
        self.name=name
        self.privilege=privilege
        self.edited=False
        self.pointer=pointer
        self.pointers=[]
        self.lastindex=-1
    def read(self,index,byte):
        print(index)
        print(self.pointers[index])
        self.pointers[index]=self.pointers[index]+byte
        print(self.pointers[index])
    def write(self,byte,index):
        self.edited=True
        self.pointers[index]=self.pointers[index]+byte
    def newaccess(self):
        self.lastindex+=1
        self.pointers.append(self.pointer)
        return self.lastindex
class UED:
    def __init__(self,username):
        self.content=Dir("root")
        self.username=username
        self.currentcont=self.content
        self.runningfile={}
    def lists(self):
        self.content.lists()
    def open(self,name):
        cont=self.currentcont.get(name)
        if (self.runningfile.get(cont.name) is not None):
            self.printrunningtask()
        if (isinstance(cont,File) and cont.readable(self)):
            self.runningfile[cont.name]=AFD(cont.name,cont.privilege,cont.filepointer)
        myAFD=self.runningfile[cont.name]
        self.printrunningtask()

        print(self.runningfile[cont.name].pointer)
        return [myAFD,myAFD.newaccess()]
    def createFile(self,name):
        self.currentcont.put(File(name,"desc",random.random(),1))
    def delFile(self,name):
        if (self.runningfile.get(name) is not None):
            print("close file first") 
        else:
            self.currentcont.remove(name)
    def close(self,name):
        del self.runningfile[name]
        self.printrunningtask()
    def printrunningtask(self):
        print([i for i in self.runningfile])
    def read(self,name,index,byte):
        self.runningfile[name].read(index,byte)
    

    
    
class MFD:
    def __init__(self):
        self.users={}
        self.currentenv=None
        
    def addusr(self,userenv):
        if(self.users.get(userenv.username) is not None):
            print("User is existed")
            return 
        self.users[userenv.username]=userenv
    def login(self,username):
        userenv=self.users[username]
        print(self.users)
        print(userenv)
        if(userenv is not None):
            self.currentenv=userenv
            print("login success")
        else:
            print("fail")
def cmdexecuter(myMFD,cmd):
    cmd=cmd.split(" ")
    if(cmd[0]=="login"):
        print("execute login")
        myMFD.login(cmd[1])
    if(cmd[0]=="list"):
        myMFD.currentenv.lists()
    if(cmd[0]=="create"):
        myMFD.currentenv.createFile(cmd[1])
    if(cmd[0]=="open"):
        myMFD.read=myMFD.currentenv.open(cmd[1])
    if(cmd[0]=="close"):
        myMFD.currentenv.close(cmd[1])
    if(cmd[0]=="del"):
        myMFD.currentenv.delFile(cmd[1])
    if(cmd[0]=="read"):
        myMFD.currentenv.read(myMFD.read[0].name,myMFD.read[1],int(cmd[1]))


def init():
    myMFD=MFD()
    myMFD.addusr(UED("martin"))
    myMFD.addusr(UED("root"))
    #currentUED=None

    while (True):
        cmd=raw_input("Enter your command\n")
        print(cmd)
        cmdexecuter(myMFD,cmd)  
        print(myMFD.currentenv)     


if (__name__=='__main__'):
    init()