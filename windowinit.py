from tkinter import *
from tkinter import ttk , messagebox
from tkinter import font
from tkinter.font import BOLD, Font
from windowinit import *
from student_fee import *
from admission import *
import admission

class Demo0(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.menubar = Menu(self)
        style = ttk.Style()
        style.configure("TButton", font =('calibri', 12, 'bold', 'underline'),foreground = 'Orange')
        self.filemenu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="File", menu=self.filemenu)
        self.filemenu.add_command(label="New", command=self.donothing)
        self.filemenu.add_command(label="Open", command=self.donothing)
        self.filemenu.add_command(label="Save", command=self.donothing)
        self.filemenu.add_command(label="Save as...", command=self.donothing)
        self.filemenu.add_command(label="Close", command=self.donothing)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit", command=self.quit)
        self.editmenu = Menu(self.menubar, tearoff=0)
        self.editmenu.add_command(label="Undo", command=self.donothing)
        self.editmenu.add_separator()
        self.menubar.add_cascade(label="Edit", menu=self.editmenu)
        self.editmenu.add_command(label="Cut", command=self.donothing)
        self.editmenu.add_command(label="Copy", command=self.donothing)
        self.editmenu.add_command(label="Paste", command=self.donothing)
        self.editmenu.add_command(label="Delete", command=self.donothing)
        self.editmenu.add_command(label="Select All", command=self.donothing)
        self.helpmenu = Menu(self.menubar, tearoff=0)
        self.helpmenu.add_command(label="Help Index", command=self.donothing)
        self.helpmenu.add_command(label="About...", command=self.donothing)
        self.menubar.add_cascade(label="Help", menu=self.helpmenu)
        self.config(menu=self.menubar)
        self._frame = None
        self.switch_frame(Demo3)
    
    def switch_frame(self,frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack_propagate(0)
        self._frame.pack(fill=BOTH)
    
    def donothing(self):
        self.filewin = Toplevel(self.master,bg="Blue")
        self.filewin.geometry("500x500")
        self.button = Button(self.filewin, text="Do nothing button")
        self.button.pack()