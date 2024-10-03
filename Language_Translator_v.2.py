from tkinter import *
import tkinter as tk
from tkinter import ttk
from googletrans import Translator
translator = Translator(service_urls= [
    'translate.google.com',
    'translate.google.co.kr',
]) 
from tkinter import messagebox

root = tk.Tk()
root.title('Language Translator v.2')
root.geometry('590x370')

frame1 = Frame(root, width=590, height=370, relief=RIDGE, borderwidth=5, bg='pink')
frame1.place(x=0, y=0)

Label(root, text="☆*: .｡.Language Translator ᓚᘏᗢ.｡.:*☆", font= ("Script 23 bold"), fg="black", bg='white').pack(pady=10)

