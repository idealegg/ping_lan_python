from hostManager.hostmanager import hostmanager
import Tkinter
from Tkconstants import *
import time


class DisplayMsg(Tkinter.Tk):
    def __init__(self):
        Tkinter.Tk.__init__(self)
        self.frame = Tkinter.Frame(self, relief=RIDGE, borderwidth=2)
        self.frame.pack(fill=BOTH, expand=1)
        self.var = Tkinter.StringVar()
        self.entry = Tkinter.Entry(self.frame, textvariable=self.var)
        self.var.set("hello world")
        self.entry.pack()
        #self.text = Tkinter.Text(self.frame)
        #self.text.insert(END, "hello world\n")
        #self.text.pack(fill=X, expand=1)
        #self.button1 = Tkinter.Button(self.frame, text="Run", command=self.runframe)
        #self.button1.pack(side=TOP)
        self.button2 = Tkinter.Button(self.frame, text="Exit", command=self.destroy)
        self.button2.pack(side=BOTTOM)
        #self.after_idle(self.runframe)

    def run(self):
        while True:
            time.sleep(1)
            datetime = time.time()
            #var = Tkinter.StringVar()
            self.var.set(str(datetime))
            #self.text.delete(1.0)
            #self.text.insert(END, str(datetime)+"\n")
            #self.label.setvar(name='text', value="1234")
            #self.frame.after()
            #self.text.pack(fill=X, expand=1)
            #self.text.update()
            #self.frame.update()
            self.update()


if __name__ == "__main__":
    dm = DisplayMsg()
    dm.run()
