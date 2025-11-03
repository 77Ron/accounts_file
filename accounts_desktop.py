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

def dept(dp1):
    dept=dp1 


root = tk.Tk() 

root.title("Account Balance File")

s = Style()
s.configure('Acct.TFrame', background=bgcol, foreground = 'black')

label = ttk.Label(root, text=company_name+" Accounts Update", font=('centaur', 21, 'bold'),
                   foreground="gray25", background="white smoke") 
label.pack() 

frame = ttk.Frame(root, style='Acct.TFrame', width = '400p', height = '500p')
frame.pack()

#-------------------

balance_total = 0.00

name_var = tk.StringVar()
ename_var = tk.StringVar()
esname_var = tk.StringVar()
eid_var = tk.IntVar()
eaddress1_var = tk.StringVar()
eaddress2_var = tk.StringVar()
ecode_var = tk.StringVar()

uname_label = tk.Label(root, text = 'Username:', font=('calibre',10, 'bold'), bg=bgcol)
uname_entry = tk.Entry(root,textvariable = name_var, font=('calibre',10,'normal'))
uname_label.place(x=10, y=60)
uname_entry.place(x=90, y=60)

#-------Customer-------

eid_label = tk.Label(root, text = 'ID/Account No.:', font=('calibre',10, 'bold'), bg=bgcol)
eid_entry = tk.Entry(root,textvariable = eid_var, font=('calibre',10,'normal'))
eid_label.place(x=222, y=105)
eid_entry.place(x=330, y=105)

ename_label = tk.Label(root, text = 'Customer Name:', font=('calibre',10, 'bold'), bg=bgcol)
ename_entry = tk.Entry(root,textvariable = ename_var, font=('calibre',10,'normal'))
ename_label.place(x=10, y=155)
ename_entry.place(x=126, y=155)

esname_label = tk.Label(root, text = 'Surname:', font=('calibre',10, 'bold'), bg=bgcol)
esname_entry = tk.Entry(root,textvariable = esname_var, font=('calibre',10,'normal'))
esname_label.place(x=52, y=180)
esname_entry.place(x=126, y=180)



#-------Address-------

eaddress1_label = tk.Label(root, text = 'Address1:', font=('calibre',10, 'bold'), bg=bgcol)
eaddress1_entry = tk.Entry(root,textvariable = eaddress1_var, font=('calibre',10,'normal'), width=25)
eaddress1_label.place(x=54, y=205)
eaddress1_entry.place(x=126, y=205)

eaddress2_label = tk.Label(root, text = 'Address2:', font=('calibre',10, 'bold'), bg=bgcol)
eaddress2_entry = tk.Entry(root,textvariable = eaddress2_var, font=('calibre',10,'normal'), width=25)
eaddress2_label.place(x=53, y=230)
eaddress2_entry.place(x=126, y=230)

eaddress2_label = tk.Label(root, text = 'Address3:', font=('calibre',10, 'bold'), bg=bgcol)
eaddress2_entry = tk.Entry(root,textvariable = eaddress2_var, font=('calibre',10,'normal'), width=25)
eaddress2_label.place(x=53, y=255)
eaddress2_entry.place(x=126, y=255)

ecode_label = tk.Label(root, text = 'Post Code:', font=('calibre',10, 'bold'), bg=bgcol)
ecode_entry = tk.Entry(root,textvariable = ecode_var, font=('calibre',10,'normal'), width=8)
ecode_label.place(x=46, y=280)
ecode_entry.place(x=126, y=280)

ecode_label = tk.Label(root, text = 'Mobile:', font=('calibre',10, 'bold'), bg=bgcol)
ecode_entry = tk.Entry(root,textvariable = ecode_var, font=('calibre',10,'normal'), width=10)
ecode_label.place(x=67, y=305)
ecode_entry.place(x=126, y=305)

ecode_label = tk.Label(root, text = 'Email:', font=('calibre',10, 'bold'), bg=bgcol)
ecode_entry = tk.Entry(root,textvariable = ecode_var, font=('calibre',10,'normal'), width=30)
ecode_label.place(x=73, y=330)
ecode_entry.place(x=126, y=330)

ecode_label = tk.Label(root, text = 'Balance: '+ str(balance_total), font=('garamond', 15, 'bold'), bg=bgcol)
ecode_label.place(x=360, y=350)


#----Department--------
dept_btn = tk.Button(root, text = '1 '+ dept1, command = dept(1), font=('garamond', 12, 'bold'), bg=btcol, fg='black')
dept_btn.place(x=25, y=370)
dept_btn = tk.Button(root, text = '2 ' +dept2, command = dept(2),  font=('garamond', 12, 'bold'), bg=btcol, fg='black')
dept_btn.place(x=40+len(dept1)*10, y=370)
dept_btn = tk.Button(root, text = '3 '+dept3, command = dept(3),  font=('garamond', 12, 'bold'), bg=btcol, fg='black')
dept_btn.place(x=50+len(dept1)*10+len(dept2)*10, y=370)

#---Save----
save_btn = tk.Button(root,text = 'Save Updates', command = save, font=('garamond', 12, 'bold'), bg=btcol, fg='black')
save_btn.place(x=240, y=590)


root.mainloop()
