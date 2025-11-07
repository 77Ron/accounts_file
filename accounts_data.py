# Account maintenance, transactions, billing, and scheduling for
# individual services providers.

# Currently a work in progress that stores dict files.
# Will be relocated on a MySQL database.


import tkinter as tk
from tkinter import ttk
from tkinter.ttk import *
from accounts_desktop import *
from accounts_dictionary import *
from company_calendar import *
from company_settings import *

def Menu(root, text1, command1, y1):
    M1_btn = tk.Button(root, text = text1, command = command1, width = 20, 
                       font=('calibre', 10, 'bold'), bg=btcol, fg='black')
    M1_btn.place(x=27, y=y1)

def main():

    root = tk.Tk() 
    root.title(company_name)
    s = Style()
    s.configure('Menu.TFrame', background=bgcol, foreground = 'black')
    label = ttk.Label(root, text = "Main Menu", font=('centaur', 21, 'bold'), foreground="gray25", background="white smoke") 
    label.pack() 
    #menu_frame = ttk.Frame(root, style='Menu.TFrame', width = '170p', height = '500p')
    menu_frame = ttk.Frame(root, style='Menu.TFrame')
    menu_frame.pack(expand=True, fill= 'both')

    
    Menu(root, 'Update Accounts', UpdateAccounts, 70)
    Menu(root, 'Print Accounts', PrintDictFile, 100)
    Menu(root, 'Table', TableDictFile, 130)
    Menu(root, 'Graphs', GraphDictFile, 160)
    Menu(root, 'Database Update', DatabaseUpdate, 190)
    Menu(root, 'Database Import', DatabaseImport, 220)
    Menu(root, 'Text File Import', TextFileImport, 250)
    Menu(root, 'Calendar', CalendarView, 280)
    #Menu(root, 'Invoicing', InvoicePrint, 310)
    #Menu(root, 'Messaging', MessageSend, 340)
    #Menu(root, 'Expenses', Expenses, 370)
    Menu(root, 'Print Log File', LogFile, 310)
    Menu(root, 'Settings', Settings, 340)
    Menu(root, 'Exit', lambda: exit(), 370)
    Menu(root, 'Update Accounts (temp)', UpdateDictFile, 430)

    #---Set main menu window screen position
    fw = 226
    fh = 600
    sw = root.winfo_screenwidth()
    sh = root.winfo_screenheight()
    xc = (sw/8) - (226/8)
    yc = (sh/6) - (600/6)
    root.geometry('%dx%d+%d+%d' % (fw, fh, xc, yc))


    root.mainloop()

    """
        if fl1 == 'Reformat':
            ReformatDictFile()
    """
    
    exit()

if __name__ == '__main__':
    main()