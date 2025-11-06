#Calendar

import tkinter as tk
from tkinter import ttk
from tkinter.ttk import *
from tkcalendar import Calendar
from company_info import *

def CalendarView():

    root = tk.Toplevel()
    root.title(company_name)
    root.geometry("500x500")
    
    #---Set window screen position
    fw = 550
    fh = 700
    sw = root.winfo_screenwidth()
    sh = root.winfo_screenheight()
    xc = (sw/2) - (550/2)
    yc = (sh/6) - (600/6)
    root.geometry('%dx%d+%d+%d' % (fw, fh, xc, yc))

    label = ttk.Label(root, text=company_name+" Calendar", font=('centaur', 21, 'bold'), 
                      foreground="gray25", background='white smoke') 
    label.pack() 

    cal = Calendar(root, selectmode = 'day', year = 2025, month = 11, day = 22, 
                   background=bgcol, foreground='white smoke')
    cal.pack(fill='both', expand=True, padx= 75, pady = 75, anchor = 'n')

    Button(root, text = "Select Date", command = lambda: date.config(text= cal.get_date())).pack(pady = 20)

    """""
    xdc, ydc = cal._get_day_coords(date)
    if xdc is not None:
        cal._calendar[xdc][ydc].state(['disabled'])
    """

    date = Label(root, text = "")
    date.pack(pady = 20)
