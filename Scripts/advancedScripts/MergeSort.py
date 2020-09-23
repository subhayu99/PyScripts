#Imporing Tkinter modules--------------------------------------------------------
from tkinter import *
import tkinter as tk
#--------------------------------------------------------------------------------

#Building window-----------------------------------------------------------------
window=tk.Tk()
window.title("GUI Sorting")
window.geometry("300x300")
window.maxsize(300,300)
window.minsize(300,300)
#---------------------------------------------------------------------------------


def ascending():                        #Funtion to sort in Ascending order
        str_arr=array.get()
        a_lst=str_arr.split(',')
        map_object = map(int, a_lst)
        lst = list(map_object)
        for i in range(len(lst)):
                minval=i
                for j in range(i+1,len(lst)):
                    if lst[j]<lst[minval]:
                        minval=j
                lst[i], lst[minval] = lst[minval], lst[i]

        #Labels for displaying the List and the Order of sorting
        Label(window,text="Sorted in Ascending Order: ").place(x=20,y=170)
        Label(window,text=lst).place(x=190,y=170)
        

def descending():                       #Funtion to sort in Descending order
        str_arr=array.get()
        a_lst=str_arr.split(',')
        map_object = map(int, a_lst)
        lst = list(map_object)
        for i in range(len(lst)):
                maxval=i
                for j in range(i+1,len(lst)):
                    if lst[j]>lst[maxval]:
                        maxval=j
                lst[i], lst[maxval] = lst[maxval], lst[i]

        #Labels for displaying the List and the Order of sorting
        Label(window,text="Sorted in Descending Order: ").place(x=20,y=170)
        Label(window,text=lst).place(x=190,y=170)


#GUI Labels and Buttons--------------------------------------------------------------------

#String value to take the array input as string
array=StringVar()

head=Label(window,text="Merge Sort",fg="black", font="Times 20")
head.place(x=90,y=10)

Label(window,text="Enter your array: ",fg="black").place(x=30,y=80)
array_entry=Entry(window,textvariable=array)
array_entry.place(x=150,y=80)

Button(window, text="Ascending", bg="black",fg="white",command=ascending).place(x=20,y=120)
Button(window, text="Descending", bg="black",fg="white",command=descending).place(x=190,y=120)
#---------------------------------------------------------------------------------------------
