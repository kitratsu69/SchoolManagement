from tkinter import *
from tkinter import ttk , messagebox
from tkinter import font
from tkinter.font import BOLD, Font
from windowinit import *
from student_fee import *
from admission import *

def main():
    listis = []
    app = Demo0() 
    app.geometry("1360x700")
    app.title("Fee Collection")
    app.config(background="Black") 
    app.mainloop()


if __name__ == '__main__':
    main()