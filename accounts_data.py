# Write, update, and delete account info in a saved dictionary file.
# Display file by department and surname initial.
# Display account table with pandas.
# Display account graph with matplotlib.
# 
# ------- Not available at this time. ----------
# Create or update a MySQL database from the account dictionary file.
# Import accounts from a MySQL database.
# Import accounts from a text file.


from accounts_dictionary import *
from company_settings import *


def main():

    root = tk.Tk() 
    root.title(company_name)
    Style().configure('Menu.TFrame', background=bgcol, foreground = 'black')
    label = ttk.Label(root, text = "Main Menu ", font=('centaur', 21, 'bold'),
                    foreground="gray25", background="white smoke") 
    label.pack() 
    frame = ttk.Frame(root, style='Menu.TFrame', width = '200p', height = '500p')
    frame.pack()

    M1_btn = tk.Button(root,text = 'Update Accounts',command = UpdateDictFile, width = 20, font=('calibre', 10, 'bold'), bg=btcol, fg='black')
    M1_btn.place(x=30, y=70)
    M2_btn = tk.Button(root,text = 'Print Accounts', command = PrintDictFile, width = 20, font=('calibre', 10, 'bold'), bg=btcol, fg='black')
    M2_btn.place(x=30, y=100)
    M3_btn = tk.Button(root,text = 'Display Table', command = TableDictFile, width = 20, font=('calibre', 10, 'bold'), bg=btcol, fg='black')
    M3_btn.place(x=30, y=130)
    M4_btn = tk.Button(root,text = 'Display Graph', command = GraphDictFile, width = 20, font=('calibre', 10, 'bold'), bg=btcol, fg='black')
    M4_btn.place(x=30, y=160)
    M4_btn = tk.Button(root,text = 'Database Update', command = DatabaseUpdate, width = 20, font=('calibre', 10, 'bold'), bg=btcol, fg='black')
    M4_btn.place(x=30, y=190)
    M4_btn = tk.Button(root,text = 'Database Import', command = DatabaseImport, width = 20, font=('calibre', 10, 'bold'), bg=btcol, fg='black')
    M4_btn.place(x=30, y=220)
    M4_btn = tk.Button(root,text = 'Text File Import', command = TextFileImport, width = 20, font=('calibre', 10, 'bold'), bg=btcol, fg='black')
    M4_btn.place(x=30, y=250)
    M5_btn = tk.Button(root,text = 'Print Log File', command = LogFile, width = 20, font=('calibre', 10, 'bold'), bg=btcol, fg='black')
    M5_btn.place(x=30, y=280)
    M6_btn = tk.Button(root,text = 'Settings', command = Settings, width = 20, font=('calibre', 10, 'bold'), bg=btcol, fg='black')
    M6_btn.place(x=30, y=310)
    M7_btn = tk.Button(root,text = 'Exit', command = lambda: exit(), width = 20, font=('calibre', 10, 'bold'), bg=btcol, fg='black')
    M7_btn.place(x=30, y=340)

    root.mainloop()

    """
        elif fl1 == 'Reformat':
            ReformatDictFile()
    """
    
    exit()

if __name__ == '__main__':
    main()