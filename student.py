from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os

class student:

    def __init__(self , root):

        self.root = root
        #now set geometry of the window
        self.root.geometry("1530x790+0+0")
        #set title
        self.root.title("Student Details")

        #variables
        self.var_bra=StringVar()
        self.var_year=StringVar()
        self.var_sem=StringVar()
        self.var_enroll_num=StringVar()
        self.var_name=StringVar()
        self.var_gender=StringVar()
        self.var_email=StringVar()
        self.var_dob=StringVar()
        self.var_contact=StringVar()
        self.var_hostel=StringVar()
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

        title_lbl = Label(bg_img , text = "STUDENT DETAILS",font=("times new roman",35,"bold"), bg="blue",fg="white")

        title_lbl.place(x=0 , y=0,width=1530,height=45)

        #main - frame --> all functionalities included in here...
        main_frame = Frame(bg_img , bd = 3 , bg = "white")

        main_frame.place(x=10 , y=55 , width = 1500 , height = 600)

        #label frames...

        #left label frame...

        Left_frame = LabelFrame(main_frame,bd=3,bg="white",relief="sunken",text="Student Details",font=("times new roman",12,"bold"))

        Left_frame.place(x=10 , y=10 , width=760 , height=580)

        #images add here...

        img_lft = Image.open(r"C:\face_recognition_system\images\img6.jpg")

        #set size
        img_lft = img_lft.resize((740,130),Image.ADAPTIVE)

        self.photoimg_lft = ImageTk.PhotoImage(img_lft)

        f_lbl = Label(Left_frame , image = self.photoimg_lft)

        f_lbl.place(x=5 , y=0 , width = 740 , height = 130)
        
        #new frame --> current coures

        curr_course_frame = LabelFrame(Left_frame,bd=3,bg="white",relief=RIDGE,text="Current Course",font=("times new roman",12,"bold"))

        curr_course_frame.place(x=5,y=135,width=740,height=150)

        bra_label = Label(curr_course_frame,text="Branch",font=("times new roman",12,"bold"),bg="yellow")

        bra_label.grid(row=0 , column=0 , padx = 2 , pady = 10)

        #combo box --> 

        bra_combo = ttk.Combobox(curr_course_frame,textvariable=self.var_bra,font=("times new roman",12,"bold"),width=25,state="readonly")
        bra_combo["values"] = ("Select Branch","CSE","ECE","CIVIL","BI/BT")
        bra_combo.current(0)
        bra_combo.grid(row=0 , column=1  , padx=2 , pady=10) #col incremented

        #2nd--> year

        year_label = Label(curr_course_frame,text="Year",font=("times new roman",12,"bold"),bg="yellow")
        year_label.grid(row=0 , column=2 ,padx=10)

        year_combo = ttk.Combobox(curr_course_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),width=25,state="readonly")
        year_combo["values"] = ("Select Year","1st","2nd","3rd","4th")
        year_combo.current(0)
        year_combo.grid(row=0 , column=3 ,padx=2,pady=10)

        #3rd --> semester

        sem_label = Label(curr_course_frame,text="Semester",font=("times new roman",12,"bold"),bg="yellow")
        sem_label.grid(row=10 , column=0 ,padx=10)

        sem_combo = ttk.Combobox(curr_course_frame,textvariable=self.var_sem,font=("times new roman",12,"bold"),width=25,state="readonly")
        sem_combo["values"] = ("Select Semester","1st","2nd","3rd","4th","5th","6th","7th","8th")
        sem_combo.current(0)
        sem_combo.grid(row=10 , column=1 ,padx=2,pady=10)

        #4th --> hostel status

        hostel_label = Label(curr_course_frame,text="Hostel Status",font=("times new roman",12,"bold"),bg="yellow")
        hostel_label.grid(row=10 , column=2 ,padx=10)

        hostel_combo = ttk.Combobox(curr_course_frame,textvariable=self.var_hostel,font=("times new roman",12,"bold"),width=25,state="readonly")
        hostel_combo["values"] = ("Select Hostel Status","Hostler","Non-Hostler")
        hostel_combo.current(0)
        hostel_combo.grid(row=10 , column=3 ,padx=2,pady=10)

        #class student information

        student_frame = LabelFrame(Left_frame,bd=3,bg="white",relief=RIDGE,text="Student Information",font=("times new roman",12,"bold"))

        student_frame.place(x=5,y=250,width=740,height=300)

        enrolNum_label = Label(student_frame,text="Enrollment Number",font=("times new roman",12,"bold"),bg="yellow")
        enrolNum_label.grid(row=0 , column=0 ,padx=10)

        enrolNum_entry = ttk.Entry(student_frame ,textvariable=self.var_enroll_num, font=("times new roman",12,"bold"))
        enrolNum_entry.grid(row = 0 , column = 1 , padx = 10)

        #student name

        studentName_label = Label(student_frame,text="Student Name",font=("times new roman",12,"bold"),bg="yellow")
        studentName_label.grid(row=0 , column=2 ,padx=10 ,pady = 5)

        studentName_entry = ttk.Entry(student_frame ,textvariable=self.var_name, font=("times new roman",12,"bold"))
        studentName_entry.grid(row = 0 , column = 3 , padx = 10 , pady = 5)

        #DOB

        DOB_label = Label(student_frame,text="Date Of Birth",font=("times new roman",12,"bold"),bg="yellow")
        DOB_label.grid(row=1 , column=0 ,padx=10 ,pady = 5)

        DOB_entry = ttk.Entry(student_frame ,textvariable=self.var_dob, font=("times new roman",12,"bold"))
        DOB_entry.grid(row = 1, column = 1 , padx = 10 , pady = 5)

        #gender

        gender_label = Label(student_frame,text="Gender",font=("times new roman",12,"bold"),bg="yellow")
        gender_label.grid(row=1 , column=2 ,padx=10 ,pady = 5)

        DOB_entry = ttk.Entry(student_frame ,textvariable=self.var_gender,  font=("times new roman",12,"bold"))
        DOB_entry.grid(row = 1, column = 3 , padx = 10 , pady = 5)

        #e-mail

        mail_label = Label(student_frame,text="Email",font=("times new roman",12,"bold"),bg="yellow")
        mail_label.grid(row=2 , column=0 ,padx=10 ,pady = 5)

        mail_entry = ttk.Entry(student_frame ,textvariable=self.var_email,font=("times new roman",12,"bold"))
        mail_entry.grid(row = 2, column = 1 , padx = 10 , pady = 5)

        #phone

        phone_label = Label(student_frame,text="Contact Number",font=("times new roman",12,"bold"),bg="yellow")
        phone_label.grid(row=2 , column=2 ,padx=10 ,pady = 5)

        phone_entry = ttk.Entry(student_frame ,textvariable=self.var_contact, font=("times new roman",12,"bold"))
        phone_entry.grid(row = 2, column = 3 , padx = 10 , pady = 5)
        

        #buttons
        self.var_radio1=StringVar()
        radio1 = ttk.Radiobutton(student_frame,variable=self.var_radio1,text="Take Photo Sample",value="YES")
        radio1.grid(row=3 , column = 0)

        radio2 = ttk.Radiobutton(student_frame,variable=self.var_radio1,text="Do Not Take Photo Sample",value="NO")
        radio2.grid(row=3 , column = 1)

        #button frame


        btn_frame=Frame(student_frame,bd=3,relief=RIDGE,bg="white")
        btn_frame.place(x=8,y=130,width=715,height=140)

        #buttons

        save_btn=Button(btn_frame,text="SAVE",command=self.add_data,width=18,font=("times new roman",12,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="UPDATE",command=self.update_data,width=20,font=("times new roman",12,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="DELETE",command=self.delete_data,width=19,font=("times new roman",12,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="RESET",command=self.reset_data,width=18,font=("times new roman",12,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)

        btn_frame1=Frame(student_frame,bd=3,relief=SUNKEN,bg="white")
        btn_frame1.place(x=200,y=200,width=300,height=35)

        takePhoto_btn=Button(btn_frame1,command=self.generateDataSet,text="Take Photo Sample",width=35,font=("times new roman",12,"bold"),bg="blue",fg="white")
        takePhoto_btn.grid(row=0,column=0)








        #right label frame...

        Right_frame = LabelFrame(main_frame,bd=3,bg="white",relief="ridge",text="Student Details",font=("times new roman",12,"bold"))

        Right_frame.place(x=780,y=10,width=680,height=580)

        
        img_rit = Image.open(r"C:\face_recognition_system\images\ritFrame.jpg")

        #set size
        img_rit = img_rit.resize((700,130),Image.ADAPTIVE)

        self.photoimg_rit = ImageTk.PhotoImage(img_rit)

        f_lbl = Label(Right_frame , image = self.photoimg_rit)

        f_lbl.place(x=5 , y=0 , width = 700 , height = 150)
        
        

        #table frame

        table_frame=Frame(Right_frame,bd=3,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=150,width=670,height=400)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_Y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,column=("branch","name","enrollment number","year","sem","gender","contact","email","date of birth","hostel status","photo"))

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_Y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.student_table.xview)
        scroll_Y.config(command=self.student_table.yview)
        
        self.student_table.heading("branch",text="BRANCH")
        self.student_table.heading("name",text="NAME")
        self.student_table.heading("enrollment number",text="ENROLLMENT NUMBER")
        self.student_table.heading("year",text="YEAR")
        self.student_table.heading("sem",text="SEMESTER")
        self.student_table.heading("gender",text="GENDER")
        self.student_table.heading("contact",text="CONTACT")
        self.student_table.heading("email",text="EMAIL")
        self.student_table.heading("date of birth",text="DATE OF BIRTH")
        self.student_table.heading("hostel status",text="HOSTEL STATUS")
        self.student_table.heading("photo",text="PHOTO SAMPLE STATUS")

        self.student_table["show"] = "headings"

        self.student_table.column("branch",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("enrollment number",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("contact",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("date of birth",width=100)
        self.student_table.column("hostel status",width=100)
        self.student_table.column("photo",width=100)

        
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

    #functions
    def add_data(self):
        if self.var_bra.get()=="SELECT BRANCH" or self.var_name.get()=="" or self.var_enroll_num.get()=="":
            messagebox.showerror("ERROR","All Fields Are Required")
        else:
            try:
                #store data in database
                conn=mysql.connector.connect(host="localhost",username="root",password="honey@2005",database="facerecog")
                #create cursour
                my_cursor=conn.cursor()
                #exexute query using cursor
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.var_bra.get(),
                self.var_name.get(),self.var_enroll_num.get(),self.var_year.get(),self.var_sem.get(),self.var_gender.get(),
                self.var_contact.get(),self.var_email.get(),self.var_dob.get(),self.var_hostel.get(),self.var_radio1.get()
                ))
                conn.commit()#data update hota rahe
                self.fetch_data()
                conn.close
                messagebox.showinfo("SUCESS","Student details added sucessfully!!!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)

    
    #----fetch data in student detail window----#
    def fetch_data(self):
        #store data in database
                conn=mysql.connector.connect(host="localhost",username="root",password="honey@2005",database="facerecog")
                #create cursour
                my_cursor=conn.cursor()
                #select query from database-->table
                my_cursor.execute("select * from student")
                #fetch
                data=my_cursor.fetchall()

                if len(data)>0:
                     self.student_table.delete(*self.student_table.get_children())
                     for i in data:
                          self.student_table.insert("",END,values=i)
                     conn.commit()
                     conn.close()
                conn.close()
    #=======get cursor--> for updation========#
    def get_cursor(self,event=""): #event,""-->bind with table
         cursor_focus=self.student_table.focus()
         content=self.student_table.item(cursor_focus)
         data=content["values"]

         self.var_bra.set(data[0])
         self.var_name.set(data[1])
         var_enrollNum = self.var_enroll_num.set(data[2])
         self.var_year.set(data[3])
         self.var_sem.set(data[4])
         self.var_gender.set(data[5])
         self.var_contact.set(data[6])
         self.var_email.set(data[7])
         self.var_dob.set(data[8])
         self.var_hostel.set(data[9])
         self.var_radio1.set(data[10])

    #update--------function-------------#
    def update_data(self):
         if self.var_bra.get()=="Select Branch" or self.var_name.get()=="" or self.var_enroll_num.get()=="":
            messagebox.showerror("ERROR","All Fields Are Required",parent=self.root)
         else:
            
            try:
                
                Update=messagebox.askyesno("UPDATE","Do you wnat to update student details",parent=self.root)
                if Update!=0:
                   #connextion creation
                    conn=mysql.connector.connect(host="localhost",username="root",password="honey@2005",database="facerecog")
                #create cursour         
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set branch=%s,Enroll_Num=%s,Year=%s,Semester=%s,gender=%s,contact=%s,email=%s,hostel_status=%s,dob=%s,Photo_Sample=%s where Name=%s",
                                    (self.var_bra.get(),self.var_enroll_num.get(),self.var_year.get(),self.var_sem.get(),
                                    self.var_gender.get(),self.var_contact.get(),self.var_email.get(),self.var_dob.get(),self.var_hostel.get(),self.var_radio1.get(),self.var_name.get()))
            

                else:
                   if not Update:
                        return
                   
                conn.commit()
                self.fetch_data() #in every updation --> data must be fetched!!!
                conn.close()
                messagebox.showinfo("SUCESS","studetn details sucessfully updated!!!",parent=self.root)
            except Exception as es:
                 messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
    
    #delete data

    def delete_data(self):
         
         if self.var_enroll_num.get()=="":
              messagebox.showerror("Error","student id is required",parent=self.root)
         else:
              try:
                   delete=messagebox.askyesno("Delete Data","Do you want to delete Student",parent = self.root)
                   if delete != 0:
                         conn=mysql.connector.connect(host="localhost",username="root",password="honey@2005",database="facerecog")
                #create cursour         
                         my_cursor=conn.cursor()
                         sql="delete from student where Enroll_Num = %s"
                         val = (self.var_enroll_num.get(),)
                         my_cursor.execute(sql,val)
                   else:
                        if not delete:
                             return
                   conn.commit()
                   self.fetch_data()
                   conn.close()
                   messagebox.showinfo("Sucess","student details deleted sucessfully!!!",parent=self.root)

              except Exception as es:
                   messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

     #reset data
    def reset_data(self):
         
         self.var_bra.set("Select Branch")
         self.var_name.set("")
         self.var_enroll_num.set("")
         self.var_year.set("Select Year")
         self.var_sem.set("Select Semester")
         self.var_gender.set("")
         self.var_contact.set("")
         self.var_email.set("")
         self.var_dob.set("")
         self.var_hostel.set("")
         self.var_radio1.set("")

     #========== TAKE PHOTO SAMPLES ===========# MATCH FROM DATABASE

    def generateDataSet(self):
         
         if self.var_bra.get()=="Select Branch" or self.var_name.get()=="" or self.var_enroll_num.get()=="":
            messagebox.showerror("ERROR","All Fields Are Required",parent=self.root)
         else:
            
            try:
                   #connextion creation
                    conn=mysql.connector.connect(host="localhost",username="root",password="honey@2005",database="facerecog")
                #create cursour         
                    my_cursor=conn.cursor()
                    my_cursor.execute("select * from student")#execute select * query
                    res = my_cursor.fetchall()
                    id=0 # match id
                    for i in res:
                         id += 1
                    #update query...
                    my_cursor.execute("update student set branch=%s,Name=%s,Year=%s,Semester=%s,gender=%s,contact=%s,email=%s,hostel_status=%s,dob=%s,Photo_Sample=%s where Enroll_Num=%s",
                                    (self.var_bra.get(),self.var_name.get(),self.var_year.get(),self.var_sem.get(),self.var_gender.get(),self.var_contact.get(),self.var_email.get(),self.var_hostel.get(),self.var_dob.get(),self.var_radio1.get(),self.var_enroll_num.get()==id+1))

                    conn.commit() #update connection
                    self.fetch_data() # fetch data
                    self.reset_data()
                    conn.close()
               
                    #Harr Cascades Algo --> ML algorithm --> frontal face + eyes

                    face_clsf = cv2.CascadeClassifier("haarcascade_frontalface_default.xml") #object detection

                    def face_crop(img):
                         gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #bgr --> geay scale...
                         faces = face_clsf.detectMultiScale(gray,1.3,5)
                         #scaling factor -> 1.3
                         #min neighbour -> 5

                         #we want a rectangle in face detection

                         for (x,y,w,h) in faces:
                              face_crop = img[y:y+h , x:x+w]
                              #face is now cropped
                              return face_crop

                    #now open camera!!!
                    capture = cv2.VideoCapture(0)

                    img_id = 0
                    while True:
                         ret,_frame = capture.read()
                         if face_crop(_frame) is not None:
                              img_id = img_id + 1
                              face = cv2.resize(face_crop(_frame),(450,450)) #size --> 500 * 500
                              face = cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                              file_path = "data/user."+str(id)+"."+str(img_id)+".jpg"
                              cv2.imwrite(file_path,face)
                              cv2.putText(face,str(img_id),(45,45),cv2.FONT_HERSHEY_PLAIN,2,(100,100,100),2)
                              cv2.imshow("FACE",face)

                         if cv2.waitKey(1)==13 or img_id>=50:
                              break

                    capture.release()
                    cv2.destroyAllWindows()
                    messagebox.showinfo("SUCESS","Data Set is sucessfully generated!!!")

            except Exception as es:
                 messagebox.showerror("Error",f"Due To : {str(es)}",parent=self.root)
     
              
                 


if __name__ == "__main__":
   
    root = Tk() #call root from tool kit

    obj = student(root)

     #  root['bg'] = '#69698B'

    root.mainloop() 