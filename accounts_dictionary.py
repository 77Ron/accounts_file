#Accounts dictionary

import pickle
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import StrMethodFormatter
from company_accounts import *

    
def LoadDictFile():
    while True:
        try:
            f2 = open("accts2", "rb")
            acct_dict_file = pickle.load(f2)
            #print(acct_dict)
            f2.close()
        except FileNotFoundError as e:
            print("Cannot find accts2: %s" % (e.strerror))
            init1 = ""
            while init1 != 'Y' and init1 != 'N':
                init1 = input("Initialise the file? (Y/N): ")
            if init1 == 'Y':
                print("Initialising file.")
                acct_dict_file = {}
                f2 = open("accts2", "wb")
                pickle.dump(acct_dict_file, f2)
                f2.close()
        except IOError as e:
            print("Cannot open accts2: %s" % (e.strerror)); exit()

        return acct_dict_file

def UpdateDictFile():
    acct_dict = LoadDictFile()
    while True:
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

        ename = input("First Name: ")
        esurname = input("Surname: ")
        aname = esurname + ", " + ename
        
        while True:
            try:
                id = int(input("ID number:"))
            except Exception:
                print("ID must be numeric.")
                continue
            break

        if (aname, id) in acct_dict and acct_dict[aname, id][2] == edept:
            print(acct_dict[aname, id])
            del1 = input("Enter 'del' to delete this account: ")
            if del1 == 'del':
                try:
                    del acct_dict[aname, id]
                    print("Account deleted:", aname, id)
                except Exception:
                    print("Account cannot be deleted.")
        else:
            if edept == 1:
                A0 = Dept1Account()
            elif edept == 2:
                A0 = Dept2Account()
            elif edept == 3:
                A0 = Dept3Account()
            A0.dept = edept
            A0.deptname = A0.department()
            A0.name = aname
            A0.id = id
            A0.address = input("Address: ")
            while True:
                ep_code = str(input("Post code: ")).upper()
                if len(ep_code) > 7:
                    print("Post code must be less than 8 characters.")
                    continue
                else: 
                    break
            A0.p_code = ep_code
            while True:
                try:
                    ebalance = float(input("Account balance: "))
                except Exception:
                    print("Balance must be numeric.")
                    continue
                break
            A0.balance = round(ebalance,2)

            print("New Account: ", A0)
            esave1 = ""
            while esave1 != 'Y' and esave1 != 'N':
                esave1 = input("Is the information correct? (Y/N): ")
            if esave1 == "Y":
                discnt = A0.discount()
                edict = {(A0.name, A0.id):[A0.address, A0.p_code, edept, A0.balance, discnt]}
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
            return

def PrintDictFile():

    while True:
        try:
            department1 = input("Enter department number, or press Enter for All: ")
            if department1 == "": 
                department1 = 0
                break 
            department1 = int(department1)
            if department1 < 1 or department1 > 3:
                print("Department must be 1, 2, or 3.")
                continue
        except Exception:
            print("Department must be numeric.")
            continue
        break

    let0 = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    
    surnames1 = input("Enter surname first letters separated by commas, or press Enter for All: ")
    
    if surnames1 == "":
        surnames1 = 'All'
        let1 = let0
    else:
        let1=[]
        for x in range (0,len(surnames1),2):
            if surnames1[x] in let0: let1.append(surnames1[x])
    print("Surname first letters:", let1)

    acct_dict = LoadDictFile()
    
    count=0
    balance_total=0
    for (name,id), info in acct_dict.items():
        if department1 == 0 or info[2] == department1:
            if name[0] in let1:
                if info[2] == 1:
                    A0 = Dept1Account()
                elif info[2] == 2:
                    A0 = Dept2Account()
                elif info[2] == 3:
                    A0 = Dept3Account()
                A0.dept = info[2]
                A0.deptname = A0.department()
                A0.name = name
                A0.id = id
                A0.address = info[0]
                A0.p_code = info[1]
                A0.balance = info[3]
                print(A0)
                count+=1
                balance_total += info[3]

    print("--------------")
    print("Total accounts:", count)
    if surnames1 == 'All': 
        print("Total of balances:", balance_total)

    return


def TableDictFile():
    acct_dict = LoadDictFile()
    df = pd.DataFrame.from_dict(acct_dict, orient='index', 
                                columns = ['-Address-','-Post Code-', '-Dept.-', '-Balance-', '-Discount-'])
    #df.style.set_properties(**{'text-align': 'left'}) ---- Requires install.
    pd.options.display.float_format = '{:.2f}'.format
    print(df)
    return

def GraphDictFile():
    acct_dict = LoadDictFile()
    df = pd.DataFrame.from_dict(acct_dict, orient='index', 
                                columns = ['-Address-','-Post Code-', '-Dept.-', '-Balance-', '-Discount-'])
    plt.figure(figsize=(9,9))
    plt.grid(True)
    plt.title("Discount vs Balance", fontsize = 20)
    plt.xlabel("Discount", fontsize = 16)
    plt.ylabel("Balance", fontsize = 16)
    plt.bar(df["-Discount-"].values, df["-Balance-"].values, color = "black")
    plt.gca().yaxis.set_major_formatter(StrMethodFormatter('{x:,.2f}'))
    plt.gca().xaxis.set_major_formatter(StrMethodFormatter('{x:,.2f}'))
    plt.show()
