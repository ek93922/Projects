import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from datetime import datetime
import os
import sys
import sqlite3
import re



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
# Create Login Window
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

def overwrite():
    first_last = getInput()
    setText(first_last)

def getInput():
    # Gets entered name and keeps alphanumeric and space 
    full_name = re.sub(r'[^A-Za-z0-9 ]+', '', new_hire_name.get().lower())

    # Creates array of first name and last name
    first_name = full_name.strip().split()[0]
    last_name = full_name.strip().split()[1]
    
    global params
    params = [first_name, last_name]
    return params

def setText(text):
    varOne = firstLast(text)
    varTwo = firstIniLastIni(text)
    varThree = firstIniLast(text)

    gmail.delete(0, END)
    gmail.insert(0, varOne)

    quickbase.delete(0, END)
    quickbase.insert(0, varTwo)

    mri.delete(0, END)
    mri.insert(0, varThree)


def firstLast(params):
    # Name: John Apple
    # result: john.apple@douglasemmett.com
    # Used for:
    # Gmail / Quickbase / Zego
    variant_one = params[0] + "." + params[1] + "@douglasemmett.com"
    return variant_one

def firstIniLastIni(params):
    # Name: John Apple
    # result: ja@douglasemmett.com
    variant_two = params[0][:1] + params[1][:1] + "@douglasemmett.com"
    return variant_two

def firstIniLast(params):
    # Name: John Apple
    # result: japple@douglasemmett.com
    variant_three = params[0][:1] + params[1] + "@douglasemmett.com"
    return variant_three

def firstLastNoEmail(params):
    # Name: John Apple
    # result: john.apple
    variant_four = params[0] + "." + params[1]
    return variant_four

def firstIniLastNoEmail(params):
    # Name: John Apple
    # result: japple
    # Used for: 
    # Nexus / hh2 / 
    variant_five = params[0][:1] + params[1]
    return variant_five


# ------------------------------------------------------------------------------------------------------#


new_hire_label = Label(top, text="Name")
new_hire_name = Entry(top) 

gmail_label = Label(top, text="Gmail")
gmail = Entry(top)

quickbase_label = Label(top, text="QuickBase")
quickbase = Entry(top)

mri_label = Label(top, text="MRI")
mri = Entry(top)

nexus_label = Label(top, text="Nexus")
nexus = Entry(top)

sage_label = Label(top, text="Sage")
sage = Entry(top)

clickpay_label = Label(top, text="Click Pay")
clickpay = Entry(top)

procore_label = Label(top, text="ProCore")
procore = Entry(top)

# ------------------------------------------------------------------------------------------------------#


new_hire_label.grid(row=1, column=0, sticky='w')
new_hire_name.grid(row=1, column=1,padx= 10, pady=15, columnspan=10)

gmail_label.grid(row=2, column=0, sticky='w')
gmail.grid(row=2, column=1,padx= 10, pady=5, columnspan=10)

quickbase_label.grid(row=3, column=0, sticky='w')
quickbase.grid(row=3, column=1,padx= 10, pady=5, columnspan=10)

mri_label.grid(row=4, column=0, sticky='w')
mri.grid(row=4, column=1,padx= 10, pady=5, columnspan=10)

nexus_label.grid(row=5, column=0, sticky='w')
nexus.grid(row=5, column=1,padx= 10, pady=5, columnspan=10)

sage_label.grid(row=6, column=0, sticky='w')
sage.grid(row=6, column=1,padx= 10, pady=5, columnspan=10)

clickpay_label.grid(row=7, column=0, sticky='w')
clickpay.grid(row=7, column=1,padx= 10, pady=5, columnspan=10)

procore_label.grid(row=8, column=0, sticky='w')
procore.grid(row=8, column=1,padx= 10, pady=5, columnspan=10)

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