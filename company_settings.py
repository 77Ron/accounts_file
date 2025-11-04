#Settings

import tkinter as tk
from tkinter import ttk
from tkinter.ttk import *
from company_info import *

def Settings():
    
    root = tk.Toplevel() 
    root.title(company_name)

    label = tk.Label(root, text=company_name+" Settings", font=('centaur', 21, 'bold'),
                   foreground="gray25", background='white smoke') 
    label.pack() 

    tabControl = ttk.Notebook(root, width = '380p', height = '480p')
    tab1 = tk.Frame(tabControl, background=bgcol)
    tab2 = tk.Frame(tabControl, background=bgcol)
    tab3 = tk.Frame(tabControl, background=bgcol)
    tab4 = tk.Frame(tabControl, background=bgcol)
    tabControl.add(tab1, text='Departments')
    tabControl.add(tab2, text='Appearance')
    tabControl.add(tab3, text='Calendar')
    tabControl.add(tab4, text='Security')
    tabControl.pack(expand=1, fill="both")
