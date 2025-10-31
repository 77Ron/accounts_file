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

frame = ttk.Frame(root, width = '400p', height = '500p')
frame.pack()

#-------------------

name_var = tk.StringVar()
ename_var = tk.StringVar()
esname_var = tk.StringVar()
eid_var = tk.IntVar()

uname_label = tk.Label(root, text = 'Username:', font=('calibre',10, 'bold'))
uname_entry = tk.Entry(root,textvariable = name_var, font=('calibre',10,'normal'))
uname_label.place(x=50, y=85)
uname_entry.place(x=130, y=85)

ename_label = tk.Label(root, text = 'Customer Name:', font=('calibre',10, 'bold'))
ename_entry = tk.Entry(root,textvariable = ename_var, font=('calibre',10,'normal'))
ename_label.place(x=14, y=130)
ename_entry.place(x=130, y=130)

esname_label = tk.Label(root, text = 'Surname:', font=('calibre',10, 'bold'))
esname_entry = tk.Entry(root,textvariable = esname_var, font=('calibre',10,'normal'))
esname_label.place(x=58, y=155)
esname_entry.place(x=130, y=155)

eid_label = tk.Label(root, text = 'ID/Account No.:', font=('calibre',10, 'bold'))
eid_entry = tk.Entry(root,textvariable = eid_var, font=('calibre',10,'normal'))
eid_label.place(x=22, y=180)
eid_entry.place(x=130, y=180)


save_btn = tk.Button(root,text = 'Save to file.', command = save)
save_btn.place(x=130, y=400)


root.mainloop()
