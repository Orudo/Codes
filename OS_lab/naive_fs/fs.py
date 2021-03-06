import random
class Dir:
    def __init__(self,name):
        self.dict={'..':None,'a':File("a",1,1,1,30)}
        self.name=name
    def lists(self):
        for k,v in self.dict.items():
            if (v is not None):
                print("%s %d"%(k,v.filepointer))
            #print(k)
            #print(v)
    def get(self,name):
        return self.dict[name]
    def remove(self,name):
        del self.dict[name]
    def put(self,cont):
        print("putting")
        self.dict[cont.name]=cont
        self.lists()

class File:
    def __init__(self,name,description,filepointer,privilege,length):
        self.name=name
        self.description=description
        self.privilege={}
        self.filepointer=filepointer
        self.length=length
    def addUserToAccess(self,User):
        self.privilege[User.username]=1
    def readable(self,user):
        return self.privilege.get(user.username) is not None

class AFD:
    def __init__(self,cont):
        self.edited=False
        self.cont=cont
        self.pointers=[]
        self.lastindex=-1
    def read(self,index,byte):
        print(index)
        print(self.pointers[index])
        if (self.pointers[index]+byte-self.cont.filepointer<self.cont.length):
            self.pointers[index]=self.pointers[index]+byte
        else:
            raise ValueError
        print(self.pointers[index])
    def write(self,index,byte):
        print(index)
        #print(self.edited)
        self.edited=True
        self.pointers[index]=self.pointers[index]+byte
    def newaccess(self):
        self.lastindex+=1
        self.pointers.append(self.cont.filepointer)
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
            myAFD=self.runningfile[cont.name]
            self.printrunningtask()
            return [myAFD,myAFD.newaccess()]
        if (isinstance(cont,File) and cont.readable(self)):
            self.runningfile[cont.name]=AFD(cont)
            myAFD=self.runningfile[cont.name]
            self.printrunningtask()
            return [myAFD,myAFD.newaccess()]
        else:
            print("Unable to Access")
        
    def createFile(self,name,addr,length):
        file=File(name,"desc",int(addr),1,length)
        file.addUserToAccess(self)
        self.currentcont.put(file)
    def delFile(self,name):
        if (self.runningfile.get(name) is not None):
            print("close file first") 
        else:
            self.currentcont.remove(name)
    def close(self,name):
        print(self.runningfile[name].edited)
        if (self.runningfile[name].edited):
            cont=self.content.get(name)
            cont.filepointer=self.runningfile[name].pointers[0]
            self.content.put(cont)
        del self.runningfile[name]
        self.printrunningtask()
    def printrunningtask(self):
        print([i for i in self.runningfile])
    def read(self,name,index,byte):
        self.runningfile[name].read(index,byte)
    def write(self,name,index,byte):
        print("writting step 1")
        self.runningfile[name].write(index,byte)
    

    
    
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
        myMFD.currentenv.createFile(cmd[1],int(cmd[2]),int(cmd[3]))
    if(cmd[0]=="open"):
        myMFD.read=myMFD.currentenv.open(cmd[1])
    if(cmd[0]=="close"):
        myMFD.currentenv.close(cmd[1])
    if(cmd[0]=="del"):
        myMFD.currentenv.delFile(cmd[1])
    if(cmd[0]=="read"):
        myMFD.currentenv.read(myMFD.read[0].cont.name,myMFD.read[1],int(cmd[1]))
    if(cmd[0]=="write"):
        myMFD.currentenv.write(myMFD.read[0].cont.name,myMFD.read[1],int(cmd[1]))


def init():
    myMFD=MFD()
    myMFD.addusr(UED("martin"))
    myMFD.addusr(UED("root"))
    #currentUED=None

    while (True):
        cmd=input("Enter your command\n")
        print(cmd)
        cmdexecuter(myMFD,cmd)  
        print(myMFD.currentenv)     


if (__name__=='__main__'):
    init()