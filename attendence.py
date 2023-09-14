from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog

myData = []
class Attendence:

    def __init__(self , root):

        self.root = root
        #now set geometry of the window
        self.root.geometry("1530x790+0+0")
        #set title
        self.root.title("Attendance Management")

        #-----TEXT VARIABLES------#
        self.var_enroll_id = StringVar()
        self.var_Name = StringVar()
        self.Var_branch = StringVar()
        self.var_sem = StringVar()
        self.var_time = StringVar()
        self.var_date = StringVar()
        self.var_attendence = StringVar()
        #img --> 1
        img = Image.open(r"C:\face_recognition_system\images\student_details1.jpg")

        #set size
        img = img.resize((500,130),Image.ADAPTIVE)

        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root , image = self.photoimg)

        f_lbl.place(x=0 , y=0 , width = 500 , height = 130)

        #img --> 2

        img1 = Image.open(r"C:\face_recognition_system\images\student_details2.jpg")

        #set size
        img1 = img1.resize((500,130),Image.ADAPTIVE)

        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root , image = self.photoimg1)

        f_lbl.place(x=500 , y=0 , width = 500 , height = 130)
        
        #img --> 3

        img2 = Image.open(r"C:\face_recognition_system\images\student_details3.jpg")

        #set size
        img2 = img2.resize((600,130),Image.ADAPTIVE)

        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root , image = self.photoimg2)

        f_lbl.place(x=1000 , y=0 , width = 500 , height = 130)
        
                #bg-color
        img3 = Image.open(r"C:\face_recognition_system\images\bgColor.jpg")

        #set size
        img3 = img3.resize((1530,710),Image.ADAPTIVE)

        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root , image = self.photoimg3)

        bg_img.place(x=0 , y=130 , width = 1530 , height = 710)

        title_lbl = Label(bg_img , text = "ATTENDANCE MANAGEMENT",font=("times new roman",35,"bold"), bg="dark blue",fg="yellow")

        title_lbl.place(x=0 , y=0,width=1530,height=45)

        main_frame = Frame(bg_img , bd = 3 , bg = "light blue")

        main_frame.place(x=10 , y=55 , width = 1500 , height = 600)

        Left_frame = LabelFrame(main_frame,bd=3,bg="light blue",relief="sunken",text="ATTENDANCE MANAGEMENT",font=("times new roman",12,"bold"))

        Left_frame.place(x=10 , y=10 , width=760 , height=580)

        #img
        img_lft = Image.open(r"C:\face_recognition_system\images\attendence.jpg")

        #set size
        img_lft = img_lft.resize((740,130),Image.ADAPTIVE)

        self.photoimg_lft = ImageTk.PhotoImage(img_lft)

        f_lbl = Label(Left_frame , image = self.photoimg_lft)

        f_lbl.place(x=5 , y=0 , width = 740 , height = 130)

        #entries

        student_frame = LabelFrame(Left_frame,bd=3,bg="light blue",relief=RIDGE,text="Student Information",font=("times new roman",12,"bold"))

        student_frame.place(x=0,y=135,width=750,height=300)

        enrolNum_label = Label(student_frame,text="Enrollment ID",font=("times new roman",12,"bold"),bg="yellow")
        enrolNum_label.grid(row=0 , column=0 ,padx=10)

        enrolNum_entry = ttk.Entry(student_frame , font=("times new roman",12,"bold"),textvariable=self.var_enroll_id)
        enrolNum_entry.grid(row = 0 , column = 1 , padx = 10)

        #student name

        studentName_label = Label(student_frame,text="Name",font=("times new roman",12,"bold"),bg="yellow")
        studentName_label.grid(row=0 , column=2 ,padx=10 ,pady = 5)

        studentName_entry = ttk.Entry(student_frame , font=("times new roman",12,"bold"),textvariable=self.var_Name)
        studentName_entry.grid(row = 0 , column = 3 , padx = 10 , pady = 5)

        #DOB

        DOB_label = Label(student_frame,text="Branch",font=("times new roman",12,"bold"),bg="yellow")
        DOB_label.grid(row=1 , column=0 ,padx=10 ,pady = 5)

        DOB_entry = ttk.Entry(student_frame , font=("times new roman",12,"bold"),textvariable=self.Var_branch)
        DOB_entry.grid(row = 1, column = 1 , padx = 10 , pady = 5)

        #gender

        gender_label = Label(student_frame,text="Semester",font=("times new roman",12,"bold"),bg="yellow")
        gender_label.grid(row=1 , column=2 ,padx=10 ,pady = 5)

        DOB_entry = ttk.Entry(student_frame , font=("times new roman",12,"bold"),textvariable=self.var_sem)
        DOB_entry.grid(row = 1, column = 3 , padx = 10 , pady = 5)

        #e-mail

        mail_label = Label(student_frame,text="Date",font=("times new roman",12,"bold"),bg="yellow")
        mail_label.grid(row=2 , column=0 ,padx=10 ,pady = 5)

        mail_entry = ttk.Entry(student_frame ,font=("times new roman",12,"bold"),textvariable=self.var_date)
        mail_entry.grid(row = 2, column = 1 , padx = 10 , pady = 5)

        #phone

        phone_label = Label(student_frame,text="Time",font=("times new roman",12,"bold"),bg="yellow")
        phone_label.grid(row=2 , column=2 ,padx=10 ,pady = 5)

        phone_entry = ttk.Entry(student_frame , font=("times new roman",12,"bold"),textvariable=self.var_time)
        phone_entry.grid(row = 2, column = 3 , padx = 10 , pady = 5)

        status_label = Label(student_frame,text="Attendance Status",font=("times new roman",12,"bold"),bg="yellow")
        status_label.grid(row=3 , column=0 ,padx=10)

        status_combo = ttk.Combobox(student_frame,font=("times new roman",12,"bold"),width=25,state="readonly",textvariable=self.var_attendence)
        status_combo["values"] = ("Status","PRESENT","ABSENT")
        status_combo.current(0)
        status_combo.grid(row=3 , column=1 ,padx=2,pady=10)

        btn_frame=Frame(student_frame,bd=3,relief=RIDGE,bg="light blue")
        btn_frame.place(x=8,y=245,width=715,height=140)

        #buttons

        save_btn=Button(btn_frame,text="IMPORT",command=self.CSV,width=25,font=("times new roman",12,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="EXPORT",command=self.exp_CSV,width=25,font=("times new roman",12,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=2)

        #delete_btn=Button(btn_frame,text="UPDATE",width=19,font=("times new roman",12,"bold"),bg="blue",fg="white")
        #delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="RESET",width=27,font=("times new roman",12,"bold"),command=self.reset,bg="blue",fg="white")
        reset_btn.grid(row=0,column=4)
        

    #right frame
        Right_frame = LabelFrame(main_frame,bd=3,bg="light blue",relief="ridge",text="Student Details",font=("times new roman",12,"bold"))

        Right_frame.place(x=780,y=10,width=680,height=580)

    # scroll bars #

        table_frame=Frame(Right_frame,bd=3,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=10,width=670,height=500)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_Y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendenceReport=ttk.Treeview(table_frame,column=("enroll id","name","branch","year","semester","date","time","attendence"))


        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_Y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttendenceReport.xview)
        scroll_Y.config(command=self.AttendenceReport.yview)
        
        self.AttendenceReport.heading("enroll id",text="Enrollment ID")
        self.AttendenceReport.heading("name",text="NAME")
        self.AttendenceReport.heading("branch",text="BRANCH")
        self.AttendenceReport.heading("year",text="YEAR")
        self.AttendenceReport.heading("semester",text="SEMESTER")
        self.AttendenceReport.heading("date",text="DATE")
        self.AttendenceReport.heading("time",text="TIME")
        self.AttendenceReport.heading("attendence",text="ATTENDANCE")
        
        self.AttendenceReport["show"] = "headings"
        self.AttendenceReport.column("enroll id",width=100)
        self.AttendenceReport.column("name",width=100)
        self.AttendenceReport.column("branch",width=100)
        self.AttendenceReport.column("year",width=100)
        self.AttendenceReport.column("semester",width=100)
        self.AttendenceReport.column("date",width=100)
        self.AttendenceReport.column("time",width=100)
        self.AttendenceReport.column("attendence",width=100)

        self.AttendenceReport.pack(fill=BOTH,expand=1)

        self.AttendenceReport.bind("<ButtonRelease>",self.get_cursor)
    
    def fetchData(self,rows):

        self.AttendenceReport.delete(*self.AttendenceReport.get_children())

        for i in rows:
            self.AttendenceReport.insert("",END,values=i)
    #CSV import
    def CSV(self):

        global myData
        myData.clear()

        filName = filedialog.askopenfilename(initialdir=os.getcwd,title="CSV",filetypes=(("CSV Files","*.csv"),("All File","*.*")),parent=self.root) #current working directory
        with open(filName) as myFile:
            csvRead = csv.reader(myFile)

            for i in csvRead:
                myData.append(i)
            self.fetchData(myData)

    #CSV export
    def exp_CSV(self):

        try:
        
        #check if table is not empty
        
            if len(myData)<=0:
                messagebox.showerror("NO DATA","NO DATA FOUND",parent = self.root)
                return False
        
            filName = filedialog.asksaveasfilename(initialdir=os.getcwd,title="CSV",filetypes=(("CSV Files","*.csv"),("All File","*.*")),parent=self.root) #current working directory
            with open(filName,mode="w",newline="") as myFile:
                export_write = csv.writer(myFile)

                for i in myData:
                    export_write.writerow(i)
                messagebox.showinfo("DATA EXPORTED","Data has been sucessfully exported")

    
        except:
            messagebox.showerror("ERROR","error occured in data exporting!!!")  


    def get_cursor(self,ev=""):
        cursor_row = self.AttendenceReport.focus()
        content = self.AttendenceReport.item(cursor_row)

        rows = content["values"]
        self.var_enroll_id.set(rows[0])
        self.var_Name.set(rows[1])
        self.Var_branch.set(rows[2]) 
        self.var_sem.set(rows[3])
        self.var_date.set(rows[4])  
        self.var_time.set(rows[5]) 
        self.var_attendence.set(rows[6]) 
    
    def reset(self):
    
        self.var_enroll_id.set("")
        self.var_Name.set("")
        self.Var_branch.set("") 
        self.var_sem.set("")
        self.var_date.set("")  
        self.var_time.set("") 
        self.var_attendence.set("") 
    



if __name__ == "__main__":
   
    root = Tk() #call root from tool kit

    obj = Attendence(root)

     #  root['bg'] = '#69698B'

    root.mainloop() 