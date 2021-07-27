from tkinter import *
from tkinter import ttk , messagebox
from tkinter import font
from tkinter.font import BOLD, Font
from windowinit import *
from student_fee import *
from admission import *
import admission
from mainapp import *


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