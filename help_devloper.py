from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as npy


class Devloper:

    def __init__(self , root):

        self.root = root
        #now set geometry of the window
        self.root.geometry("1530x790+0+0")

        self.root.background = 'blue'
        #set title
        self.root.title("ABOUT DEVLOPER and HELP Page")

        title_lbl = Label(self.root , text = "HELP and DEVLOPER",font=("times new roman",30,"bold"), bg="blue",fg="white")
        title_lbl.place(x=0 , y=0,width=1530,height=45)

        Left_frame = LabelFrame(self.root,bd=1,bg="light blue",relief="sunken",text="HELP DESK",font=("times new roman",20,"bold"))

        Left_frame.place(x=0 , y=45 , width=750 , height=740)

        devloper1_lbl = Label(Left_frame , text = "CONTACT : 8219831134\n\nEMAIL : harshitkishtwal@gmail.com\n\nLinkedIn : Kishtwal_Harshit",font=("times new roman",20,"bold"), bg="light blue",fg="blue")
        devloper1_lbl.place(x=-150, y=50,width=1000,height=500)
        
        Right_frame = LabelFrame(self.root,bd=1,bg="light pink",relief="sunken",text="DEVLOPER",font=("times new roman",20,"bold"))

        Right_frame.place(x=750,y=45,width=780,height=740)

        img2 = Image.open(r"C:\face_recognition_system\images\devloper_1.jpg")

        
        img2 = img2.resize((300,300),Image.ADAPTIVE)

        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root , image = self.photoimg2)

        f_lbl.place(x=990 , y=100 , width = 300 , height = 300)

        devloper_lbl = Label(Right_frame , text = "Hi there, I am Harshit Kishtwal",font=("times new roman",20,"bold"), bg="light pink",fg="red")
        devloper_lbl.place(x=-100 , y=350,width=1000,height=45)

        devloper1_lbl = Label(Right_frame , text = "I have keen intrest in software domain and I love working\non new technologies",font=("times new roman",20,"bold"), bg="light pink",fg="red")
        devloper1_lbl.place(x=-100 , y=400,width=1000,height=70)








        



if __name__ == "__main__":

    root = Tk()
    obj = Devloper(root)
    root.mainloop()
