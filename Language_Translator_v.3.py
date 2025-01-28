from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import font
from tkinter import messagebox

#Import Translator from GoogleTrans package
from googletrans import Translator
translator = Translator(service_urls= [
    'translate.google.com',
    'translate.google.co.kr',
]) 

#Set Up the Language Translator Window pop-up
root = tk.Tk()
root.title('Language Translator v.3')
root.geometry('590x370')

frame1 = Frame(root, width=590, height=370, relief=RIDGE, borderwidth=5, bg='#89cff0')
frame1.place(x=0, y=0)

Label(root, text="ฅ⁠^⁠•⁠ﻌ⁠•⁠^⁠ฅ Language Translator~", font= ("Courier 20 bold"), fg="black", bg='white').pack(pady=10)

selected_language = tk.StringVar()
selected_language.set('English') #English will be the default language

#Lessened the available language
language_list = [
        'Arabic','Cebuano','Chinese','Dutch','English','French','German','Greek','Hawaiian','Ilocano',
        'Italian','Japanese','Korean','Latin','Polish','Portuguese','Russian','Spanish','Swedish','Turkish',
]

#This will serve as the language code for the give list of languages above
language_codes = { 'Arabic': 'ar', 'Cebuano': 'ceb', 'Chinese': 'zh-cn', 'Dutch': 'nl', 'English': 'en', 'French': 'fr',
    'German': 'de', 'Greek': 'el', 'Hawaiian': 'haw', 'Ilocano': 'ilo','Italian': 'it', 'Japanese': 'ja', 'Korean': 'ko',
    'Latin': 'la', 'Polish': 'pl', 'Portuguese': 'pt', 'Russian': 'ru', 'Spanish': 'es', 'Swedish': 'sv', 'Turkish': 'tr',
}

#Function to filter the languages based on the search input
def search_lang(event): 
    query = search_entry.get().lower()
    filtered_lang = [lang for lang in language_list if query in lang.lower()]
    lang_listbox.delete(0, END) #Clears the Listbox
    for lang in filtered_lang:
        lang_listbox.insert(END, lang) #Inserts Filtered Languages according to the given codes
    if filtered_lang:
        lang_listbox.place(x=315, y=60) #Placement of the listbox
    else:
        lang_listbox.place_forget() #Listbox dissappears when there is not match
        selected_language.set("")

#Function to choose a language based on the search results
def select_lang(event):
    try: 
        selected = lang_listbox.get(lang_listbox.curselection())
        selected_language.set(selected) #Selects the Language
        lang_listbox.place_forget() #Hides the listbox
        search_entry.delete(0, END) #Delete what is inside the search bar
        search_entry.insert(0, selected) #Display Selected Language
    except: 
        search_entry.delete(0, END)
        selected_language.set("")

def translate():
    lang_1 = text_entry1.get("1.0", "end-1c")
    cl = selected_language.get().strip()

    #If there is no text inputted, it will display "Enter The Text To Translate!"
    if lang_1.strip() == '':
        messagebox.showerror('Language Translator', 'Enter the Text to Translate!')
        return
    
    #If the inputted text are not alphabetical, it will display "Please Input Text Only!!!"
    if not lang_1.replace(" ", "").isalpha():
        messagebox.showerror('Language Translator', f'Please Input Text Only!!!')
        return
    
    #If the selected Language is not Available, it will display "Invalid Language Selected!"
    lang_codes = language_codes.get(cl, None)
    if not lang_codes:
        messagebox.showerror('Language Translator', f'Invalid Language Selected! {cl}')
        messagebox.showerror('Language Translator', f'Choose another Language Available. {cl}')
        return

    try:
        text_entry2.delete(1.0, 'end')
        output = translator.translate(lang_1, dest=lang_codes)
        text_entry2.insert('end', output.text)
    except Exception as e: 
        messagebox.showerror('Translation Error', f'Error Occured: {e}')

#Clear function - will clear everything
def clear():
    text_entry1.delete(1.0, 'end')
    text_entry2.delete(1.0, 'end')
    search_entry.delete(0, END)
    selected_language.set('English')
    search_entry.insert(0, "Search Language...")

#Set Up the Search Entry box for language selection
search_entry = Entry(frame1, font=('Courier 10 bold'))
search_entry.place(x=310, y=50, width=250)
search_entry.insert(0, "Search Language...")

def empty_placeholder(event):
    if search_entry.get() == "Search Language...":
        search_entry.delete(0, END)

search_entry.bind('<FocusIn>', empty_placeholder)
search_entry.bind('<KeyRelease>',search_lang)

#This is the Listbox for filtered Results
lang_listbox = Listbox(frame1, height=7, width=25, font=('Courier 10 bold'))
lang_listbox.bind('<<ListboxSelect>>', select_lang)

#Setup for Entry Box
text_entry1 = Text(frame1,width=20, height=7, borderwidth=5, relief=RIDGE, font=('Courier', 15))
text_entry1.place(x=20, y=100)

text_entry2 = Text(frame1, width=20, height=7, borderwidth=5, relief=RIDGE, font=('Courier', 15))
text_entry2.place(x=310, y=100)

#Buttons for Translate and Clear
btn = Button(frame1, command=translate, text="  Translate  ", relief=RAISED, borderwidth=2, font=('Courier', 12, 'bold'), bg='#89cff0', fg='black', cursor="hand2")
btn.place(x=140, y=300)

btn2 = Button(frame1, command=clear, text="   Clear   ", relief=RAISED, borderwidth=2, font=('Courier', 12, 'bold'), bg='#89cff0', fg='black', cursor="hand2")
btn2.place(x=300, y=300)

root.mainloop()