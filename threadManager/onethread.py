import threading
from workTask.pingTask import pingTask
from hostManager.hostmanager import hostmanager

mylock = threading.RLock()
num = 0


class onethread(threading.Thread):
    def __init__(self, name=str(num)):
        global num
        threading.Thread.__init__(self)
        self.name = name
        num += 1
        #self.hostlist =  hostlist

    @staticmethod
    def gethost():
        mylock.acquire()
        if not hostmanager.instance().cangethost():
            mylock.release()
            return None
        host = hostmanager.instance().gethost()
        mylock.release()
        return host

    @staticmethod
    def setresult(host, flag):
        hostmanager.instance().setresult(host, flag)

    def run(self):
        print "run thread {0}".format(self.name)
        while True:
            host = onethread.gethost()
            if host is None:
                return 0
            p = pingTask(host)
            p.dotask()
            if p.retcode == 0:
                onethread.setresult(host, True)
                print "thread {0} host {1} is over with {2}".format(self.name, host, True)
            else:
                onethread.setresult(host, False)
                print "thread {0} host {1} is over with {2}".format(self.name, host, False)
