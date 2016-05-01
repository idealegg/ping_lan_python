from threadManager.onethread import onethread
from hostManager.hostmanager import hostmanager
import pprint


class runthread:
    def __init__(self, num=10):
        self.num = num
        self.hostlist = []
        self.threadlist = []

    def genhostlist(self, network='192.168.118', max=256):
        self.hostlist=[]
        for i in range(max):
            self.hostlist.append(network+'.'+str(i))
        #print "runthread genhostlist:"
        #pprint.pprint(self.hostlist)

    def dorun(self, network='192.168.118', max=256):
        self.genhostlist(network, max)
        hostmanager.instance().addhostlist(self.hostlist)
        hostmanager.instance().printf()
        for i in range(self.num):
            print "adding a thread %d" % i
            self.threadlist.append(onethread())
            print "added a thread %d" % i
        for i in range(self.num):
            print "starting a thread %d" % i
            self.threadlist[i].start()
            print "started a thread %d" % i
        for i in range(self.num):
            print "joining a thread %d" % i
            self.threadlist[i].join()
            print "joined a thread %d" % i
        hostmanager.instance().printf()

if __name__ == '__main__':
    rt = runthread(2)
    rt.dorun(max=10)
