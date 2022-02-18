from operator import truediv
from pickle import TRUE
from textwrap import fill
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk


root= tk.Tk()

root.title("Velocity Bike-sharing")
root.geometry("1920x1080")
root.resizable(width=False, height=False)

label1= tk.Label(root)
label1.pack(fill="x")

label2= tk.Label(root)
label2.pack(side="left", fill="y")

image= Image.open("Premiere Timeline.PNG")

label1.configure(text="Welcome to Velocity Bike-sharing!", bg="light blue")
label2.configure(
    text='''
Welcome to Velocity Bike-sharing!

Your Bikes

Bikes nearby

add another bike
''',
bg="light green"
)

root.mainloop()