from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from student import student
import os
from traindata import train 
from face_recog import face_recognition
from attendence import Attendence
from help_devloper import Devloper

class face_recognition_system:

    def __init__(self , root):

        self.root = root
        #now set geometry of the window
        self.root.geometry("1530x790+0+0")
        #set title
        self.root.title("Face Recognition System")

        #img --> 1
        img = Image.open(r"C:\face_recognition_system\images\img1.jpg")

        #set size
        img = img.resize((550,300),Image.ADAPTIVE)

        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root , image = self.photoimg)

        f_lbl.place(x=0 , y=0 , width = 550 , height = 300)

        #img --> 2

        img1 = Image.open(r"C:\face_recognition_system\images\img3.jpg")

        #set size
        img1 = img1.resize((550,300),Image.ADAPTIVE)

        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root , image = self.photoimg1)

        f_lbl.place(x=550 , y=0 , width = 550 , height = 300)
        
        #img --> 3

        img2 = Image.open(r"C:\face_recognition_system\images\img4.jpg")

        #set size
        img2 = img2.resize((550,300),Image.ADAPTIVE)

        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root , image = self.photoimg2)

        f_lbl.place(x=1100 , y=0 , width = 550 , height = 300)
        
        #bg-color

        img3 = Image.open(r"C:\face_recognition_system\images\bgColor.jpg")

        #set size
        img3 = img3.resize((1530,710),Image.ADAPTIVE)

        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root , image = self.photoimg3)

        bg_img.place(x=0 , y=300 , width = 1530 , height = 710)

        title_lbl = Label(bg_img , text = "SMART   ATTENDANCE   SYSTEM",font=("times new roman",35,"bold"), bg="blue",fg="white")

        title_lbl.place(x=0 , y=0,width=1530,height=45)

        #buttons-STUDENT
          
        img4 = Image.open(r"C:\face_recognition_system\images\stud_BUTTON.jpg")

        #set size
        img4 = img4.resize((200,200),Image.ADAPTIVE)

        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1 = Button(bg_img,image=self.photoimg4 ,command=self.student_details, cursor = "hand2")

        b1.place(x=0,y=100,width=200,height=200)

        #button down

        b2 = Button(bg_img,text = "STUDENT DETAILS" ,command=self.student_details, cursor = "hand2" , font=("times new roman",15,"bold"), bg="dark blue",fg="white")

        b2.place(x=0,y=300,width=200,height=40)

        #buttons- FACE - DETECTION
          
        img5 = Image.open(r"C:\face_recognition_system\images\button_FACE_DETECTION.jpg")

        #set size
        img5 = img5.resize((200,200),Image.ADAPTIVE)

        self.photoimg5 = ImageTk.PhotoImage(img5)

        b3 = Button(bg_img,image=self.photoimg5 ,command = self.recog_face, cursor = "hand2")

        b3.place(x=220,y=100,width=200,height=200)

        #button down

        b4 = Button(bg_img,text = "FACE DETECTOR" , cursor = "hand2" ,command = self.recog_face, font=("times new roman",15,"bold"), bg="dark blue",fg="white")

        b4.place(x=220,y=300,width=200,height=40)
        

        #buttons- ATTENDANCE
          
        img6 = Image.open(r"C:\face_recognition_system\images\button_ATTENDANCE.jpg")

        #set size
        img6 = img6.resize((200,200),Image.ADAPTIVE)

        self.photoimg6 = ImageTk.PhotoImage(img6)

        b5 = Button(bg_img,image=self.photoimg6 ,command=self.attendence, cursor = "hand2")

        b5.place(x=440,y=100,width=200,height=200)

        #button down

        b6 = Button(bg_img,text = "ATTENDANCE" ,command=self.attendence, cursor = "hand2" , font=("times new roman",15,"bold"), bg="dark blue",fg="white")

        b6.place(x=440,y=300,width=200,height=40)
        

        #buttons- TRAIN DATA
          
        img7 = Image.open(r"C:\face_recognition_system\images\button_TRAINDATA.jpg")

        #set size
        img7 = img7.resize((200,200),Image.ADAPTIVE)

        self.photoimg7 = ImageTk.PhotoImage(img7)

        b7 = Button(bg_img,image=self.photoimg7 ,command=self.train_data, cursor = "hand2")

        b7.place(x=660,y=100,width=200,height=200)

        #button down

        b8 = Button(bg_img,text = "TRAIN DATA" , cursor = "hand2" ,command=self.train_data, font=("times new roman",15,"bold"), bg="dark blue",fg="white")

        b8.place(x=660,y=300,width=200,height=40)
        

        #buttons- PHOTOS
          
        img8 = Image.open(r"C:\face_recognition_system\images\button_PHOTOS.jpg")

        #set size
        img8 = img8.resize((200,200),Image.ADAPTIVE)

        self.photoimg8 = ImageTk.PhotoImage(img8)

        b9 = Button(bg_img,image=self.photoimg8 , command = self.open_photos , cursor = "hand2")

        b9.place(x=880,y=100,width=200,height=200)

        #button down

        b10 = Button(bg_img,text = "PHOTOS" , command = self.open_photos , cursor = "hand2" , font=("times new roman",15,"bold"), bg="dark blue",fg="white")

        b10.place(x=880,y=300,width=200,height=40)
        
        
        #buttons- HELP DESK AND DEVLOPER
          
        img9 = Image.open(r"C:\face_recognition_system\images\button_DEVLOPER.jpg")

        #set size
        img9 = img9.resize((200,200),Image.ADAPTIVE)

        self.photoimg9 = ImageTk.PhotoImage(img9)

        b11 = Button(bg_img,image=self.photoimg9 ,command=self.devloper, cursor = "hand2")

        b11.place(x=1100,y=100,width=200,height=200)

        #button down

        b12 = Button(bg_img,text = "HELP / DEVLOPER" ,command=self.devloper, cursor = "hand2" , font=("times new roman",15,"bold"), bg="dark blue",fg="white")

        b12.place(x=1100,y=300,width=200,height=40)

        #buttons- EXIT APPLICATION
          
        img10 = Image.open(r"C:\face_recognition_system\images\button_EXIT.jpg")

        #set size
        img10 = img10.resize((200,200),Image.ADAPTIVE)

        self.photoimg10 = ImageTk.PhotoImage(img10)

        b13 = Button(bg_img,image=self.photoimg10 ,command=root.quit, cursor = "hand2")

        b13.place(x=1320,y=100,width=200,height=200)

        #button down

        b14 = Button(bg_img,text = " EXIT " , command=root.quit ,cursor = "hand2" , font=("times new roman",15,"bold"), bg="dark blue",fg="white")

        b14.place(x=1320,y=300,width=200,height=40)

        #============== Functions =================#

    def student_details(self):
        #new window open on clicking a abutton!!!
        self.new_window=Toplevel(self.root)
        self.app=student(self.new_window)
    def open_photos(self):
        os.startfile("data")
    
    def train_data(self):
        #new window open on clicking a abutton!!!
        self.new_window=Toplevel(self.root)
        self.app=train(self.new_window)
    
    def recog_face(self):
        #new window open on clicking a abutton!!!
        self.new_window=Toplevel(self.root)
        self.app= face_recognition(self.new_window)
    
    def attendence(self):
        #new window open on clicking a abutton!!!
        self.new_window=Toplevel(self.root)
        self.app= Attendence(self.new_window)

    def devloper(self):

        self.new_window=Toplevel(self.root)
        self.dev = Devloper(self.new_window)


      
    
    

        

if __name__ == "__main__":

    root = Tk() #call root from tool kit

    obj = face_recognition_system(root)

   # root['bg'] = '#69698B'

    

    root.mainloop()





































