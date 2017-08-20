try:
    import tkinter as tk
    from tkinter import messagebox
except:
    import Tkinter as tk
    import tkMessageBox as messagebox

import ttk
import time
from scraper.scraper_1 import Drug_Recalls

color = ["#329fea", "#cc93e8"]
    
def Drug_GUI(frame):
    parse_ctrl = Drug_Recalls()
    parse_ctrl.parse()

    labelframe = tk.LabelFrame(frame, text="Drug Store")
    labelframe.configure(bg="#4f617b", fg="#e26306", font=('courier', 15, 'bold'),
                         relief="sunken", labelanchor="n")
    # labelframe.grid(row=i, sticky='WE', padx=5, pady=15, ipadx=5, ipady=5)
    labelframe.pack()

    i = 0
    label_list(labelframe, "Date", "Brand Name", "Production Description", "Reason/Problem", "Company", i)
    i = 1
    for line in parse_ctrl.total_data:
        label_list(labelframe, line['date'], line['brand'], line['description'], line['problem'],
                        line['company'], i)
        i += 1

    print('Drug GUI is made!')

def label_list(labelframe, date, brand, desc, problem, company, ind):
    frame = tk.Frame(labelframe)
    frame.configure(background=color[ind % 2])
    frame.pack(padx=5, pady=5, ipadx=5, ipady=5)

    ''' Date '''
    labelVariable_date = tk.StringVar()
    label_date = tk.Label(frame, textvariable=labelVariable_date,
                           width = 10, wraplength=70,
                           anchor="nw", justify="left",
                           fg="black", bg=color[ind % 2])
    label_date.grid(column=0, row=ind, columnspan = 1, sticky="W",
                     padx=3, pady=3, ipadx=3, ipady=3)

    labelVariable_date.set(date)

    ''' Brand '''
    labelVariable_brand = tk.StringVar()
    label_brand = tk.Label(frame, textvariable=labelVariable_brand,
                          width = 10, wraplength=70,
                          anchor="nw", justify="left",
                          fg="black", bg=color[ind % 2])
    label_brand.grid(column=2, row=ind, columnspan = 1, sticky="W",
                    padx=3, pady=3, ipadx=3, ipady=3)
    labelVariable_brand.set(brand)

    ''' Description '''
    labelVariable_desc = tk.StringVar()
    label_desc = tk.Label(frame, textvariable=labelVariable_desc,
                          width = 50, wraplength=350,
                          anchor="nw", justify="left",
                          fg="black", bg=color[ind % 2])
    label_desc.grid(column=4, row=ind, columnspan = 10, sticky="W",
                    padx=3, pady=3, ipadx=3, ipady=3)
    labelVariable_desc.set(desc)

    ''' Problem '''
    labelVariable_problem = tk.StringVar()
    label_problem = tk.Label(frame, textvariable=labelVariable_problem,
                          width = 40, wraplength=280,
                          anchor="nw", justify="left",
                          fg="black", bg=color[ind % 2])
    label_problem.grid(column=15, row=ind, columnspan = 7, sticky="W",
                    padx=3, pady=3, ipadx=3, ipady=3)
    labelVariable_problem.set(problem)

    ''' Company '''
    labelVariable_company = tk.StringVar()
    label_company = tk.Label(frame, textvariable=labelVariable_company,
                          width = 10, wraplength=70,
                          anchor="nw", justify="left",
                          fg="black", bg=color[ind % 2])
    label_company.grid(column=23, row=ind, columnspan = 2, sticky="W",
                    padx=3, pady=3, ipadx=3, ipady=3)
    labelVariable_company.set(company)



