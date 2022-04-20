# from https://www.youtube.com/watch?v=jE-SpRI3K5g
import imp
from importlib.resources import open_binary
from plistlib import FMT_BINARY
import tkinter as tk
from tkinter import filedialog, Text
import os

root = tk.Tk()



def addApp():
    filename = filedialog.askopenfilename(initialdir='/', title='select file',
    filetypes=(('executables','*.exe'), ('all files', '*.*')))


# Box app Style
canvas = tk.Canvas(root, height=700, width=700, bg='#263D42')
canvas.pack()

frame = tk.Frame(root, bg='white')
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)



# Make buttons for opening files and running apps
openFile = tk.Button(root, text='Open file', padx=10, pady=5, fg='white', bg='#263D42', command=addApp)
openFile.pack()

runApps = tk.Button(root, text='Run Apps', padx=10, pady=5, fg='white', bg='#263D42')
runApps.pack()



root.mainloop()