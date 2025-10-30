#Accounts desktop

#Move UI from console to desktop screen.

import tkinter as tk
from tkinter import ttk
from company_info import *

def save():

    name=name_var.get()  
    print("Username is: " + name)
    name_var.set("")


root = tk.Tk() 

root.title("Account Balance File")

label = ttk.Label(root, text=company_name+" Account Balances", font=('timesroman',20, 'italic'), foreground="white", background="black") 
label.pack() 

button = ttk.Button(root, text="Click Me", command=lambda: print("Button clicked!")) 
button.pack()

frame = ttk.Frame(root, width = '400p', height = '500p')
frame.pack()

#-------------------

name_var=tk.StringVar()

name_label = tk.Label(root, text = 'Username:', font=('calibre',10, 'bold'))
name_entry = tk.Entry(root,textvariable = name_var, font=('calibre',10,'normal'))
save_btn = tk.Button(root,text = 'Save to file.', command = save)
name_label.place(x = 100, y = 100)
name_entry.place(x=180, y= 100)
save_btn.place(x=180, y=400)


root.mainloop()
