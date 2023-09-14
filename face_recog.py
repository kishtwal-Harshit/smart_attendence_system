from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as npy
import student
from time import strftime
from datetime import datetime

class face_recognition:

    def __init__(self , root):

        self.root = root
        #now set geometry of the window
        self.root.geometry("1530x790+0+0")
        #set title
        self.root.title("FACE RECOGNITION SYSTEM")

        title_lbl = Label(self.root , text = "FACE RECOGNITION",font=("times new roman",35,"bold"), bg="dark blue",fg="yellow")

        title_lbl.place(x=0 , y=0,width=1530,height=45)

        img = Image.open(r"C:\face_recognition_system\images\img8.jpg")

        #set size
        img = img.resize((830,720),Image.ADAPTIVE)

        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root , image = self.photoimg)

        f_lbl.place(x=0 , y=55 , width = 830 , height = 720)

        #img --> 2

        img1 = Image.open(r"C:\face_recognition_system\images\img9.jpg")

        #set size
        img1 = img1.resize((830,720),Image.ADAPTIVE)

        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root , image = self.photoimg1)

        f_lbl.place(x=700 , y=55 , width = 830 , height = 720)

        img4 = Image.open(r"C:\face_recognition_system\images\img10.jpg")

        #set size
        img4 = img4.resize((300,300),Image.ADAPTIVE)

        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1 = Button(self.root,command=self.face_recogN,image=self.photoimg4 ,cursor = "hand2")

        b1.place(x=790,y=250,width=300,height=250)

        #button down

        b2 = Button(self.root,text = "FACE RECOGNIZE",command=self.face_recogN,cursor = "hand2" , font=("times new roman",15,"bold"), bg="dark blue",fg="white")

        b2.place(x=790,y=500,width=300,height=50)

    #-------attendence at backend--------#

    def attendence(self,b,n,y,s,enrm):
        with open("attendence.csv","r+",newline="\n") as f:
            myData = f.readlines()
            nameLis=[]
            for line in myData:
                entry=line.split((","))
                nameLis.append(entry[0])

                #----make sure that no repetition is there----#
            if((enrm not in nameLis) and (b not in nameLis) and (n not in nameLis) and (y not in nameLis) and (s not in nameLis)):
                
                #now mark attendence#

                now = datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString = now.strftime("%H:%M:%S")
                f.writelines(f"\n{enrm},{n},{b},{y},{s},{dtString},{d1},PRESENT")

            


    #---------face recognition-----------#
    
    def face_recogN(self):
        
        def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            #convert to gray scale
            gray_image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)
            #coord list

        
            coord=[]
            for(x,y,w,h) in features:
                #cv2.rectangle(img,(400,400),(100,100),(255,0,0),5)
                cv2.rectangle(img,(x,y),(x+w,y+h),(155,48,255),5)
                id,predict = clf.predict(gray_image[y:y+h,x:x+w])
                
                #calculate confidence value to check for img accuracy matching

                confidence = int((100*(1-predict/300)))

                conn=mysql.connector.connect(host="localhost",username="root",password="honey@2005",database="facerecog")
                #create cursour
                my_cursor=conn.cursor()
                    #query
                my_cursor.execute("select branch from student where Enroll_Num="+str(id))
                b = my_cursor.fetchone()
                b=" ".join(b)
                    
                my_cursor.execute("select Name from student where Enroll_Num="+str(id))
                n = my_cursor.fetchone()
                n=" ".join(n)

                my_cursor.execute("select Year from student where Enroll_Num="+str(id))
                y = my_cursor.fetchone()
                y = " ".join(y)
                
                    
                my_cursor.execute("select Semester from student where Enroll_Num="+str(id))
                s = my_cursor.fetchone()
                s = " ".join(s)

                my_cursor.execute("select Enroll_Num from student where Enroll_Num="+str(id))
                enrm = my_cursor.fetchone()
                enrm = " ".join(enrm)
                
                #idd=1
                #my_cursor.execute("select Name from student where Enroll_Num="+str(idd))
                #nms = my_cursor.fetchall()
                #print(nms)

                if confidence > 87:
                    #put texts
                    #print(id)
                    cv2.putText(img,f"Semester:{s}",(70,300),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,0,0),2)
                    cv2.putText(img,f"Enrollment ID:{enrm}",(70,250),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,0,0),2)
                    cv2.putText(img,f"Year:{y}",(70,200),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,0,0),2)
                    cv2.putText(img,f"Name:{n}",(70,150),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,0,0),2)
                    cv2.putText(img,f"Branch:{b}",(70,100),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,0,0),2)
                                        
                    cv2.putText(img,f"FACE RECOGNIZED-Attendence Marked",(100,50),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,0,0),2)
                    self.attendence(b,n,y,s,enrm)
                
                else:
                    #unknown_face!!!
                    
                    cv2.putText(img,f"UNKNOWN FACE",(300,100),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,0,255),2)
                
                coord = [x,y,w,h]

            return coord
        
        def recognize(img,clf,faceCascade):
            coord=draw_boundary(img,faceCascade,1.1,10,(255,255,255),"Face",clf)
            return img

        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        #read the classifier

        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)

        while True:
            #read images
            res,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("FACE RECOG",img)

            if cv2.waitKey(1) == 13:
                break
        video_cap.release()
        cv2.destroyAllWindows()
    
    def trial(self):

        conn=mysql.connector.connect(host="localhost",username="root",password="honey@2005",database="facerecog")
                #create cursour
        my_cursor=conn.cursor()

        nme = my_cursor.execute("select Name from student")

        print(nme)



if __name__ == "__main__":
   
    root = Tk() #call root from tool kit

    obj = face_recognition(root)

     #  root['bg'] = '#69698B'

    root.mainloop() 
