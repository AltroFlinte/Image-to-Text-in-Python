from importlib.resources import path
import pytesseract
import tkinter as tk 
import customtkinter as ck 
from tkinter.filedialog import askopenfilename
from tkinter import *
from PIL import Image   
import pyttsx3


def Output():
    a=entry_text.get()
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract"
    Result=pytesseract.image_to_string(a) 
    t.insert(tk.END,Result)


def filepath():
    filename=askopenfilename()
    entry_text.set(filename)


def speak2():
    engine = pyttsx3.init()
    s2=t.get("1.0",END)
    engine.say(s2)
    engine.runAndWait()


def clear():
    t.delete(1.0,END)


def img():
    b=entry_text.get()
    img=Image.open(b)
    img.show()


root = tk.Tk()
root.geometry('1280x720')
root.resizable(0,0)
root.title("Text Extract")
entry_text = tk.StringVar()


Label(root, font = 'arial 12 bold', text ='Enter the path of the image: ').place(x=60, y = 40)

Label(root, font = 'arial 12 bold', text ='Converted Text: ').place(x=75,y=250)

Entry(root, font = 'arial 10',textvariable=entry_text, bg= 'ghost white',width=100 ).place(x=290, y = 45)

button = ck.CTkButton(root, corner_radius=10,text='Generate',command=Output).place(x=340, y = 600)

button = ck.CTkButton(root, corner_radius=10,text='Browse',command=filepath).place(x=1009, y = 41)

button = ck.CTkButton(root, corner_radius=10,text='Speak',command=speak2).place(x=540, y = 600)

button = ck.CTkButton(root, corner_radius=10,text='Preview',command=img).place(x=540, y = 160)

button = ck.CTkButton(root, corner_radius=10,text='Clear',command=clear).place(x=740, y = 600)


t = tk.Text(root, width=135, height=18)
t.grid(column=10, row=15,pady=280, padx=80)

root.mainloop()


