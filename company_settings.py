#Settings

from accounts_dictionary import *


def Settings():
    
    root = tk.Tk() 
    root.title(company_name)

    label = tk.Label(root, text=company_name+" Settings", font=('centaur', 21, 'bold'),
                   foreground="gray25", background='white smoke') 
    label.pack() 

    tabControl = ttk.Notebook(root, width = '400p', height = '500p')
    tab1 = tk.Frame(tabControl)
    tab2 = tk.Frame(tabControl)
    tab3 = tk.Frame(tabControl)
    tab4 = tk.Frame(tabControl)
    tabControl.add(tab1, text='Departments')
    tabControl.add(tab2, text='Appearance')
    tabControl.add(tab3, text='Calendar')
    tabControl.add(tab4, text='Security')
    tabControl.pack(expand=1, fill="both")

    root.mainloop()
