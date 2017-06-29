class content:
    def __init__(self,Name,RequestTime,Priority,Status):
        self.name=Name
        self.requestTime=RequestTime
        self.priority=Priority
        self.status=Status
class myThread:
    def __init__(self,Name,RequestTime,Priority,Status):
        self.mycontent=content(Name,RequestTime,Priority,Status)

    def setnext(self,Next):
        self.next=Next



def init():
    
    #simulate(threadpool[0])
    return 0
def status_printer():
    print("use printer")
    for i in threadpool:
        print("%s: req time:%d pri:%d status:%s" % (i.mycontent.name,i.mycontent.requestTime,i.mycontent.priority,i.mycontent.status))

def insert(head,myT):
    if (head.mycontent.name=="Empty"):
        head.mycontent=myT.mycontent
        head.next=myThread("Empty",1,-100,1)
        return 0
    while (head.next.mycontent.name!="Empty" ):
        if (head.next.mycontent.priority>=myT.mycontent.priority):
            head=head.next
        else:
            break
    myT.next=head.next
    head.next=myT
        
def simulate(head):

    while(head.mycontent.name!="Empty"):
        
        proc=head
        head=head.next
        proc.mycontent.requestTime-=1
        proc.mycontent.priority-=1
        if(proc.mycontent.requestTime>0):
            proc.mycontent.status="working"
            insert(head,proc)
        else:
            proc.mycontent.status="finish"
        status_printer()
        for i in threadpool:
            if (i.mycontent.status!="finish"):
                i.mycontent.status="ready"
        print(head.mycontent.name)


init()

threadpool=[myThread("P2",3,5,"ready"),myThread("P4",2,4,"ready"),myThread("P3",1,3,"ready"),myThread("P5",4,2,"ready"),myThread("P1",2,1,"ready")]
threadpool[0].setnext(threadpool[1])
threadpool[1].setnext(threadpool[2])
threadpool[2].setnext(threadpool[3])
threadpool[3].setnext(threadpool[4])
threadpool[4].setnext(myThread("Empty",1,-100,1))
print(threadpool[3].next)
status_printer()
simulate(threadpool[0])
        