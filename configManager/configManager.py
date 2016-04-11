import os
import ConfigParser
import pprint


class configManager:
    def __init__(self):
        self.configmap = {}
        self.configdir = ""
        self.configparser = ConfigParser.ConfigParser()
        self.initconfig()

    def initconfig(self):
        self.configdir = os.path.join(os.path.dirname(os.getcwd()), 'config')
        if os.path.isdir(self.configdir):
            print "{} is a dir".format(self.configdir)
            for conffile in os.listdir(self.configdir):
                print conffile
                (mapkey, _) = os.path.splitext(conffile)
                conffile = os.path.join(self.configdir, conffile)
                if os.path.isfile(conffile):
                    print "{} is a file".format(conffile)
                    self.configparser.read(conffile)
                    self.configmap[mapkey] = dict(self.configparser.items(mapkey))

    def getconfig(self, itemtype):
        if itemtype in self.configmap:
            return self.configmap[itemtype]
        return {}

    def printf(self):
        pprint.pprint(self.configmap)

    @classmethod
    def instance(cls):
        # print "call instance"
        if not hasattr(cls, '__instance__'):
            cls.__instance__ = configManager()
        return cls.__instance__

if __name__ == '__main__':
    configManager.printf()
