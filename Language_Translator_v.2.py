from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import font
from googletrans import Translator
translator = Translator(service_urls= [
    'translate.google.com',
    'translate.google.co.kr',
]) 
from tkinter import messagebox

root = tk.Tk()
root.title('Language Translator v.2')
root.geometry('590x370')

frame1 = Frame(root, width=590, height=370, relief=RIDGE, borderwidth=5, bg='#89cff0')
frame1.place(x=0, y=0)

Label(root, text="ฅ⁠^⁠•⁠ﻌ⁠•⁠^⁠ฅ Language Translator~", font= ("Courier 20 bold"), fg="black", bg='white').pack(pady=10)

def translate():
    lang_1 = text_entry1.get("1.0", "end-1c")
    cl = choose_language.get()

    if lang_1 == '':
        messagebox.showerror('Language Translator', 'Enter the Text to Translate!')
    else:
        text_entry2.delete(1.0, 'end')
        translator = Translator()
        output = translator.translate(lang_1, dest=cl)
        text_entry2.insert('end', output.text)

def clear():
    text_entry1.delete(1.0, 'end')
    text_entry2.delete(1.0, 'end')

a = tk.StringVar()

auto_select = ttk.Combobox(frame1, width=27, textvariable= a, state='randomly', font=('Courier', 10, 'bold'))

auto_select['values'] = (
                         'Auto Select',
                        )

auto_select.place(x=30, y=60)
auto_select.current(0)

l = tk.StringVar()
choose_language = ttk.Combobox(frame1, width=27, textvariable=l, state='readonly', font=('Courier', 10, 'bold'))
choose_language['values'] = (
                        'Afrikaans',
                        'Albanian',
                        'Amharic',
                        'Arabic',
                        'Armenian',
                        'Assamese',
                        'Aymara',
                        'Azerbaijani',
                        'Bambara',
                        'Basque',
                        'Belarusian',
                        'Bengali',
                        'Bhojpuri',
                        'Bosnian',
                        'Bulgarian',
                        'Catalan',
                        'Cebuano',
                        'Chinese',
                        'Corsican',
                        'Croatian',
                        'Czech',
                        'Danish',
                        'Dhivehi',
                        'Dogri',
                        'Dutch',
                        'English',
                        'Esperanto',
                        'Estonian',
                        'Ewe',
                        'Filipino',
                        'Finnish',
                        'French',
                        'Frisian',
                        'Galician',
                        'Georgian',
                        'German',
                        'Greek',
                        'Guarani',
                        'Gujarati',
                        'Haitian Creole',
                        'Hausa',
                        'Hawaiian',
                        'Hebrew',
                        'Hindi',
                        'Hmong',
                        'Hungarian',
                        'Icelandic',
                        'Igbo',
                        'Ilocano',
                        'Indonesian',
                        'Irish',
                        'Italian',
                        'Japanese',
                        'Javanese',
                        'Kannada',
                        'Kazakh',
                        'Khmer',
                        'Kinyarwanda',
                        'Konkani',
                        'Korean',
                        'Krio',
                        'Kurdish',
                        'Kurdish',
                        'Kyrgyz',
                        'Lao',
                        'Latin',
                        'Latvian',
                        'Lingala',
                        'Lithuanian',
                        'Luganda',
                        'Luxembourgish',
                        'Macedonian',
                        'Maithili',
                        'Malagasy',
                        'Malay',
                        'Malayalam',
                        'Maltese',
                        'Maori',
                        'Marathi',
                        'Meiteilon',
                        'Mizo',
                        'Mongolian',
                        'Myanmar',
                        'Nepali',
                        'Norwegian',
                        'Nyanja',
                        'Odia',
                        'Oromo',
                        'Pashto',
                        'Persian',
                        'Polish',
                        'Portuguese',
                        'Punjabi',
                        'Quechua',
                        'Romanian',
                        'Russian',
                        'Samoan',
                        'Sanskrit',
                        'Scots Gaelic',
                        'Sepedi',
                        'Serbian',
                        'Sesotho',
                        'Shona',
                        'Sindhi',
                        'Sinhala',
                        'Slovak',
                        'Slovenian',
                        'Somali',
                        'Spanish',
                        'Sundanese',
                        'Swahili',
                        'Swedish',
                        'Tajik',
                        'Tamil',
                        'Tatar',
                        'Telugu',
                        'Thai',
                        'Tigrinya',
                        'Tsonga',
                        'Turkish',
                        'Turkmen',
                        'Twi',
                        'Ukrainian',
                        'Urdu',
                        'Uyghur',
                        'Uzbek',
                        'Vietnamese',
                        'Welsh',
                        'Xhosa',
                        'Yiddish',
                        'Yoruba',
                        'Zulu',
                            )
choose_language.place(x=315, y=60)
choose_language.current(0)

text_entry1 = Text(frame1,width=20, height=7, borderwidth=5, relief=RIDGE, font=('Courier', 15))
text_entry1.place(x=20, y=100)

text_entry2 = Text(frame1, width=20, height=7, borderwidth=5, relief=RIDGE, font=('Courier', 15))
text_entry2.place(x=310, y=100)

btn = Button(frame1, command=translate, text="  Translate  ", relief=RAISED, borderwidth=2, font=('Courier', 12, 'bold'), bg='#89cff0', fg='black', cursor="hand2")
btn.place(x=140, y=300)

btn2 = Button(frame1, command=clear, text="   Clear   ", relief=RAISED, borderwidth=2, font=('Courier', 12, 'bold'), bg='#89cff0', fg='black', cursor="hand2")
btn2.place(x=300, y=300)

root.mainloop()