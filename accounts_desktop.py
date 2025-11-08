#Accounts desktop

#Move UI from console to desktop screen.

import tkinter as tk
from tkinter import ttk
from tkinter.ttk import *
from company_info import *


#---------Put validations here in two functions. 
    # One for account info and one for transactions.---
"""
    def service_ic(entry):
          if entry.isdigit() == False:
            return False
          if int(entry) < 1 or int(entry) > 3:
            return False
          else:
            return True
    
    service = root.register(service_ic)
    usrv_label = tk.Label(root, text = 'Service Number:', font=('calibre',11, 'bold'), bg=bgcol)
    usrv_entry = tk.Entry(root, textvariable = esrv_v, font=('calibre',11,'normal'), width=1,
                          validate='key', validatecommand=(service, '%P'))
    usrv_label.place(x=10, y=60)
    usrv_entry.place(x=140, y=60)
"""


def dept(dp1, button1, button2, button3, estndchrg_v, esdiscnt_v, estot_v):
    dept=dp1
    button1.configure(bg=btcol1)
    button2.configure(bg=btcol)
    button3.configure(bg=btcol)

    if dept == 1:
        stnd = stnrd_fee1
        disc = d1dc1
        if stnd < 0:
            disc = 0
        if stnd > d1rng:
            disc = d1dc2
    elif dept == 2:
        stnd = stnrd_fee2
        disc = d2dc1
        if stnd < 0:
            disc = 0
        if stnd > d2rng:
            disc = d2dc2
    elif dept == 3:       
        stnd = stnrd_fee3
        disc = d3dc1
        if stnd < 0:
            disc = 0
        if stnd > d3rng:
            disc = d3dc2

    disc_amount = 0.0
    if disc > 0: 
        disc_amount = round(stnd * (disc/100), 2)

    estndchrg_v.set(stnd)
    esdiscnt_v.set(disc_amount)
    estot_v.set(stnd-disc_amount)
   

def save(name_v):
    name=name_v.get()  
    print("Saved")
    name_v.set("")


def UpdateAccounts():
    root = tk.Toplevel()
    root.title("Account Balance File")

    label = tk.Label(root, text=company_name+" Accounts Update", font=('centaur', 21, 'bold'),
                    foreground="gray25", background="white smoke") 
    label.pack()

    frame = tk.Frame(root, width = '550', height = '700', bg=bgcol)
    frame.pack()

    #---Set window screen position
    fw = 550
    fh = 700
    sw = root.winfo_screenwidth()
    sh = root.winfo_screenheight()
    xc = (sw/2) - (550/2)
    yc = (sh/6) - (600/6)
    root.geometry('%dx%d+%d+%d' % (fw, fh, xc, yc))


    #-------------------

    balance_total = 0.00

    name_v = tk.StringVar()
    
    ename_v = tk.StringVar()
    esname_v = tk.StringVar()
    eid_v = tk.IntVar()
    eaddress1_v = tk.StringVar()
    eaddress2_v = tk.StringVar()
    eaddress3_v = tk.StringVar()
    ecode_v = tk.StringVar()
    emobile_v = tk.StringVar()
    eemail_v = tk.StringVar()
    
    estndchrg_v = tk.DoubleVar()
    eothrchrg_v = tk.DoubleVar()
    epayment_v = tk.DoubleVar()
    erefund_v = tk.DoubleVar()

    esdiscnt_v = tk.DoubleVar()
    eodiscnt_v = tk.DoubleVar()
    estax_v = tk.DoubleVar()
    eotax_v = tk.DoubleVar()
    estot_v = tk.DoubleVar()
    eotot_v = tk.DoubleVar()
    etrc_v = tk.StringVar()

    #------Username--------

    uname_label = tk.Label(root, text = 'Username:', font=('calibre',10, 'bold'), bg=bgcol)
    uname_entry = tk.Entry(root,textvariable = name_v, font=('calibre',10,'normal'))
    uname_label.place(x=10, y=60)
    uname_entry.place(x=90, y=60)

    #-------Customer-------

    eid_label = tk.Label(root, text = 'ID/Account No.: '+ acct_number_prefix, font=('calibre',10, 'bold'), bg=bgcol)
    eid_entry = tk.Entry(root,textvariable = eid_v, font=('calibre',10,'normal'))
    eid_label.place(x=211, y=105)
    eid_entry.place(x=345, y=105)

    ename_label = tk.Label(root, text = 'Customer Name:', font=('calibre',10, 'bold'), bg=bgcol)
    ename_entry = tk.Entry(root,textvariable = ename_v, font=('calibre',10,'normal'))
    ename_label.place(x=10, y=155)
    ename_entry.place(x=126, y=155)

    esname_label = tk.Label(root, text = 'Surname:', font=('calibre',10, 'bold'), bg=bgcol)
    esname_entry = tk.Entry(root,textvariable = esname_v, font=('calibre',10,'normal'))
    esname_label.place(x=52, y=180)
    esname_entry.place(x=126, y=180)


    #-------Address-------

    eaddress1_label = tk.Label(root, text = 'Address1:', font=('calibre',10, 'bold'), bg=bgcol)
    eaddress1_entry = tk.Entry(root,textvariable = eaddress1_v, font=('calibre',10,'normal'), width=25)
    eaddress1_label.place(x=54, y=205)
    eaddress1_entry.place(x=126, y=205)

    eaddress2_label = tk.Label(root, text = 'Address2:', font=('calibre',10, 'bold'), bg=bgcol)
    eaddress2_entry = tk.Entry(root,textvariable = eaddress2_v, font=('calibre',10,'normal'), width=25)
    eaddress2_label.place(x=53, y=230)
    eaddress2_entry.place(x=126, y=230)

    eaddress2_label = tk.Label(root, text = 'Address3:', font=('calibre',10, 'bold'), bg=bgcol)
    eaddress2_entry = tk.Entry(root,textvariable = eaddress3_v, font=('calibre',10,'normal'), width=25)
    eaddress2_label.place(x=53, y=255)
    eaddress2_entry.place(x=126, y=255)

    ecode_label = tk.Label(root, text = 'Post Code:', font=('calibre',10, 'bold'), bg=bgcol)
    ecode_entry = tk.Entry(root,textvariable = ecode_v, font=('calibre',10,'normal'), width=8)
    ecode_label.place(x=46, y=280)
    ecode_entry.place(x=126, y=280)

    emobile_label = tk.Label(root, text = 'Mobile:', font=('calibre',10, 'bold'), bg=bgcol)
    emobile_entry = tk.Entry(root,textvariable = emobile_v, font=('calibre',10,'normal'), width=10)
    emobile_label.place(x=67, y=305)
    emobile_entry.place(x=126, y=305)

    eemail_label = tk.Label(root, text = 'Email:', font=('calibre',10, 'bold'), bg=bgcol)
    eemail_entry = tk.Entry(root,textvariable = eemail_v, font=('calibre',10,'normal'), width=30)
    eemail_label.place(x=73, y=330)
    eemail_entry.place(x=126, y=330)

    ebalance_label = tk.Label(root, text = 'Balance: '+ str(balance_total), font=('garamond', 15, 'bold'), bg=bgcol)
    ebalance_label.place(x=360, y=350)


    #----Transactions--------

    dept1_btn = tk.Button(root, text = '1 '+dept1, 
                          command = lambda: dept(1, dept1_btn, dept2_btn, dept3_btn, estndchrg_v, esdiscnt_v, estot_v), 
                          font=('garamond', 12, 'bold'), bg=btcol, fg='black')
    dept1_btn.place(x=25, y=370)
    dept2_btn = tk.Button(root, text = '2 '+dept2,
                          command = lambda: dept(2, dept2_btn, dept1_btn, dept3_btn, estndchrg_v, esdiscnt_v, estot_v), 
                          font=('garamond', 12, 'bold'), bg=btcol, fg='black')
    dept2_btn.place(x=40+len(dept1)*10, y=370)
    dept3_btn = tk.Button(root, text = '3 '+dept3, 
                          command = lambda: dept(3, dept3_btn, dept1_btn, dept2_btn, estndchrg_v, esdiscnt_v, estot_v), 
                          font=('garamond', 12, 'bold'), bg=btcol, fg='black')
    dept3_btn.place(x=50+len(dept1)*10+len(dept2)*10, y=370)

    etr_label = tk.Label(root, text = 'Standard Charge'+' '*10+'Other Charges'+' '*12+'Payment'+' '*15+'Refund', font=('garamond', 13, 'bold'), bg=bgcol)
    etr_label.place(x=18, y=410)

    estndchrg_entry = tk.Entry(root, textvariable = estndchrg_v, font=('calibre',10,'normal'), width=10)
    estndchrg_entry.place(x=21, y=440)

    eothrchrg_entry = tk.Entry(root, textvariable = eothrchrg_v, font=('calibre',10,'normal'), width=10)
    eothrchrg_entry.place(x=180, y=440)

    epayment_entry = tk.Entry(root, textvariable = epayment_v, font=('calibre',10,'normal'), width=10)
    epayment_entry.place(x=330, y=440)

    erefund_entry = tk.Entry(root, textvariable = erefund_v, font=('calibre',10,'normal'), width=10)
    erefund_entry.place(x=453, y=440)

    esdiscnt_label = tk.Label(root, text = 'Discount', font=('garamond', 11, 'bold'), bg=bgcol)
    esdiscnt_label.place(x=18, y=468)
    esdiscnt_entry = tk.Entry(root, textvariable = esdiscnt_v, font=('calibre',10,'normal'), width=10)
    esdiscnt_entry.place(x=21, y=490)

    eodiscnt_label = tk.Label(root, text = 'Discount', font=('garamond', 11, 'bold'), bg=bgcol)
    eodiscnt_label.place(x=177, y=468)
    eodiscnt_entry = tk.Entry(root,textvariable = eodiscnt_v, font=('calibre',10,'normal'), width=10)
    eodiscnt_entry.place(x=180, y=490)

    estax_label = tk.Label(root, text = 'Tax', font=('garamond', 11, 'bold'), bg=bgcol)
    estax_label.place(x=18, y=513)
    estax_entry = tk.Entry(root, textvariable = estax_v, font=('calibre',10,'normal'), width=10)
    estax_entry.place(x=21, y=535)

    eotax_label = tk.Label(root, text = 'Tax', font=('garamond', 11, 'bold'), bg=bgcol)
    eotax_label.place(x=177, y=513)
    eotax_entry = tk.Entry(root, textvariable = eotax_v, font=('calibre',10,'normal'), width=10)
    eotax_entry.place(x=180, y=535)

    estot_label = tk.Label(root, text = 'Total', font=('garamond', 11, 'bold'), bg=bgcol)
    estot_label.place(x=18, y=560)
    estax_entry = tk.Entry(root, textvariable = estot_v, state='readonly',
                           font=('calibre',10,'normal'), width=10)
    estax_entry.place(x=21, y=580)

    eotot_label = tk.Label(root, text = 'Total', font=('garamond', 11, 'bold'), bg=bgcol)
    eotot_label.place(x=177, y=560)
    eotax_entry = tk.Entry(root, textvariable = eotot_v, state='readonly',
                           font=('calibre',10,'normal'), width=10)
    eotax_entry.place(x=180, y=580)

    etrc_label = tk.Label(root, text = 'Transaction Comments:', font=('calibre',10, 'bold'), bg=bgcol)
    etrc_entry = tk.Entry(root, textvariable = etrc_v, font=('calibre',10,'normal'), width=75)
    etrc_label.place(x=10, y=605)
    etrc_entry.place(x=10, y=630)

    #----Save----
    save_btn = tk.Button(root,text = 'Save Updates', command = lambda: save(name_v), font=('garamond', 12, 'bold'), bg=btcol, fg='black')
    save_btn.place(x=330, y=680)

