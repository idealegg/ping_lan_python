from threadManager.runthread import runthread
from displayMsg.DisplayMsg import DisplayMsg
import threading

dmstop = 0
rhstop = 0


class dmThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.dm = DisplayMsg()

    def run(self):
        global dmstop
        self.dm.run()
        dmstop = 1


class rhThread(threading.Thread):
    def __init__(self, tnum=2, hnum=10, network='192.168.118'):
        threading.Thread.__init__(self)
        self.rh = runthread(tnum)
        #self.tnum = tnum
        self.hnum = hnum
        self.network = network

    def run(self):
        global rhstop
        self.rh.dorun(max=self.hnum, network=self.network)
        rhstop = 1


class main:
    def __init__(self, tnum, hnum):
        self.dm = dmThread()
        self.rh = rhThread(tnum, hnum)

    def run(self):
        self.rh.start()
        self.dm.start()
        while True:
            if dmstop and rhstop:
                return 0
            if dmstop:
                self.dm.join()
                if not rhstop:
                    self.rh.rh.stop()
            if rhstop:
                self.rh.join()


if __name__ == '__main__':
    m = main(2, 10)
    m.run()





