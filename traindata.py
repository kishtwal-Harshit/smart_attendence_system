from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as npy


class train:

    def __init__(self , root):

        self.root = root
        #now set geometry of the window
        self.root.geometry("1530x790+0+0")

        self.root.background = 'blue'
        #set title
        self.root.title("TRAIN DATA")

        title_lbl = Label(self.root , text = "TRAIN DATA SET",font=("times new roman",35,"bold"), bg="blue",fg="white")

        title_lbl.place(x=0 , y=0,width=1530,height=45)

                #img --> 1
        img = Image.open(r"C:\face_recognition_system\images\img1.jpg")

        #set size
        img = img.resize((550,300),Image.ADAPTIVE)

        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root , image = self.photoimg)

        f_lbl.place(x=0 , y=50 , width = 550 , height = 300)

        #img --> 2

        img1 = Image.open(r"C:\face_recognition_system\images\img3.jpg")

        #set size
        img1 = img1.resize((550,300),Image.ADAPTIVE)

        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root , image = self.photoimg1)

        f_lbl.place(x=550 , y=50 , width = 550 , height = 300)
        
        #img --> 3

        img2 = Image.open(r"C:\face_recognition_system\images\img4.jpg")

        #set size
        img2 = img2.resize((550,300),Image.ADAPTIVE)

        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root , image = self.photoimg2)

        f_lbl.place(x=1100 , y=50 , width = 550 , height = 300)
        
        #bg-color

        img3 = Image.open(r"C:\face_recognition_system\images\bgColor.jpg")

        #set size
        img3 = img3.resize((1530,710),Image.ADAPTIVE)

        self.photoimg3 = ImageTk.PhotoImage(img3)

        img4 = Image.open(r"C:\face_recognition_system\images\ml.jpg")

        #set size
        img4 = img4.resize((300,300),Image.ADAPTIVE)

        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1 = Button(self.root,image=self.photoimg4 , command=self.train_clsf,cursor = "hand2")

        b1.place(x=600,y=400,width=300,height=250)

        #button down

        b2 = Button(self.root,text = "TRAIN DATA ",command=self.train_clsf, cursor = "hand2" , font=("times new roman",15,"bold"), bg="dark blue",fg="white")

        b2.place(x=600,y=600,width=300,height=50)

    def train_clsf(self):

        data_directory = ("data")
        path = [os.path.join(data_directory,file) for file in os.listdir(data_directory)]#list comprehension

        faces=[]
        ids=[]

        for image in path:

            img = Image.open(image).convert('L')
            #convert image to grid --> numpy array

            imageNpy = npy.array(img,'uint8')
            id = int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNpy)
            ids.append(id)
            cv2.imshow("TRAINING",imageNpy)
            cv2.waitKey(1) == 13
        
        ids = npy.array(ids) #ids ko numpy me convert karo!!!

        # train the clsf #
        recognizer = cv2.face.LBPHFaceRecognizer_create()

        recognizer.train(faces,ids)
        recognizer.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("SUCESS","Dataset Training Completed!!!")




















if __name__ == "__main__":

    root = Tk()
    obj = train(root)
    root.mainloop()

    
