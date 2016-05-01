import pprint


class hostmanager:
    def __init__(self, hostlist=[]):
        self.hostlist = hostlist
        self.resultmap = {}

    def addhost(self, host):
        self.hostlist.append(host)

    def addhostlist(self, hostlis):
        #print "start addhostlist ##################"
        #pprint.pprint(hostlis)
        #pprint.pprint(hostmanager.__instance__.hostlist)
        self.hostlist.extend(hostlis)
        #pprint.pprint(hostmanager.__instance__.hostlist)
        #print "end addhostlist ##################"

    def genhostlist(self, network='192.168.118', max=255, min=2):
        self.hostlist=[]
        for i in range(min, max):
            self.hostlist.append("".join((network, '.', str(i))))

    def removehost(self, host):
        self.hostlist.remove(host)

    def cangethost(self):
        return len(self.hostlist) != 0

    def gethost(self):
        return self.hostlist.pop(0)

    def setresult(self, host, flag):
        self.resultmap[host] = flag

    def getresult(self):
        tmplist = []
        keylist = self.resultmap.keys()
        keylist.sort()
        for key in keylist:
            tmplist.append("%-16s%-5s" % (key, self.resultmap[key]))
        return tmplist

    def printf(self):
        pprint.pprint(self.hostlist)
        pprint.pprint(self.resultmap)

    @classmethod
    def instance(cls):
        #print "call instance"
        if not hasattr(cls, '__instance__'):
            cls.__instance__ = hostmanager()
        #cls.__instance__.addhostlist(hostlis)
        #print "after addhostlist"
        #pprint.pprint(cls.__instance__.hostlist)
        return cls.__instance__

if __name__ == '__main__':
    h1 = hostmanager.instance()
    h2 = hostmanager.instance(['192.168.118.10'])

    h1.printf()
    h2.printf()

    h1.addhost('192.168.118.20')
    h2.removehost('192.168.118.10')

    h1.printf()
    h2.printf()

    host = h1.gethost()
    h1.setresult('192.168.118.10', True)
    h2.addhostlist(['192.168.118.30', '192.168.118.40'])

    h1.printf()
    h2.printf()

    print id(h1)
    print id(h2)

