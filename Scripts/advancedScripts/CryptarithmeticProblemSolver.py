#---------------Importing Modules-----------------------------------------------------

import itertools
from tkinter import *
import tkinter as tk

#-------------------------------------------------------------------------------------

#-----------------Window Design-------------------------------------------------------

window=tk.Tk()
window.title('Crypt-Arithmetic Problem Solver')
window.geometry('700x1000')
window.maxsize(700,1000)
window.minsize(700,1000)

#--------------------------------------------------------------------------------------

def get_value(word, substitution):
    s = 0
    factor = 1
    for letter in reversed(word):
        s += factor * substitution[letter]
        factor *= 10
    return s


def solve2(equation):
    #Getting equation value
    equation=Eq.get()
    # split equation in left and right
    left, right = equation.lower().replace(' ', '').split('=')
    # split words in left part
    left = left.split('+')
    # create list of used letters
    letters = set(right)
    for word in left:
        for letter in word:
            letters.add(letter)
    letters = list(letters)

    digits = range(10)
    for perm in itertools.permutations(digits, len(letters)):
        sol = dict(zip(letters, perm))

        if sum(get_value(word, sol) for word in left) == get_value(right, sol):
            print(' + '.join(str(get_value(word, sol)) for word in left) + " = {} (mapping: {})".format(get_value(right, sol), sol))

#-------------------------Window Functions-------------------------------------------------------------------------------------------------

head=Label(window, text='Problem Solver', fg='white', bg='black',font='Times 20').place(x=270,y=20)
Eq=StringVar()
Label(window,text="Enter the Crypt Equation (A + B = C) :",fg="white",bg="black").place(x=200,y=80)
eq_entry=Entry(window,textvariable=Eq).place(x=420,y=80)
Button(window,text="Submit",fg="white",bg="black",command=solve2).place(x=330,y=120)

#------------------------------------------------------------------------------------------------------------------------------------------
