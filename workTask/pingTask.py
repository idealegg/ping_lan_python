# -*- coding:utf-8 -*-
import sys
import shlex, subprocess


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
        args = shlex.split(self.cmd)
        p = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        (self.output, self.outerr) = p.communicate()
        self.retcode = p.returncode
        print "return code: %d" % self.retcode
        print "stdout:\n%s" % self.output
        print "stderr:\n%s" % self.outerr

if __name__ == '__main__':
    p = pingTask('192.168.118.100')
    p.dotask()

