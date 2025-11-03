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
from company_calendar import *

def Menu(root, text1, command1, y1):
    M1_btn = tk.Button(root, text = text1, command = command1, width = 20, font=('calibre', 10, 'bold'), bg=btcol, fg='black')
    M1_btn.place(x=27, y=y1)

def main():

    root = tk.Tk() 
    root.title(company_name)
    s = Style()
    s.configure('Menu.TFrame', background=bgcol, foreground = 'black')
    label = ttk.Label(root, text = "Main Menu", font=('centaur', 21, 'bold'), foreground="gray25", background="white smoke") 
    label.pack() 
    frame = ttk.Frame(root, style='Menu.TFrame', width = '170p', height = '500p')
    frame.pack()

    Menu(root, 'Update Accounts', UpdateDictFile, 70)
    Menu(root, 'Print Accounts', PrintDictFile, 100)
    Menu(root, 'Display Table', TableDictFile, 130)
    Menu(root, 'Display Graph', GraphDictFile, 160)
    Menu(root, 'Database Update', DatabaseUpdate, 190)
    Menu(root, 'Database Import', DatabaseImport, 220)
    Menu(root, 'Text File Import', TextFileImport, 250)
    Menu(root, 'Calendar', CalendarView, 280)
    Menu(root, 'Print Log File', LogFile, 310)
    Menu(root, 'Settings', Settings, 340)
    Menu(root, 'Exit', lambda: exit(), 370)
   
    root.mainloop()

    """
        elif fl1 == 'Reformat':
            ReformatDictFile()
    """
    
    exit()

if __name__ == '__main__':
    main()