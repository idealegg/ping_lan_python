from hostManager.hostmanager import hostmanager
from configManager.configManager import configManager
import Tkinter
import tkFont
from Tkconstants import *
import time


class DisplayMsg(Tkinter.Tk):
    def __init__(self):
        Tkinter.Tk.__init__(self)
        self.title("Get Lan Info")
        self.geometry('300x200')
        self.iconname("haha")
        self.frame = Tkinter.Frame(self, cnf=configManager.instance().getconfig('Frame'), relief=RIDGE, borderwidth=2)
        self.frame.pack(fill=BOTH, expand=1)
        self.var = Tkinter.StringVar()
        self.font = tkFont.Font(family="Times", size=10, weight=tkFont.BOLD)
        self.listbox = Tkinter.Listbox(self.frame, cnf=configManager.instance().getconfig('Listbox'), height=5,
                                       selectmode=BROWSE, listvariable=self.var, font=self.font, bg='#646464',
                                       fg='#c8c8c8')
        self.list_item = tuple(hostmanager.instance().getresult())
        self.var.set(self.list_item)
        self.scrl = Tkinter.Scrollbar(self.frame)
        self.scrl.pack(side=RIGHT, fill=Y)
        self.listbox.configure(yscrollcommand=self.scrl.set)
        self.listbox.pack(side=LEFT, fill=BOTH)
        self.scrl['command'] = self.listbox.yview
        self.button2 = Tkinter.Button(self.frame, text="Exit", command=self.exit)
        self.button2.pack(side=BOTTOM)
        self.done = 0
        self.starttime = time.time()
        #'''
        for key in self.listbox.keys():
            value = self.listbox.cget(key)
            if type(value) is not None:
                print "{0}: {1}".format(key, self.listbox.cget(key))
            else:
                print key
        #'''

    def exit(self):
        self.done = 1
        self.destroy()

    def run(self):
        #num = 0
        while not self.done:
            time.sleep(1)
            #num += 1
            #runtime = time.time() - self.starttime
            #tmplist = list(self.list_item)
            #for i in range(len(tmplist)):
                #tmplist[i] += runtime

            #tmplist.insert(0, num)
            self.list_item = tuple(hostmanager.instance().getresult())
            self.var.set(self.list_item)
            self.update()


if __name__ == "__main__":
    hostmanager.instance().genhostlist(network='192.168.118', max=106, min=105)
    dm = DisplayMsg()
    dm.run()
