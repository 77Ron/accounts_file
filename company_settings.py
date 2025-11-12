#Settings

import tkinter as tk
from tkinter import ttk
from tkinter.ttk import *
from company_info import *

def Settings():
    
    root = tk.Toplevel() 
    root.title(company_name)

    #---Set window screen position
    fw = 550
    fh = 600
    sw = root.winfo_screenwidth()
    sh = root.winfo_screenheight()
    xc = (sw/2) - (550/2)
    yc = (sh/6) - (600/6)
    root.geometry('%dx%d+%d+%d' % (fw, fh, xc, yc))

    label = tk.Label(root, text=company_name+" Settings", font=('centaur', 21, 'bold'),
                   foreground="gray25", background='white smoke') 
    label.pack() 

    tabControl = ttk.Notebook(root, width = '550p', height = '600p')
    tab1 = tk.Frame(tabControl, background=bgcol)
    tab2 = tk.Frame(tabControl, background=bgcol)
    tab3 = tk.Frame(tabControl, background=bgcol)
    tab4 = tk.Frame(tabControl, background=bgcol)
    tabControl.add(tab1, text='Main')
    tabControl.add(tab2, text='Appearance')
    tabControl.add(tab3, text='Calendar')
    tabControl.add(tab4, text='Security')
    tabControl.pack(expand=1, fill="both")
