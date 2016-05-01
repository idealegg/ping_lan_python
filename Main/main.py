from threadManager.runthread import runthread
from displayMsg.DisplayMsg import DisplayMsg
from hostManager.hostmanager import hostmanager
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
    def __init__(self, tnum=2):
        threading.Thread.__init__(self)
        self.rh = runthread(tnum)
        #self.tnum = tnum

    def run(self):
        global rhstop
        self.rh.dorun()
        rhstop = 1


class main:
    def __init__(self, tnum=2):
        self.dm = dmThread()
        self.rh = rhThread(tnum)

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
    hostmanager.instance().genhostlist(network='192.168.1', max=120, min=100)
    m = main(5)
    m.run()





