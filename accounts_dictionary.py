#Accounts dictionary

from datetime import datetime
import pickle
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

    root = tk.Tk() 
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
                A0 = Dept1Account(1, name, id, info[0], info[1], info[2][1])
                T.insert(tk.END, A0)
                T.insert(tk.END,'\n')
                balance_total += info[2][1]
            if (deptin == 0 or deptin == 2) and info[3][3] > 0:
                A0 = Dept2Account(2, name, id, info[0], info[1], info[3][1])
                T.insert(tk.END, A0)
                T.insert(tk.END,'\n')
                balance_total += info[3][1]
            if (deptin == 0 or deptin == 3) and info[4][3] > 0:
                A0 = Dept3Account(3, name, id, info[0], info[1], info[4][1])         
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
    
    tk.mainloop()



def TableDictFile():

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

    acct_dict = LoadDictFile()

    root = tk.Tk() 
    root.title("Account Balance File")
    root.geometry("900x500")
    T = tk.Text(root, height = 700, width = 900, bg=bgcol)
    l = Label(root, text = "Accounts Table")
    l.config(font =("centaur", 22))
    l.pack()
    T.pack()
  
    df = pd.DataFrame({key: pd.Series(val[edept+1], index=['Dept','Balance','Discount','Created','Last Updated']) for key, val in acct_dict.items()})
    dft = df.transpose()
    #df.style.set_properties(**{'text-align': 'left'}) ---- Requires install.
    #pd.options.display.float_format = '{:.2f}'.format
    T.insert(tk.END, dft)

    tk.mainloop()

def GraphDictFile():

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

    acct_dict = LoadDictFile()

    df = pd.DataFrame({key: pd.Series(val[edept+1], index=['Dept','Balance','Discount','Created','Last Updated']) for key, val in acct_dict.items()})
    dft = df.transpose()
    #df = pd.DataFrame.from_dict(acct_dict, orient='index', columns = ['-Address-','-Post Code-', '-Dept.-', '-Balance-', '-Discount-'])
    plt.figure(figsize=(9,9))
    plt.grid(True)
    plt.title("Department "+str(edept)+" Balance vs Discount", fontsize = 20)
    plt.xlabel("Discount", fontsize = 16)
    plt.ylabel("Balance", fontsize = 16)
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

            root = tk.Tk() 
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
            
            tk.mainloop()
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
        newinfo = [1, 0.0, 0.0, 0, 0],[2, 0.0, 0.0, 0, 0],[3, 0.0, 0.0, 0, 0]
        newinfo[info[2]-1][1] = info[3]
        newinfo[info[2]-1][2] = info[4]
        newinfo[info[2]-1][3] = d2
        newinfo[info[2]-1][4] = d2

        account_temp = {(name, id):[info[0], info[1], newinfo[0], newinfo[1], newinfo[2]]}
        print(name, id, info[0], info[1], newinfo)
        acct_dict_temp.update(account_temp)
           
    f2 = open("accts_temp2", "wb")
    pickle.dump(acct_dict_temp, f2)
    f2.close()