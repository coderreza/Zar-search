import ctypes
import os
import string
import tkinter as tk
from tkinter import *
from tkinter import messagebox

def get_drives():
    drives = []
    bitmask = ctypes.windll.kernel32.GetLogicalDrives()
    for letter in string.ascii_uppercase:
        if bitmask & 1:
            drives.append(f"{letter}:\\")
        bitmask >>= 1
    return drives
win = tk.Tk()
win.configure(width=170,height=40)
def find():
    found = ""
    foundornot = False
    file = filename.get()
    for drive in get_drives():
        for root, dirs, files in os.walk(drive, onerror=lambda e: None):
            for name in files:
                if name == file:
                    foundornot = True
                    found += f"{os.path.join(root, name)}\n"
    if foundornot:
        if messagebox.askyesno("file was found. do you want to open it?", found):
            files = found.splitlines()
            for i in files:
                os.startfile(i)
        else:
            pass
    else:
        messagebox.showwarning("file not found",f"{file} was not found on your pc")
filename = tk.Entry(master=win)
filename.place(x=1,y=1)
searchbtn = tk.Button(text="search",command=find)
searchbtn.place(x=120,y=1)
win.mainloop()