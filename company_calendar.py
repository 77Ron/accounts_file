#Calendar


from accounts_dictionary import *
from tkcalendar import Calendar

def CalendarView():

    root = tk.Tk()
    root.title(company_name)
    root.geometry("500x500")
    label = ttk.Label(root, text=company_name+" Calendar", font=('centaur', 21, 'bold'), foreground="gray25", background='white smoke') 
    label.pack() 

    cal = Calendar(root, selectmode = 'day', year = 2025, month = 11, day = 22, background=bgcol, foreground='white smoke')

    cal.pack(fill='both', expand=True, pady = 20)

    def grad_date():
        date.config(text = "Selected Date is: " + cal.get_date())

    Button(root, text = "Get Date", command = grad_date).pack(pady = 20)

    date = Label(root, text = "")
    date.pack(pady = 20)

    root.mainloop()
