import datetime
import Queue
class pagingstruct:
    '''def __gt__(self,other):
        return self.lastaccess>other.lastaccess'''
    def __lt__(self,other):
        '''print("pagenum:%d"%(self.pagingnum))
        print(str(self.lastaccess))
        print("pagenum:%d"%(other.pagingnum))
        print(str(other.lastaccess))'''
        print(self.lastaccess<other.lastaccess)
        return self.lastaccess<other.lastaccess
    def __init__(self,pagingnum,blocknum,location):
        self.pagingnum=pagingnum
        self.blocknum=blocknum
        self.valid=False
        self.location=location
        self.lastaccess=datetime.datetime(2009, 12, 2, 10, 24, 34)
        self.edited=False
    def getcontent(self,offset):
        if self.valid==True:
            print("successfully get content")
        else:
            print("*%d"%(self.pagingnum))
            self.valid=True
        self.lastaccess=datetime.datetime.now()
class priq:
    def __init__(self,capacity):
        self.queue=[]
        self.capacity=capacity
        self.currentsize=0
    def pop(self):
        if (self.currentsize>0):
            self.currentsize-=1
            #print([i.pagingnum for i in self.queue])
            page=Queue.heapq.heappop(self.queue)
           # print([i.pagingnum for i in self.queue])
                 
            #print(page.pagingnum)
            return Queue.heapq.heappop(self.queue)
        else:
            raise ValueError ("unexpected value")
    def push(self,page):
        if (self.currentsize<self.capacity):
            Queue.heapq.heappush(self.queue,page)
            self.currentsize+=1
        else:
            raise ValueError("unexpected value--push")
    def full(self):
        return (self.currentsize>=self.capacity)
class pagemanager:
    def __init__(self,capacity):
        self.dict={}
        self.queue=priq(capacity)

    def add(self,pagingstruct):
        self.dict[str(pagingstruct.pagingnum)]=pagingstruct
    def access(self,pagenum):
        page=self.dict[str(pagenum)]
        if (page.valid):
            print("in page")
            return page
        page=None

        if (self.queue.full()):
            print("page full:")
            page=self.queue.pop()
            print("pop page%d"%(page.pagingnum))
            if(page.edited): 
                print("write back")
                page.edited=False
            page.valid=0
        print("page interrupt:%d"%(pagenum))
        page=self.dict[str(pagenum)]
        page.valid=1
        page.lastaccess=datetime.datetime.now()
        self.queue.push(page)
        return page
    def edit(self,pagenum):
        page=self.access(pagenum)
        page.edited=True

def get(address):
    pagenum=address>>7
    page=manager.access(pagenum)
    page.getcontent(address&127)
def addressgen(pagenum,offset):
    return pagenum*128+offset
manager=pagemanager(4)
def init():
    
    manager.add(pagingstruct(0,5,int('011')))
    manager.add(pagingstruct(1,8,int('012')))
    manager.add(pagingstruct(2,9,int('013')))
    manager.add(pagingstruct(3,1,int('021')))
    manager.add(pagingstruct(4,None,int('022')))
    manager.add(pagingstruct(5,None,int('023')))
    manager.add(pagingstruct(6,None,int('121')))
    print("all pages has been added")
    get(addressgen(0,36))
    get(addressgen(5,30))
    manager.edit(5)
    manager.edit(0)
    get(addressgen(2,21))
    get(addressgen(1,21))
    get(addressgen(4,21))
    get(addressgen(6,21))

    #get(addressgen(8,35))



if (__name__=='__main__'):
    init()
    
