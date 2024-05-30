import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from datetime import datetime, date
import calendar
import os
import sys
import sqlite3
import re
import copyPaste
from tkcalendar import Calendar, DateEntry



# ------------------------------------------------------------------------------------------------------#
root = Tk()

# Define screen width and height
ws = root.winfo_screenwidth() / 3
hs = root.winfo_screenheight() / 4

# Define window width and height
w = 300
h = 500
# ------------------------------------------------------------------------------------------------------#

# ------------------------------------------------------------------------------------------------------#
# Create root Window
top = Toplevel()
top.title('New-Hire')
# Opens a window with dimension of 300x450 at screen coordinate of 300, 200
top.geometry('%dx%d+%d+%d' % (w, h, ws, hs))
# Prevents the user from resizing the window
top.resizable(False, False)
# Login window will always be the top window
top.attributes("-topmost", True)

submit_btn = Button(top, text="Submit", command=lambda:overwrite())
quit_btn = Button(top, text="Quit", command=lambda:quit())

# ------------------------------------------------------------------------------------------------------#

def overwrite():
    name = getInput()
    first_last = getFirstLast(name)
    setText(first_last)


def getInput():

    #   Splits the entered name into a list
    full_name = new_hire_name.get().lower().split()
    
    #   Checks if each entry in the list is only alphetical.
    #   Recusrion if any of the list entry is not a valid input, and clear fields.
    for str in full_name:
        if str.isalpha() == True:
            continue 
        else:
            clearText()
            getInput()

    return full_name


#   Retrieves only the first and last name from the 
def getFirstLast(full_name):
    
    list_size = len(full_name)

    # Creates array of first name and last name
    first_name = full_name[0]
    last_name = full_name[list_size - 1]
    
    global params
    params = [first_name, last_name]
    return params

#   
def setText(text):
    # Name: John Apple
    # result: john.apple@douglasemmett.com
    varOne = copyPaste.firstLast(text)

    # Name: John Apple
    # result: john.apple
    varTwo = copyPaste.firstLastNoEmail(text)
    
    #   Takes in the selected date from tkcalendar app
    #   returns string of 'mmdd'
    #   ex: May 2nd turns into 0502
    varThree = copyPaste.temp_password(cal)

    email.delete(0, END)
    email.insert(0, varOne)

    simplefied.delete(0, END)
    simplefied.insert(0, varTwo)

    temp_pass.delete(0, END)
    temp_pass.insert(0, varThree)


#   Clears Entry fields.
def clearText():
    email.delete(0, END)

    simplefied.delete(0, END)

    temp_pass.delete(0, END)


# ------------------------------------------------------------------------------------------------------#
#   Defines fields for elements to be used for the GUI.

new_hire_label = Label(top, text="Name")
new_hire_name = Entry(top) 

cal_label = Label(top, text="Start Date")
cal = DateEntry(top, width=12, background='darkblue',
                    foreground='white', borderwidth=2)

email_label = Label(top, text="Email")
email = Entry(top)

simplefied_label = Label(top, text="Simple")
simplefied = Entry(top)

temp_pass_label = Label(top, text="Temp PW")
temp_pass = Entry(top)


# ------------------------------------------------------------------------------------------------------#
#   Puts defined fields into a grid.

new_hire_label.grid(row=1, column=0, sticky='w')
new_hire_name.grid(row=1, column=1,padx= 10, pady=5, columnspan=10)


cal_label.grid(row=2, column=0, sticky='w')
cal.grid(row=2, column=1, pady=2, columnspan=5)

simplefied_label.grid(row=3, column=0, sticky='w')
simplefied.grid(row=3, column=1,padx= 10, pady=5, columnspan=10)

email_label.grid(row=4, column=0, sticky='w')
email.grid(row=4, column=1,padx= 10, pady=5, columnspan=10)

temp_pass_label.grid(row=5, column=0, sticky='w')
temp_pass.grid(row=5, column=1,padx= 10, pady=5, columnspan=10)


submit_btn.grid(row=12, column=1)
quit_btn.grid(row=12, column=2)


# ------------------------------------------------------------------------------------------------------#

def quit():
    top.destroy()
    root.destroy()
    sys.exit()

# withdraw() hides the installer window. It's manifested but just cannot be seen.
root.withdraw()


root.mainloop()