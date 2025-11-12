#Accounts dictionary

from datetime import datetime
import pickle
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import StrMethodFormatter
from company_accounts import *

import tkinter as tk
from tkinter import ttk
from tkinter.ttk import *
    

def LoadDictFile():

    while True:
        try:
            f2 = open("accts2", "rb")
            acct_dict_file = pickle.load(f2)
            #print(acct_dict)
            f2.close()
        except FileNotFoundError as e:
            print("Cannot find file, accts2: %s" % (e.strerror))
            init1 = ""
            while init1 != 'Y' and init1 != 'N':
                init1 = input("Initialise the accounts file? (Y/N): ")
            if init1 == 'Y':
                print("Initialising file.")
                acct_dict_file = {}
                f2 = open("accts2", "wb")
                pickle.dump(acct_dict_file, f2)
                f2.close()
        except IOError as e:
            print("Cannot open file, accts2: %s" % (e.strerror)); exit()

        return acct_dict_file


def UpdateDictFile():

    uname = input("Enter username: ")
    with open("accts1", "a") as f:
        f.write(uname + " logged in " + str(datetime.now())+ " - ")

    acct_dict = LoadDictFile()

    while True:
        
        ename = ""
        while len(ename) < 1 or len(ename) > 25:
            efname = input("First Name: ").strip()
            esurname = input("Surname: ").strip()
            ename = esurname + ", " + efname
        
        while True:
            try:
                eid = int(input("ID number:"))
            except Exception:
                print("ID must be numeric.")
                continue
            break
        
        update1 = "New"
        info = ["", 0.0, [1, 0.0, 0.0, 0, 0],[2, 0.0, 0.0, 0, 0],[3, 0.0, 0.0, 0, 0]]
        if (ename, eid) in acct_dict:
            info = acct_dict[ename, eid]
            print(acct_dict[ename, eid])
            while update1 != 'Del' and update1 != 'U':
                update1 = input("Account already exists. Del'ete or U'pdate this account: ")
            if update1 == 'Del':
                try:
                    del acct_dict[ename, eid]
                    print("Account deleted:", ename, eid)
                except Exception:
                    print("Account cannot be deleted.")

        if update1 != 'Del':
            #Currently cannot modify address.
            if update1 == 'New':
                eaddress = ""
                while len(eaddress) < 1 or len(eaddress) > 25:
                    eaddress = input("Address: ").strip()
                while True:
                    ecode = str(input("Post code: ")).upper()
                    if len(ecode) > 7:
                        print("Post code must be less than 8 characters.")
                        continue
                    else: 
                        break
            else:
                eaddress = info[0]
                ecode = info[1]

            while True:
                try:
                    edept = int(input("Department: "))
                    if edept < 1 or edept > 3:
                        print("Department must be 1, 2, or 3.")
                        continue
                except Exception:
                    print("Department must be numeric.")
                    continue
                break
                    
            while True:
                try:
                    ebalance = float(input("Account balance: "))
                    ebalance = round(ebalance,2)
                except Exception:
                    print("Balance must be numeric.")
                    continue
                break

            if edept == 1:
                A0 = Dept1Account(edept, ename, eid, eaddress, ecode, ebalance)
            elif edept == 2:
                A0 = Dept2Account(edept, ename, eid, eaddress, ecode, ebalance)
            elif edept == 3:
                A0 = Dept3Account(edept, ename, eid, eaddress, ecode, ebalance)
            
            print("New or modified account: ", A0)
            esave1 = ""
            while esave1 != 'Y' and esave1 != 'N':
                esave1 = input("Is the information correct? (Y/N): ")
            if esave1 == "Y":
                d1 = datetime.now() #Consider using Julian date.
                d2 = int(d1.strftime("%Y%m%d"))
                #info[edept+1][0] is always set to 1, 2, or 3.
                info[edept+1][1] = A0.balance
                info[edept+1][2] = A0.discnt
                if info[edept+1][3] == 0:
                    info[edept+1][3] = d2
                info[edept+1][4] = d2
                edict = {(A0.name, A0.id):[A0.address, A0.p_code,
                                            [info[2][0], info [2][1],info [2][2],info [2][3],info [2][4]],
                                            [info[3][0], info [3][1],info [3][2],info [3][3],info [3][4]],
                                            [info[4][0], info [4][1],info [4][2],info [4][3],info [4][4]]]}
                acct_dict.update(edict)
            else:
                print("Account", A0.name, A0.id," was not updated.")

        esave = ""
        while esave != 'Save' and esave != '+':
            esave = input("Enter 'Save' to save all changes, or '+' to enter or delete another account: ")
        if esave == "Save":
            acct_dict = dict(sorted(acct_dict.items()))
            f2 = open("accts2", "wb")
            pickle.dump(acct_dict, f2)
            f2.close()
            with open("accts1", "a") as f:
                f.write(uname + " saved changes " + str(datetime.now())+ " \n ")

            return


def PrintDictFile():

    while True:
        try:
            deptin = input("Enter department number, or press Enter for All: ")
            if deptin == "": 
                deptin = 0
                break 
            deptin = int(deptin)
            if deptin < 1 or deptin > 3:
                print("Department must be 1, 2, or 3.")
                continue
        except Exception:
            print("Department must be numeric.")
            continue
        break

    let0 = ['A','B','C','D','E','F','G','H','I','J','K','L','M',
            'N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    
    surnames1 = input("Enter surname initials separated by commas, or press Enter for All: ").upper().strip()
    
    if surnames1 == "":
        surnames1 = 'All'
        let1 = let0
    else:
        let1=[]
        for x in range (0,len(surnames1),2):
            if surnames1[x] in let0: let1.append(surnames1[x])

    acct_dict = LoadDictFile()
    
    #Print currently recalculates discount.

    root = tk.Toplevel() 
    root.title("Account Balance File")
    root.geometry("900x500")
    T = tk.Text(root, height = 700, width = 900)
    l = Label(root, text = "Print Accounts")
    l.config(font =("Courier", 14))
    l.pack()
    T.pack()

    count=0
    balance_total=0
    T.insert(tk.END, " "*92+"-Balance- -Discount-"+'\n')
    for (name,id), info in acct_dict.items():
        if name[0] in let1:
            if (deptin == 0 or deptin == 1) and info[2][3] > 0:
                A0 = Dept1Account(srvc_code[0], name, id, info[0], info[1], info[2][1])
                T.insert(tk.END, A0)
                T.insert(tk.END,'\n')
                balance_total += info[2][1]
            if (deptin == 0 or deptin == 2) and info[3][3] > 0:
                A0 = Dept2Account(srvc_code[1], name, id, info[0], info[1], info[3][1])
                T.insert(tk.END, A0)
                T.insert(tk.END,'\n')
                balance_total += info[3][1]
            if (deptin == 0 or deptin == 3) and info[4][3] > 0:
                A0 = Dept3Account(srvc_code[2], name, id, info[0], info[1], info[4][1])         
                T.insert(tk.END, A0)
                T.insert(tk.END,'\n')
                balance_total += info[4][1]         
        count+=1

    T.insert(tk.END, "-------------- \n")
    if surnames1 == 'All': 
        pstr = "Total accounts: "+str(count)+" "*61+"Balance Total: "+str(round(balance_total,2))+"\n"
        T.insert(tk.END, pstr)
    else:
        pstr = "Total accounts: "+str(count)+"\n"
        T.insert(tk.END, pstr)



def TableDictFile():
    root = tk.Toplevel() 
    root.title(company_name)

    label = tk.Label(root, text="Table Selection", font=('centaur', 21, 'bold'),
                    foreground="gray25", background="white smoke") 
    label.pack()

    frame = tk.Frame(root, width = '550', height = '700', bg=bgcol)
    frame.pack()

    #---Set window screen position
    fw = 550
    fh = 600
    sw = root.winfo_screenwidth()
    sh = root.winfo_screenheight()
    xc = (sw/2) - (fw/2)
    yc = (sh/6) - (fh/6)
    root.geometry('%dx%d+%d+%d' % (fw, fh, xc, yc))

    srv1_v = tk.IntVar()
    srv2_v = tk.IntVar()
    srv3_v = tk.IntVar()

    srv_ck1 = tk.Checkbutton(root, text=dept_name[0], font=('calibre',11, 'bold'), bg=bgcol,
                             variable=srv1_v, onvalue=1, offvalue=0)
    srv_ck1.place(x=20, y=100)
    srv_ck2 = tk.Checkbutton(root, text=dept_name[1], font=('calibre',11, 'bold'), bg=bgcol,
                             variable=srv2_v, onvalue=1, offvalue=0)
    srv_ck2.place(x=20, y=130)
    srv_ck3 = tk.Checkbutton(root, text=dept_name[2], font=('calibre',11, 'bold'), bg=bgcol,
                             variable=srv3_v, onvalue=1, offvalue=0)
    srv_ck3.place(x=20,y=160)

    display_btn = tk.Button(root,text = 'Display Table', 
                            command = lambda: TableDisplay(srv1_v, srv2_v, srv3_v),
                             font=('garamond', 12, 'bold'), bg=btcol, fg='black')
    display_btn.place(x=330, y=380)

    def TableDisplay(srv1_v1, srv2_v1, srv3_v1):
        
        srv1_v2 = srv1_v1.get()
        srv2_v2 = srv2_v1.get()
        srv3_v2 = srv3_v1.get()

        acct_dict = LoadDictFile()

        root = tk.Toplevel() 
        root.title(company_name)
        root.geometry("900x500")
        text = tk.Text(root, height = 500, width = 700, bg=bgcol)
        label = Label(root, text = "Accounts Table")
        label.config(font =("centaur", 22))
        label.pack()
        text.pack()

        for edept in range(3):
           
            if (edept == 0 and srv1_v2 == 1) or (edept == 1 and srv2_v2 == 1) or (edept == 2 and srv3_v2 == 1):

                df = pd.DataFrame({key: pd.Series(val[edept+2], 
                                                index=['Dept','Balance','Discount','Created','Last Updated'])
                                                    for key, val in acct_dict.items()})
                dft = df.transpose()
                dft['Dept'] = dft['Dept'].map('{:.0f}'.format)
                dft['Balance'] = dft['Balance'].map('£{:,.2f}'.format)
                dft['Created'] = dft['Created'].map(lambda x: "{1}-{2}-{0}".format(int(x/10000),int((x%10000)/100),int(x%100)))
                dft['Last Updated'] = dft['Last Updated'].map(lambda x: "{1}-{2}-{0}".format(int(x/10000),int((x%10000)/100),int(x%100)))

                #dft['Created'] = pd.to_datetime(dft['Created']).dt.date
                text.insert(tk.END, "\n")
                text.insert(tk.END, dft)


def GraphDictFile():

    root = tk.Toplevel() 
    root.title(company_name)

    label = tk.Label(root, text="Graph Criterea", font=('centaur', 21, 'bold'),
                    foreground="gray25", background="white smoke") 
    label.pack()

    frame = tk.Frame(root, width = '550', height = '700', bg=bgcol)
    frame.pack()

    #---Set window screen position
    fw = 550
    fh = 600
    sw = root.winfo_screenwidth()
    sh = root.winfo_screenheight()
    xc = (sw/2) - (fw/2)
    yc = (sh/6) - (fh/6)
    root.geometry('%dx%d+%d+%d' % (fw, fh, xc, yc))

    #esrv_v = tk.StringVar()
    srv1_v = tk.IntVar()
    srv2_v = tk.IntVar()
    srv3_v = tk.IntVar()

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
    
    srv_ck1 = tk.Checkbutton(root, text=dept_name[0], font=('calibre',11, 'bold'), bg=bgcol,
                             variable=srv1_v, onvalue=1, offvalue=0)
    srv_ck1.place(x=20, y=100)
    srv_ck2 = tk.Checkbutton(root, text=dept_name[1], font=('calibre',11, 'bold'), bg=bgcol,
                             variable=srv2_v, onvalue=1, offvalue=0)
    srv_ck2.place(x=20, y=130)
    srv_ck3 = tk.Checkbutton(root, text=dept_name[2], font=('calibre',11, 'bold'), bg=bgcol,
                             variable=srv3_v, onvalue=1, offvalue=0)
    srv_ck3.place(x=20,y=160)

    display_btn = tk.Button(root,text = 'Display Graph', 
                            command = lambda: GraphDisplay(srv1_v, srv2_v, srv3_v),
                             font=('garamond', 12, 'bold'), bg=btcol, fg='black')
    display_btn.place(x=330, y=380)

    def GraphDisplay(srv1_v1, srv2_v1, srv3_v1):

        #edept = int(esrv_v1.get())
        
        srv1_v2 = srv1_v1.get()
        srv2_v2 = srv2_v1.get()
        srv3_v2 = srv3_v1.get()

        acct_dict = LoadDictFile()
       
        for edept in range(3):
           
            if (edept == 0 and srv1_v2 == 1) or (edept == 1 and srv2_v2 == 1) or (edept == 2 and srv3_v2 == 1):
                
                df = pd.DataFrame({key: pd.Series(val[edept+2], index=['Dept','Balance','Discount','Created','Last Updated']) for key, val in acct_dict.items()})
                dft = df.transpose()
                #df = pd.DataFrame.from_dict(acct_dict, orient='index', columns = ['-Address-','-Post Code-', '-Dept.-', '-Balance-', '-Discount-'])
                plt.figure(figsize=(8,5), facecolor = gbcol)
                #ax = plt.gca()
                #ax.set_facecolor("white")
                plt.grid(True)
                plt.title(str(edept+1)+" "+dept_name[edept]+" - Balance vs Discount", fontsize = 15)
                plt.xlabel("Discount", fontsize = 11)
                plt.ylabel("Balance", fontsize = 11)
                plt.bar(dft["Discount"].values, dft["Balance"].values, color = "black")
                plt.gca().yaxis.set_major_formatter(StrMethodFormatter('{x:,.2f}'))
                plt.gca().xaxis.set_major_formatter(StrMethodFormatter('{x:,.2f}'))
                plt.show()


def DatabaseUpdate():
    print("Option not avaiable yet.")

def DatabaseImport():
    print("Option not avaiable yet.")

def TextFileImport():
    print("Option not avaiable yet.")


def LogFile():

    try:
        with open("accts1", "r") as f:

            root = tk.Toplevel() 
            root.title("Login File")
            root.geometry("900x500")
            T = tk.Text(root, height = 700, width = 900, bg="white smoke")
            l = Label(root, text = "Login Records")
            l.config(font =("courier", 17))
            l.pack()
            T.pack()
  
            for line1 in f:
                #print(line1)
                T.insert(tk.END, line1)
            
            return

    except Exception:
        print("Login file does not exist or cannot be opened.")
        return
    

def ReformatDictFile():

    acct_dict = LoadDictFile()
    
    acct_dict_temp = {}
    for (name,id), info in acct_dict.items():

        d1 = datetime.now() #Consider using Julian date.
        d2 = int(d1.strftime("%Y%m%d"))
        
        account_temp = {(name, id):[info[0], " ", " ", info[1], " ", " ", "0.00", info[2], info[3], info[4]]}
        #transaction_temp = {}

        acct_dict_temp.update(account_temp)

        """
        newinfo = [1, 0.0, 0.0, 0, 0],[2, 0.0, 0.0, 0, 0],[3, 0.0, 0.0, 0, 0]
        newinfo[info[2]-1][1] = info[3]
        newinfo[info[2]-1][2] = info[4]
        newinfo[info[2]-1][3] = d2
        newinfo[info[2]-1][4] = d2
        """
    f2 = open("accts_temp2", "wb")
    f2.truncate()
    pickle.dump(acct_dict_temp, f2)
    f2.close()

    print("===========\n")
    f2 = open("accts_temp2", "rb")
    acct_dict_temp = pickle.load(f2)
    for (name,id), info in acct_dict_temp.items():
        print(name,id,info,"\n")
    f2.close()

    #SQLite---------------
    
    with sqlite3.connect('accounts_main.db') as conn:

        cursor = conn.cursor()    
   
        sql='''
            DROP TABLE IF EXISTS account_info;
            DROP TABLE IF EXISTS transactions;
            PRAGMA foreign_keys = ON;

            CREATE TABLE account_info(
                id INTEGER,
                name TEXT NOT NULL,
                address1 TEXT,
                address2 TEXT,
                address3 TEXT,
                post_code TEXT,
                mobile TEXT,
                email TEXT,
                balance REAL NOT NULL,
                service1_code TEXT,
                service1_taps INTEGER NOT NULL,
                service1_dtcr INTEGER NOT NULL,
                service2_code TEXT,
                service2_taps INTEGER NOT NULL,
                service2_dtcr INTEGER NOT NULL,
                service3_code TEXT,
                service3_taps INTEGER NOT NULL,
                service3_dtcr INTEGER NOT NULL,
                PRIMARY KEY (id),
                CONSTRAINT fk_transactions
                    FOREIGN KEY (id)
                    REFERENCES transactions(id)
                    ON DELETE CASCADE  
            );
        
            CREATE TABLE transactions(
                id INTEGER REFERENCES account_info(id),
                tr_code TEXT NOT NULL,
                trdate_t INTEGER NOT NULL,
                service_code TEXT,
                amount1 REAL,
                amount2 REAL,
                amount3 REAL,
                amount4 REAL,
                PRIMARY KEY (id, tr_code, trdate_t)
            )'''
        
        cursor.executescript(sql)
    
    with sqlite3.connect('accounts_main.db') as conn:

        cursor = conn.cursor()

        #cursor.execute("UPDATE MAIN.SQLITE_SEQUENCE SET SEQ = 1000 WHERE NAME = 'account_info'")
        sflag = 1
        for (name1,id1), info in acct_dict.items():
            
            print(name1,id1,info,"\n")

            d1 = datetime.now() #Consider using Julian date.
            d2 = int(d1.strftime("%Y%m%d"))
            d3 = int(d1.strftime("%Y%m%d%H%M%S"))
            sp = ' '
            address=info[0]
            pcode=info[1]

            if sflag == 1:
                cursor.execute("INSERT INTO account_info VALUES "
                "(?, ?, ?, ?, ?, ?, ?, ?, 0, ?, 0, 0, ?, 0, 0, ?, 0, 0)", 
                (start_acct_no, name1, address, sp, sp, pcode, sp, sp, sp, sp, sp))
                sflag = 0
            else:
                cursor.execute("INSERT INTO account_info VALUES "
                "(NULL, ?, ?, ?, ?, ?, ?, ?, 0, ?, 0, 0, ?, 0, 0, ?, 0, 0)", 
                (name1, address, sp, sp, pcode, sp, sp, sp, sp, sp))
            
            for i in range(3):
                x1 = info[i+2][3]
                if x1 > 0:
                    trcode = "C1"
                    scode = srvc_code[i]
                    for t in range(200000):
                        print('.', end="") #Delay for time stamp
                    d1 = datetime.now()
                    d3 = int(d1.strftime("%Y%m%d%H%M%S"))
                    
                    cursor.execute("INSERT INTO transactions VALUES "
                    "((SELECT id FROM account_info WHERE name = ?), ?, ?, ?, ?, ?, ?, ?)",
                    (name1, trcode, d3, scode, info[i+2][1], info[i+2][2], info[i+2][3], info[i+2][4]))
                    
                    #Update accounts_info.

                    s2flag = 1
                    
                    cursor.execute("SELECT * FROM account_info WHERE name = ?", (name1,))
                    S1 = cursor.fetchone()[11]
                    if S1 == 0:
                        cursor.execute("UPDATE account_info SET service1_code = ?, service1_dtcr = ? WHERE name = ?",
                                    (scode, d2, name1))
                        s2flag = 0
                    
                    if s2flag == 1:
                        cursor.execute("SELECT * FROM account_info WHERE name = ?", (name1,))
                        S1 = cursor.fetchone()[14]
                        if S1 == 0:
                            cursor.execute("UPDATE account_info SET service2_code = ?, service2_dtcr = ? WHERE name = ?",
                                        (scode, d2, name1))
                            s2flag = 0
                    
                    if s2flag == 1:
                        cursor.execute("SELECT * FROM account_info WHERE name = ?", (name1,))
                        S1 = cursor.fetchone()[17]
                        if S1 == 0:
                            cursor.execute("UPDATE account_info SET service3_code = ?, service3_dtcr = ? WHERE name = ?",
                                        (scode, d2, name1))
                        
        
        #conn = sqlite3.connect('accounts_main.db')
        #conn.execute("BEGIN")
        #conn.commit() or END TRANSACTION
        #cursor.execute("SELECT * FROM account_info")
        #cursor.execute("SELECT * FROM transactions")