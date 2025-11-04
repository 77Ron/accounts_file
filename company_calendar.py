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
    
    label = ttk.Label(root, text=company_name+" Calendar", font=('centaur', 21, 'bold'), foreground="gray25", background='white smoke') 
    label.pack() 

    cal = Calendar(root, selectmode = 'day', year = 2025, month = 11, day = 22, background=bgcol, foreground='white smoke')
    cal.pack(fill='both', expand=True, pady = 20)

    Button(root, text = "Select Date", command = lambda: date.config(text= cal.get_date())).pack(pady = 20)

    """""
    xc, yc = cal._get_day_coords(date)
    if xc is not None:
        cal._calendar[xc][yc].state(['disabled'])
    """

    date = Label(root, text = "")
    date.pack(pady = 20)
