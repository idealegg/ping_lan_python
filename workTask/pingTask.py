import sys
import shlex, subprocess
import chardet


class pingTask:
    def __init__(self, host):
        self.host = host
        self.cmd = ""
        self.output = ""
        self.outerr = ""
        self.retcode = 0

    def dotask(self):
        self.cmd = 'ping'
        if sys.platform == "win32":
            self.cmd += ' -n 3 '
        else:
            self.cmd += ' -c 3 '
        self.cmd += self.host
        # os.popen(self.cmd, 'r', self.result)
        print "default coding type: {0}".format(sys.getdefaultencoding())
        reload(sys)
        sys.setdefaultencoding('utf-8')
        args = shlex.split(self.cmd)
        p = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        (tmpoutput, tmpouterr) = p.communicate()
        self.retcode = p.returncode
        self.output = "".join(tmpoutput)
        self.outerr = "".join(tmpouterr)
        print "return code: %d" % self.retcode
        print "stdout:"
        if self.output:
            if not isinstance(self.output, unicode):
                self.output = self.output.decode(chardet.detect(self.output)['encoding'])
            print self.output
        print "stderr:"
        if self.outerr:
            if not isinstance(self.outerr, unicode):
                self.outerr = self.outerr.decode(chardet.detect(self.outerr)['encoding'])
            print self.outerr
        '''
        infos = subprocess.Popen(args, stdout=subprocess.PIPE, shell=False).stdout.readlines()

        unicode_text = ''.join(infos)
        print chardet.detect(unicode_text)
        #print unicode_text.decode('gbk')
        '''

if __name__ == '__main__':
    p = pingTask('192.168.118.200')
    p.dotask()

