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

    def removehost(self, host):
        self.hostlist.remove(host)

    def cangethost(self):
        return len(self.hostlist) != 0

    def gethost(self):
        return self.hostlist.pop(0)

    def setresult(self, host, flag):
        self.resultmap[host] = flag

    def printf(self):
        #print "hostlist: %s %s %s" % (" ".join(self.hostlist), self.__class__, self.__module__)
        #print "resultlist: %s%" % " ".join(self.resultmap.keys())
        print "hostlist:"
        pprint.pprint(self.hostlist)
        print "resultlist:"
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

