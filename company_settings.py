#Settings

from accounts_dictionary import *


def Settings():
    
    root = tk.Tk() 
    root.title(company_name)
    s = Style()
    s.configure('Settings.TFrame', background = bgcol, foreground = 'black')
    #s = Style()
    #s.configure('TNotebook.Tab', font=('centaur','21','bold') )
    label = ttk.Label(root, text=company_name+" Settings", font=('centaur', 21, 'bold'),
                   foreground="gray25", background='white smoke') 
    label.pack() 

    tabControl = ttk.Notebook(root)
    tab1 = ttk.Frame(tabControl, style='Settings.TFrame', width = '400p', height = '500p')
    tab2 = ttk.Frame(tabControl, style='Settings.TFrame', width = '400p', height = '500p')
    tab3 = ttk.Frame(tabControl, style='Settings.TFrame', width = '400p', height = '500p')
    tabControl.add(tab1, text='Departments')
    tabControl.add(tab2, text='Appearance')
    tabControl.add(tab3, text='Security')
    tabControl.pack(expand=1, fill="both")

    root.mainloop()
