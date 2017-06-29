import threading
import time
import random
FULL=5
full = threading.Semaphore(value=0)
empty = threading.Semaphore(value=5)
mutex=threading.Semaphore()

class Box:

    def __init__(self):
        self.rare=0
        self.head=0
        self.shared_content=[0,0,0,0,0]
    def put(self,i):
        #print(self.rare)
        self.shared_content[self.rare]=i
        self.rare=(self.rare+1)%FULL
        self.showcontent()
    def get(self):
        #print(self.shared_content[self.head])
        self.shared_content[self.head]=0
        self.head=(self.head+1)%FULL
        self.showcontent()
    def showcontent(self):
        print("show shared_content:")
        for i in self.shared_content:
            print(i)
        print("end")

def producer(box,num,limit):
    #print("enter producer:")
    cnt=0
    while (cnt<limit):
        
        empty.acquire()
        mutex.acquire()
        print("producer %d"%(num))
        box.put("mywork")
        mutex.release()
        #produce
        full.release()
        cnt+=1
        #time.sleep(random.random()*100)
        
def consumer(box,num,limit):
    #print("enter consumer")
    cnt=0
    while (cnt<limit):
        
        full.acquire()
        mutex.acquire()
        print("consumer %d:"%(num))
        box.get()
        mutex.release()
        #consume
        empty.release()
        cnt+=1
        #time.sleep(random.random()*100)


def main():
    box=Box()
    for i in range(10):
        t = threading.Thread(target = producer,args=(box,i,30))
        t.start()
    for i in range(10):
        t2 = threading.Thread(target = consumer,args=(box,i,30))
    #t.start()
        t2.start()

print(__name__)
if __name__ == '__main__':
    main()


