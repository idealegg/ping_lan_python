from hostManager.hostmanager import hostmanager
import Tkinter
from Tkconstants import *
import time


class DisplayMsg(Tkinter.Tk):
    def __init__(self):
        Tkinter.Tk.__init__(self)
        self.title("Get Lan Info")
        self.geometry('300x200')
        self.iconname("haha")
        self.frame = Tkinter.Frame(self, relief=RIDGE, borderwidth=2)
        self.frame.pack(fill=BOTH, expand=1)
        self.var = Tkinter.StringVar()
        self.listbox = Tkinter.Listbox(self.frame, height=5, selectmode=BROWSE, listvariable=self.var)
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
    dm = DisplayMsg()
    dm.run()
