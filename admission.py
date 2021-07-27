from tkinter import *
from tkinter import ttk , messagebox
from tkinter import font
from tkinter.font import BOLD, Font
from windowinit import *
from student_fee import *
import student_fee

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
        self.Search_student_button = ttk.Button(self.Left_frame,text="Student details \& fee",style = 'TButton',cursor="pencil",command=lambda : master.switch_frame(student_fee.Demo2)).pack(fill=X,pady="4px",padx="2px")
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

