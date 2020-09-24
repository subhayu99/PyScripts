#Importing modules----------------------------------------------------------------------------

import random
from tkinter import *
from PIL import ImageTk, Image #pip install pillow
import tkinter as tk

#---------------------------------------------------------------------------------------------

#Window design -------------------------------------------------------------------------------

window=tk.Tk()
window.title('Guessing Game')
window.geometry('500x500')
window.maxsize(500,500)
window.minsize(500,500)

#---------------------------------------------------------------------------------------------

#Checking function----------------------------------------------------------------------------

def start():
    limit=Limit.get()
    chances=Chances.get()
    guess=Guess.get()    
    number = random.randint(1, limit)
    win = False
    while chances > 0:
        if guess == number:
            Label(window,text="Hooray, You Won!!",font="TImes 16").place(x=220,y=250)
            img_won = ImageTk.PhotoImage(Image.open('won.png'))
            label_won = Label(image=img_won)
            label_won.place(x=230,y=280)
            win = True
            break
        elif guess < number:
            Label(window,text="Your Guess is Low!!",font="TImes 16").place(x=220,y=250)
            img_think1 = ImageTk.PhotoImage(Image.open('think.png'))
            label_think1 = Label(image=img_think1)
            label_think1.place(x=230,y=280)
            
        else:
            Label(window,text="Your Guess is High!!",font="TImes 16").place(x=220,y=250)
            img_think2 = ImageTk.PhotoImage(Image.open('think.png'))
            label_think2 = Label(image=img_think2)
            label_think2.place(x=230,y=280)
        
        chances -= 1

    if win is not True:
        Label(window,text="You Lost the Game!!",font="TImes 16").place(x=220,y=250)
        img_lost = ImageTk.PhotoImage(Image.open('loose.png'))
        label_lost = Label(image=img_lost)
        label_lost.place(x=230,y=280)

#---------------------------------------------------------------------------------------------------

#Function-------------------------------------------------------------------------------------------


head=Label(window, text='Guessing Game', bg='black', fg='white',font="Times 20").place(x=170,y=20)
Limit=IntVar()
Chances=IntVar()
Guess=IntVar()

Label(window,text="Enter your Limit:",bg='black', fg='white').place(x=140,y=100)
entry_lim=Entry(window,textvariable=Limit)
entry_lim.place(x=250,y=100)

Label(window,text="Enter no. of Chances:",bg='black', fg='white').place(x=130,y=140)
entry_ch=Entry(window,textvariable=Chances)
entry_ch.place(x=260,y=140)

Button(window,text="Submit",bg='black', fg='white',command=start).place(x=220,y=220)

Label(window,text="Enter your guess:",bg='black',fg='white').place(x=140,y=180)
entry_guess=Entry(window,textvariable=Guess)
entry_guess.place(x=250,y=180)

#---------------------------------------------------------------------------------------------------
