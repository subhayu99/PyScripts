##import the modules
import cv2
from tkinter import *
import tkinter as tk
#-------------------------------------------------

win=tk.Tk()                 #Designing window outline
win.title('Image Cropper')
win.geometry('800x700')

def crop() #Cropping Funcction
    img = cv2.imread("Sample.jpg") ##read your image 
    y = 0  #HEIGHT for cropping
    x = 0  #WIDTH for cropping
    Height = height.get() #Getting values from height
    Width = width.get() #Getting values from width
    crop_image = img[x:Width, y:Height]
    imageLabel.config(image=cv2.imshow("Cropped", crop_image)) ##display Cropped image
    cv2.waitKey(0)


head=Label(win,text="Python Image Cropper", fg="black", font="times 20")
head.place(x=280,y=10)

height=IntVar()     #Tkinter variable to store height
width=IntVar()      #Tkinter variable to store width

Label(win,text="Height:", fg="black",font="times 12").place(x=250,y=100)
h=Entry(win,textvariable=height)
h.place(x=300,y=100)

Label(win,text="Width:", fg="black",font="times 12").place(x=400,y=100)
w=Entry(win,textvariable=width)
w.place(x=450,y=100)

imageLabel=Label(win)
imageLabel.place(x=300,y=250)

Button(win, text="Submit", bg="black", fg="white", font="times 12", command=crop).place(x=370,y=170)
