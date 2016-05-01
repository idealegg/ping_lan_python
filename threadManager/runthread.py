from threadManager.onethread import onethread
from hostManager.hostmanager import hostmanager
import pprint


class runthread:
    def __init__(self, num=10):
        self.num = num
        self.hostlist = []
        self.threadlist = []

    def dorun(self):
        #hostmanager.instance().addhostlist(self.hostlist)
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
        return 0

    def stop(self):
        for i in range(self.num):
            self.threadlist[i].stop()

if __name__ == '__main__':
    hostmanager.instance().genhostlist(network='192.168.118', max=10, min=2)
    rt = runthread(2)
    rt.dorun()
