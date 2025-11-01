#Accounts desktop

#Move UI from console to desktop screen.

import tkinter as tk
from tkinter import ttk
from tkinter.ttk import *
from company_info import *

def save():

    name=name_var.get()  
    print("Username is: " + name)
    name_var.set("")


root = tk.Tk() 

root.title("Account Balance File")

Style().configure('Acct.TFrame', background=bgcol, foreground = 'black')

label = ttk.Label(root, text=company_name+" Account Balances", font=('centaur', 28, 'bold'),
                   foreground="white smoke", background="gray25") 
label.pack() 

frame = ttk.Frame(root, style='Acct.TFrame', width = '400p', height = '500p')
frame.pack()

#-------------------

name_var = tk.StringVar()
ename_var = tk.StringVar()
esname_var = tk.StringVar()
eid_var = tk.IntVar()
eaddress1_var = tk.StringVar()
eaddress2_var = tk.StringVar()
ecode_var = tk.StringVar()

uname_label = tk.Label(root, text = 'Username:', font=('calibre',10, 'bold'), bg=bgcol)
uname_entry = tk.Entry(root,textvariable = name_var, font=('calibre',10,'normal'))
uname_label.place(x=50, y=85)
uname_entry.place(x=130, y=85)

#-------Customer-------

ename_label = tk.Label(root, text = 'Customer Name:', font=('calibre',10, 'bold'), bg=bgcol)
ename_entry = tk.Entry(root,textvariable = ename_var, font=('calibre',10,'normal'))
ename_label.place(x=14, y=130)
ename_entry.place(x=130, y=130)

esname_label = tk.Label(root, text = 'Surname:', font=('calibre',10, 'bold'), bg=bgcol)
esname_entry = tk.Entry(root,textvariable = esname_var, font=('calibre',10,'normal'))
esname_label.place(x=58, y=155)
esname_entry.place(x=130, y=155)

eid_label = tk.Label(root, text = 'ID/Account No.:', font=('calibre',10, 'bold'), bg=bgcol)
eid_entry = tk.Entry(root,textvariable = eid_var, font=('calibre',10,'normal'))
eid_label.place(x=22, y=180)
eid_entry.place(x=130, y=180)

#-------Address-------

eaddress1_label = tk.Label(root, text = 'Address1:', font=('calibre',10, 'bold'), bg=bgcol)
eaddress1_entry = tk.Entry(root,textvariable = eaddress1_var, font=('calibre',10,'normal'), width=25)
eaddress1_label.place(x=58, y=215)
eaddress1_entry.place(x=130, y=215)

eaddress2_label = tk.Label(root, text = 'Address2:', font=('calibre',10, 'bold'), bg=bgcol)
eaddress2_entry = tk.Entry(root,textvariable = eaddress2_var, font=('calibre',10,'normal'), width=25)
eaddress2_label.place(x=57, y=245)
eaddress2_entry.place(x=130, y=245)

ecode_label = tk.Label(root, text = 'Post Code:', font=('calibre',10, 'bold'), bg=bgcol)
ecode_entry = tk.Entry(root,textvariable = ecode_var, font=('calibre',10,'normal'), width=8)
ecode_label.place(x=50, y=270)
ecode_entry.place(x=130, y=270)


save_btn = tk.Button(root,text = 'Save to file.', command = save)
save_btn.place(x=130, y=400)


root.mainloop()
