#Accounts desktop

#Move UI from console to desktop screen.

import tkinter as tk
from tkinter import ttk
from company_info import *

root = tk.Tk() 

root.title("Account Balance File")

label = ttk.Label(root, text=company_name+" Account Balances", font='timesroman', foreground="white", background="black") 
label.pack() 

button = ttk.Button(root, text="Click Me", command=lambda: print("Button clicked!")) 
button.pack()

frame = ttk.Frame(root, width = '400p', height = '500p')
frame.pack()

root.mainloop()