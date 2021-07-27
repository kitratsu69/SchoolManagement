from tkinter import *
from tkinter import ttk , messagebox
from tkinter import font
from tkinter.font import BOLD, Font

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

class Demo2(Frame):
    def __init__(self,master):
        Frame.__init__(self,master,width=1500,height=660)
        self.Heading_frame = Frame(self,background="black",borderwidth="2px",highlightbackground="black",relief="sunken")
        self.Heading_frame.pack(side="top",fill=X,expand=FALSE,pady="0.7px")
        # ttk_style.configure(self.Heading_frame , backgroung = "Black")
        self.Heading_Label = ttk.Label(self.Heading_frame,text="School Management",font=("Abadi MT Condensed Extra Bold",25,"bold","underline"),background="#70807F",foreground="White").pack(side="top",fill=X,expand=FALSE)
        self.side_frame_bg = "#C0C0C0"
        self.side_frame_text_size = 18
        self.Left_frame = Frame(self,borderwidth="1.5px",highlightbackground="black",relief="sunken",background=self.side_frame_bg)
        self.Left_frame.pack(side="left",fill=Y,padx="1px",pady="1px")
        self.Search_student_button = ttk.Button(self.Left_frame,text="New Admission",cursor="pencil",command=lambda : master.switch_frame(Demo3)).pack(fill=X,pady="4px",padx="2px")
        # Student_search = Label(self.Left_frame,text="Student details & fee",font=("Elephant",self.side_frame_text_size,"bold"),bg=self.side_frame_bg,pady="6px",fg="#000000").pack(side=TOP,pady="3px")
        self.Search_student_button = ttk.Button(self.Left_frame,text="Student details \& fee",style = 'TButton',cursor="pencil",command=lambda : master.switch_frame(Demo2)).pack(fill=X,pady="4px",padx="2px")
        # Student_search = Label(self.Left_frame,text="New Admission",font=("Elephant",self.side_frame_text_size,"bold"),bg=self.side_frame_bg,pady="6px",fg="#000000").pack(side=TOP,pady="3px")
        # Student_search = Label(self.Left_frame,text="Database Connection",font=("Elephant",self.side_frame_text_size,"bold"),bg=self.side_frame_bg,pady="6px",fg="#000000").pack(side=TOP,pady="3px")
        self.Search_student_button = ttk.Button(self.Left_frame,text="Database Connection",cursor="pencil").pack(fill=X,pady="4px",padx="2px")

        # self.master = master
        self.Student_search_frame = Frame(self,borderwidth=2,highlightbackground="Black",relief="sunken")
        self.style = ttk.Style()
        self.student_search_frame_text_size = 16
        self.student_search_frame_entry_size = 17
        self.Student_search_frame.pack(side = RIGHT,fill=BOTH,expand=TRUE,padx="1.5px",pady="1px")
        self.Student_search_title = Label(self.Student_search_frame,text="Student details & Fees",font=("Elephant",23,"bold","italic")).pack(side=TOP,fill=X)


        self.Student_search_button = Label(self.Student_search_frame,text="Student Search: ",font=("Elephant",self.student_search_frame_text_size,"bold")).place(x="30px",y="50px")

        self.btn1 = Button(self.Student_search_frame, text ='Search',font=("Elephant",15,"bold"),borderwidth=3,highlightbackground="black",bg="grey",cursor="pencil",command=lambda: self.switch_mini_frame(Demo2.Single_student_search(self)))
        self.btn1.place(x="150px",y="50px")


        self.class_search_button = Label(self.Student_search_frame,text="Class Search: ",font=("Elephant",self.student_search_frame_text_size,"bold")).place(x="350px",y="50px")

        self.btn1 = Button(self.Student_search_frame, text ='Search',font=("Elephant",15,"bold"),borderwidth=3,bg="grey",cursor="pencil",command=lambda: self.switch_mini_frame(Demo2.search_whole_class(self)))
        self.btn1.place(x="450px",y="50px")


        self.fee_pending_search_button = Label(self.Student_search_frame,text="All fee pending students:",font=("Elephant",self.student_search_frame_text_size,"bold")).place(x="580px",y="50px")

        self.btn1 = Button(self.Student_search_frame, text ='Search',font=("Elephant",15,"bold"),borderwidth=3,highlightbackground="black",bg="grey",cursor="pencil",command=lambda: self.switch_mini_frame(Demo2.all_non_fee_paid(self)))
        self.btn1.place(x="760px",y="50px")

        self.seperating_line = Label(self.Student_search_frame,text="_____________________________________________________________________________________________________",font=("Elephant",self.student_search_frame_text_size,"bold")).place(x="0px",y="90px")
        self.switch_mini_frame(Demo2.Single_student_search(self))
    def switch_mini_frame(self,frame_class):
        self.new_frame = frame_class
        self.single_student_value = 0
        self.class_search_value = 0
        self.all_non_fee_value = 0
        value = self.new_frame

        if value == 0 and self.single_student_value == 0:
            try:
                if self.whole_class_top_level_window.winfo_exists():
                    self.whole_class_top_level_window.destroy()
                    self.class_search_value = 0    
                if self.all_non_fee_paid_toplevel.winfo_exists():
                    self.all_non_fee_paid_toplevel.destroy()
                    self.all_non_fee_value = 0
            except:
                pass
            self.new_frame
            self.single_student_value = 1
        elif value == 1 and self.class_search_value == 0:
            try:
                if self.Single_student_top_level_window.winfo_exists():
                    self.Single_student_top_level_window.destroy()    
                    self.single_student_value = 0
                elif self.all_non_fee_paid_toplevel.winfo_exists():
                    self.all_non_fee_paid_toplevel.destroy()
                    self.all_non_fee_value = 0
            except:
                pass
            self.new_frame
            self.class_search_value = 1
        elif value == 2 and self.all_non_fee_value == 0:
            try:
                if self.Single_student_top_level_window.winfo_exists():
                    self.Single_student_top_level_window.destroy()
                    self.single_student_value = 0 
                elif self.whole_class_top_level_window.winfo_exists():
                    self.whole_class_top_level_window.destroy()
                    self.class_search_value = 0
            except:
                pass
            self.new_frame
            self.all_non_fee_value = 1
    
    def onclosing(self):
        pass


    def Single_student_search(self):
        self.Single_student_top_level_window = Toplevel(self)
        self.Single_student_top_level_window.geometry("1130x427+226+261")
        self.student_search_title = Label(self.Single_student_top_level_window,text="Student Details",font=("Elephant",23,"bold","underline")).place(x="30px",y="10px")
        self.Student_search_admission_No = Label(self.Single_student_top_level_window,text="Search by admission No:",font=("Elephant",self.student_search_frame_text_size,"bold")).place(x="30px",y="60px")
        self.Student_search_admission_no_input = ttk.Entry(self.Single_student_top_level_window,justify=LEFT,font=('Elephant',self.student_search_frame_entry_size,"bold"),foreground="Blue",background="green").place(x="220px",y="60px")
        self.btn1 = Button(self.Single_student_top_level_window, text ='Search',font=("Elephant",15,"bold"),bg="grey",cursor="pencil")
        self.btn1.place(x="410px",y="55px")
        self.Student_search_alternative = Label(self.Single_student_top_level_window,text="OR",font=("Elephant",22,"bold","underline")).place(x="30px",y="100px")
        self.Student_search_first_name = Label(self.Single_student_top_level_window,text="First Name : ",font=("Elephant",self.student_search_frame_text_size,"bold")).place(x="30px",y="140px")
        self.Student_search_first_name_input = ttk.Entry(self.Single_student_top_level_window,justify=LEFT,font=('courier',self.student_search_frame_entry_size,"bold"),foreground="Blue").place(x="190px",y="140px")
        self.Student_search_last_name = Label(self.Single_student_top_level_window,text="Last Name : ",font=("Elephant",self.student_search_frame_text_size,"bold")).place(x="440px",y="140px")
        self.Student_search_last_name_input = ttk.Entry(self.Single_student_top_level_window,justify=LEFT,font=('courier',self.student_search_frame_entry_size,"bold"),foreground="Blue").place(x="540px",y="140px")
        self.Student_search_roll_no = Label(self.Single_student_top_level_window,text="Roll Number : ",font=("Elephant",self.student_search_frame_text_size,"bold")).place(x="30px",y="180px")
        self.Student_search_RollNo_input = ttk.Entry(self.Single_student_top_level_window,justify=LEFT,font=('courier',self.student_search_frame_entry_size,"bold"),foreground="Blue").place(x="190px",y="180px")
     
        self.Student_search_class = Label(self.Single_student_top_level_window,text="Class : ",font=("Elephant",self.student_search_frame_text_size,"bold")).place(x="30px",y="220px")
        self.Student_search_class_var_type = IntVar()
        self.Student_search_class_input = ttk.Combobox(self.Single_student_top_level_window, width = 37, textvariable = self.Student_search_class_var_type,font=("Elephant",12,"bold"),foreground="Blue")
        self.Student_search_class_input['values'] = (1,2,3,4,5,6,7,8,9,10,11,12)
 
        self.Student_search_class_input.place(x="190px",y="220px")
 
        self.Student_search_section = Label(self.Single_student_top_level_window,text="Section : ",font=("Elephant",self.student_search_frame_text_size,"bold")).place(x="440px",y="220px")
        self.Student_search_section_var_type = StringVar()
     
        self.Student_search_section_input = ttk.Combobox(self.Single_student_top_level_window, width = 37, textvariable = self.Student_search_section_var_type,font=("Elephant",12,"bold"),foreground="Blue")
        self.Student_search_section_input['values'] = (list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
     
        self.Student_search_section_input.place(x="540px",y="220px")
        self.Student_search_section_input.current()
        self.style.configure('W.TButton', font =('calibri', 20, 'bold', 'underline'),foreground = 'Blue')
 
        self.btn1 = ttk.Button(self.Single_student_top_level_window, text = 'Search',style = 'W.TButton',cursor="pencil")
        self.btn1.place(x="350px",y="260px")

        # self.Single_student_top_level_window.bind("<Map>",Demo2.on_closing)
        return 0
 
    def search_whole_class(self):
       self.whole_class_top_level_window = Toplevel(self)
       self.whole_class_top_level_window.geometry("1130x427+226+261")
       self.style = ttk.Style()
       self.student_search_frame_text_size = 16
       self.student_search_frame_entry_size = 17
       self.class_search_title = Label(self.whole_class_top_level_window,text="Class Details",font=("Elephant",23,"bold","underline")).place(x="30px",y="20px")
       self.class_search_class_section = Label(self.whole_class_top_level_window,text="Class and Section",font=("Elephant",18,"bold","underline"),foreground="Blue").place(x="30px",y="60px")
       self.Student_search_class = Label(self.whole_class_top_level_window,text="Class : ",font=("Elephant",self.student_search_frame_text_size,"bold")).place(x="30px",y="100px")
       self.Student_search_class_var_type = IntVar()
       self.Student_search_class_input = ttk.Combobox(self.whole_class_top_level_window, width = 37, textvariable = self.Student_search_class_var_type,font=("Elephant",12,"bold"),foreground="Blue")
       self.Student_search_class_input['values'] = (1,2,3,4,5,6,7,8,9,10,11,12)
    
       self.Student_search_class_input.place(x="190px",y="100px")
       self.Student_search_class_input.current()
       self.Student_search_section = Label(self.whole_class_top_level_window,text="Section : ",font=("Elephant",self.student_search_frame_text_size,"bold")).place(x="440px",y="100px")
       self.Student_search_section_var_type = StringVar()
    
       self.Student_search_section_input = ttk.Combobox(self.whole_class_top_level_window, width = 37, textvariable = self.Student_search_section_var_type,font=("Elephant",12,"bold"),foreground="Blue")
       self.Student_search_section_input['values'] = ["All"]+(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
    
       self.Student_search_section_input.place(x="540px",y="100px")
       self.Student_search_section_input.current()
       self.style.configure('W.TButton', font =('calibri', 20, 'bold', 'underline'),foreground = 'Blue')
       self.class_search_class_section = Label(self.whole_class_top_level_window,text="Limit Roll Numbers",font=("Elephant",18,"bold","underline"),foreground="Blue").place(x="30px",y="130px")
       self.Student_limit_rollNo_lower = Label(self.whole_class_top_level_window,text="From : ",font=("Elephant",self.student_search_frame_text_size,"bold")).place(x="30px",y="170px")
       self.Student_limit_rollNo_lower_var_type = IntVar()
       self.Student_limit_rollNo_lower_input = ttk.Combobox(self.whole_class_top_level_window, width = 37, textvariable = self.Student_search_class_var_type,font=("Elephant",12,"bold"),foreground="Blue")
       self.Student_limit_rollNo_lower_input['values'] = [x for x in range(0,101)]
    
       self.Student_limit_rollNo_lower_input.place(x="190px",y="170px")
       self.Student_limit_rollNo_lower_input.current()
       self.Student_limit_rollNo_upper = Label(self.whole_class_top_level_window,text="To : ",font=("Elephant",self.student_search_frame_text_size,"bold")).place(x="440px",y="170px")
       self.Student_limit_rollNo_upper_var_type = IntVar()
       self.Student_limit_rollNo_upper_input = ttk.Combobox(self.whole_class_top_level_window, width = 37, textvariable = self.Student_search_class_var_type,font=("Elephant",12,"bold"),foreground="Blue")
       self.Student_limit_rollNo_upper_input['values'] = ["All"]+[x for x in range(0,101)]
    
       self.Student_limit_rollNo_upper_input.place(x="540px",y="170px")
       self.Student_limit_rollNo_upper_input.current()
       self.btn1 = ttk.Button(self.whole_class_top_level_window, text = 'Search',style = 'W.TButton',cursor="pencil")
       self.btn1.place(x="340px",y="250px")
       return 1

    def all_non_fee_paid(self):
       self.all_non_fee_paid_toplevel = Toplevel(self)
       self.all_non_fee_paid_toplevel.geometry("1130x427+226+261")
       self.class_search_title = Label(self.all_non_fee_paid_toplevel,text="List of all non fee paid students : ",font=("Elephant",23,"bold","underline")).place(x="30px",y="30px")
       self.class_search_title = Label(self.all_non_fee_paid_toplevel,text="Categorize : ",font=("Elephant",23,"bold","underline")).place(x="30px",y="100px")
       self.button_alphabetically = Button(self.all_non_fee_paid_toplevel, text = '1. Alphabatical Order',highlightbackground="black",borderwidth="2px",font=("Elephant",20,"bold","underline"),relief="raised",cursor="pencil")
       self.button_alphabetically.place(x="30px",y="200px")
       self.button_class_wise = Button(self.all_non_fee_paid_toplevel, text = '2. Class Wise',highlightbackground="black",borderwidth="2px",font=("Elephant",20,"bold","underline"),relief="raised",cursor="pencil")
       self.button_class_wise.place(x="350px",y="200px")
       return 2

class Demo3(Frame):
    def __init__(self,master):
        Frame.__init__(self,master,width=1500,height=660)
        self.Heading_frame = Frame(self,background="black",borderwidth="2px",highlightbackground="black",relief="sunken")
        self.Heading_frame.pack(side="top",fill=X,expand=FALSE,pady="0.7px")
        # ttk_style.configure(self.Heading_frame , backgroung = "Black")
        self.Heading_Label = ttk.Label(self.Heading_frame,text="School Management",font=("Abadi MT Condensed Extra Bold",25,"bold","underline"),background="#70807F",foreground="White").pack(side="top",fill=X,expand=FALSE)
        self.side_frame_bg = "#C0C0C0"
        self.side_frame_text_size = 18
        self.Left_frame = Frame(self,borderwidth="1.5px",highlightbackground="black",relief="sunken",background=self.side_frame_bg)
        self.Left_frame.pack(side="left",fill=Y,padx="1px",pady="1px")
        self.Search_student_button = ttk.Button(self.Left_frame,text="New Admission",cursor="pencil",command=lambda : master.switch_frame(Demo3)).pack(fill=X,pady="4px",padx="2px")
        # Student_search = Label(self.Left_frame,text="Student details & fee",font=("Elephant",self.side_frame_text_size,"bold"),bg=self.side_frame_bg,pady="6px",fg="#000000").pack(side=TOP,pady="3px")
        self.Search_student_button = ttk.Button(self.Left_frame,text="Student details \& fee",style = 'TButton',cursor="pencil",command=lambda : master.switch_frame(Demo2)).pack(fill=X,pady="4px",padx="2px")
        # Student_search = Label(self.Left_frame,text="New Admission",font=("Elephant",self.side_frame_text_size,"bold"),bg=self.side_frame_bg,pady="6px",fg="#000000").pack(side=TOP,pady="3px")
        # Student_search = Label(self.Left_frame,text="Database Connection",font=("Elephant",self.side_frame_text_size,"bold"),bg=self.side_frame_bg,pady="6px",fg="#000000").pack(side=TOP,pady="3px")
        self.Search_student_button = ttk.Button(self.Left_frame,text="Database Connection",cursor="pencil").pack(fill=X,pady="4px",padx="2px")


        self.Student_admission_frame = Frame(self,borderwidth=2,highlightbackground="Black",relief="sunken")
        self.first_row_text = "10px"
        self.first_row_entry = "100px"
        self.second_row_text = "270px"
        self.second_row_entry = "360px"
        self.third_row_text = "530px"
        self.third_row_entry = "630px"

        style = ttk.Style()
        self.student_admission_frame_text_size = 12
        self.student_admission_frame_entry_size = 13
        self.Student_admission_frame.pack(side = LEFT,fill=BOTH,expand=TRUE,pady="0.7",padx="0.7")
        self.Student_admission_title = Label(self.Student_admission_frame,text="New Admission",font=("Elephant",27,"bold","italic","underline")).pack(side=TOP,fill=X)

        self.Student_admission_student_name = Label(self.Student_admission_frame,text="Student",font=("Elephant",15,"bold","underline"),foreground="Blue").place(x=self.first_row_text,y="45px")

        self.Student_admission_first_name_student = Label(self.Student_admission_frame,text="First Name : ",font=("Elephant",self.student_admission_frame_text_size,"bold")).place(x=self.first_row_text,y="70px")
        self.Student_admission_first_name_student_input = ttk.Entry(self.Student_admission_frame,justify=LEFT,font=('courier',self.student_admission_frame_entry_size,"bold"),foreground="Blue").place(x=self.first_row_entry,y="70px")

        self.Student_admission_last_name_student = Label(self.Student_admission_frame,text="Last Name : ",font=("Elephant",self.student_admission_frame_text_size,"bold")).place(x=self.second_row_text,y="70px")
        self.Student_admission_last_name_student_input = ttk.Entry(self.Student_admission_frame,justify=LEFT,font=('courier',self.student_admission_frame_entry_size,"bold"),foreground="Blue").place(x=self.second_row_entry,y="70px")

        self.Student_admission_DOB_student = Label(self.Student_admission_frame,text="DOB : ",font=("Elephant",self.student_admission_frame_text_size,"bold")).place(x=self.third_row_text,y="70px")
        self.Student_admission_DOB_student_input = ttk.Entry(self.Student_admission_frame,justify=LEFT,font=('courier',self.student_admission_frame_entry_size,"bold"),foreground="Blue").place(x=self.third_row_entry,y="70px")

        self.Student_search_class_var_type = IntVar()
        self.Student_admission_class = Label(self.Student_admission_frame,text="Class : ",font=("Elephant",self.student_admission_frame_text_size,"bold")).place(x=self.first_row_text,y="95px")
        self.Student_admission_class_input = ttk.Combobox(self.Student_admission_frame, width = 23, textvariable = self.Student_search_class_var_type,font=("Elephant",12,"bold"),foreground="Blue")
        self.Student_admission_class_input['values'] = (1,2,3,4,5,6,7,8,9,10,11,12)
        self.Student_admission_class_input.place(x=self.first_row_entry,y="95px")
        self.Student_admission_class_input.current()

        self.Student_search_section_var_type = StringVar()
        self.Student_admission_section = Label(self.Student_admission_frame,text="Section : ",font=("Elephant",self.student_admission_frame_text_size,"bold")).place(x=self.second_row_text,y="95px")
        self.Student_admission_section_input = ttk.Combobox(self.Student_admission_frame, width = 23, textvariable = self.Student_search_section_var_type,font=("Elephant",12,"bold"),foreground="Blue")
        self.Student_admission_section_input['values'] = (list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
        self.Student_admission_section_input.place(x=self.second_row_entry,y="95px")
        self.Student_admission_section_input.current()

        self.Student_admission_address_student = Label(self.Student_admission_frame,text="Home Address : ",font=("Elephant",self.student_admission_frame_text_size,"bold")).place(x=self.first_row_text,y="120px")
        self.Student_admission_address_student_input = Text(self.Student_admission_frame,height=1,background="white",font=('Elephant',self.student_admission_frame_entry_size,),foreground="Blue").place(x=self.first_row_entry,y="120px")


        self.Student_admission_father_name = Label(self.Student_admission_frame,text="Father",font=("Elephant",15,"bold","underline"),foreground="Blue").place(x=self.first_row_text,y="150px")

        self.Student_admission_first_name_father = Label(self.Student_admission_frame,text="First Name : ",font=("Elephant",self.student_admission_frame_text_size,"bold")).place(x=self.first_row_text,y="185px")
        self.Student_admission_first_name_father_input = ttk.Entry(self.Student_admission_frame,justify=LEFT,font=('courier',self.student_admission_frame_entry_size,"bold"),foreground="Blue").place(x=self.first_row_entry,y="185px")

        self.Student_admission_last_name_father = Label(self.Student_admission_frame,text="Last Name : ",font=("Elephant",self.student_admission_frame_text_size,"bold")).place(x=self.second_row_text,y="185px")
        self.Student_admission_last_name_father_input = ttk.Entry(self.Student_admission_frame,justify=LEFT,font=('courier',self.student_admission_frame_entry_size,"bold"),foreground="Blue").place(x=self.second_row_entry,y="185px")

        self.Student_admission_MobileNo_father = Label(self.Student_admission_frame,text="Phone No : ",font=("Elephant",self.student_admission_frame_text_size,"bold")).place(x=self.third_row_text,y="185px")
        self.Student_admission_MobileNo_father_input = ttk.Entry(self.Student_admission_frame,justify=LEFT,font=('courier',self.student_admission_frame_entry_size,"bold"),foreground="Blue").place(x=self.third_row_entry,y="185px")

        self.Student_admission_occupation_father = Label(self.Student_admission_frame,text="Occupation : ",font=("Elephant",self.student_admission_frame_text_size,"bold")).place(x=self.first_row_text,y="210px")
        self.Student_admission_Occupation_father_input = ttk.Entry(self.Student_admission_frame,justify=LEFT,font=('courier',self.student_admission_frame_entry_size,"bold"),foreground="Blue").place(x=self.first_row_entry,y="210px")

        self.Student_admission_address_student = Label(self.Student_admission_frame,text="Office Address:",font=("Elephant",self.student_admission_frame_text_size,"bold")).place(x=self.first_row_text,y="235px")
        self.Student_admission_address_student_input = Text(self.Student_admission_frame,height=1,background="white",font=('Elephant',self.student_admission_frame_entry_size,),foreground="Blue").place(x=self.first_row_entry,y="235px")


        self.Student_admission_Mother_name = Label(self.Student_admission_frame,text="Mother",font=("Elephant",15,"bold","underline"),foreground="Blue").place(x=self.first_row_text,y="265px")

        self.Student_admission_first_name_mother = Label(self.Student_admission_frame,text="First Name : ",font=("Elephant",self.student_admission_frame_text_size,"bold")).place(x=self.first_row_text,y="295px")
        self.Student_admission_first_name_mother_input = ttk.Entry(self.Student_admission_frame,justify=LEFT,font=('courier',self.student_admission_frame_entry_size,"bold"),foreground="Blue").place(x=self.first_row_entry,y="295px")

        self.Student_admission_last_name_mother = Label(self.Student_admission_frame,text="Last Name : ",font=("Elephant",self.student_admission_frame_text_size,"bold")).place(x=self.second_row_text,y="295px")
        self.Student_admission_last_name_mother_input = ttk.Entry(self.Student_admission_frame,justify=LEFT,font=('courier',self.student_admission_frame_entry_size,"bold"),foreground="Blue").place(x=self.second_row_entry,y="295px")

        self.Student_admission_MobileNo_mother = Label(self.Student_admission_frame,text="Phone No : ",font=("Elephant",self.student_admission_frame_text_size,"bold")).place(x=self.third_row_text,y="295px")
        self.Student_admission_MobileNo_mother_input = ttk.Entry(self.Student_admission_frame,justify=LEFT,font=('courier',self.student_admission_frame_entry_size,"bold"),foreground="Blue").place(x=self.third_row_entry,y="295px")


        self.Student_admission_occupation_mother = Label(self.Student_admission_frame,text="Occupation : ",font=("Elephant",self.student_admission_frame_text_size,"bold")).place(x=self.first_row_text,y="320px")
        self.Student_admission_Occupation_mother_input = ttk.Entry(self.Student_admission_frame,justify=LEFT,font=('courier',self.student_admission_frame_entry_size,"bold"),foreground="Blue").place(x=self.first_row_entry,y="320px")

        self.Student_admission_address_student = Label(self.Student_admission_frame,text="Office Address:",font=("Elephant",self.student_admission_frame_text_size,"bold")).place(x=self.first_row_text,y="345px")
        self.Student_admission_address_student_input = Text(self.Student_admission_frame,height=1,background="white",font=('Elephant',self.student_admission_frame_entry_size,),foreground="Blue").place(x=self.first_row_entry,y="345px")



        style.configure('W.TButton', font =('calibri', 30, 'bold', 'underline'),foreground = 'Blue')
        
        self.btn1 = ttk.Button(self.Student_admission_frame, text = 'Submit',style = 'W.TButton',cursor="pencil")
        self.btn1.place(x=self.second_row_text,y="390px")



def main():
    app = Demo0() 
    app.geometry("1360x700")
    app.title("Fee Collection")
    app.config(background="Black")
    # Demo3(root)    
    app.mainloop()


if __name__ == '__main__':
    main()