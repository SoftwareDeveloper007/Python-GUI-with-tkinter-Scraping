try:
    import tkinter as tk
    from tkinter import messagebox
except:
    import Tkinter as tk
    import tkMessageBox as messagebox

import ttk
import time
from scraper.drug_scraper import Drug_Recalls

color = ["#efefe9", "#e4e4dd"]
    
def Drug_GUI(canvas):
    frame = tk.Frame(canvas)
    frame.pack()
    parse_ctrl = Drug_Recalls()
    parse_ctrl.parse()

    labelframe = tk.LabelFrame(frame, text="Drug Store")
    labelframe.pack()
    labelframe.configure(bg="white", fg="#e26306", font=('courier', 15, 'bold'),
                         relief="sunken", labelanchor="n")
    # labelframe.grid(row=i, sticky='WE', padx=5, pady=15, ipadx=5, ipady=5)


    i = 0
    label_list_3(labelframe, "Date", "Brand Name", "Production Description", "Reason/Problem", "Company", i)
    i = 1
    for line in parse_ctrl.total_data:
        label_list_3(labelframe, line['date'], line['brand'], line['description'], line['problem'],
                        line['company'], i)
        i += 1

    print('Drug GUI is made!')

    frame.update_idletasks()
    return frame

def label_list_3(labelframe, data1, data2, data3, data4, data5, ind):
    frame = tk.Frame(labelframe)
    frame.configure(background=color[ind % 2])
    frame.pack(padx=5, pady=5, ipadx=5, ipady=5)

    ''' data1 '''
    labelVariable_1 = tk.StringVar()
    label_1 = tk.Label(frame, textvariable=labelVariable_1,
                           width = 10, wraplength=70,
                           anchor="nw", justify="left",
                           fg="black", bg=color[ind % 2])
    label_1.grid(column=0, row=ind, sticky="W",
                     padx=3, pady=3, ipadx=3, ipady=3)

    labelVariable_1.set(data1)

    ''' data2 '''
    labelVariable_2 = tk.StringVar()
    label_2 = tk.Label(frame, textvariable=labelVariable_2,
                          width = 20, wraplength=140,
                          anchor="nw", justify="left",
                          fg="black", bg=color[ind % 2])
    label_2.grid(column=1, row=ind, sticky="W",
                    padx=3, pady=3, ipadx=3, ipady=3)
    labelVariable_2.set(data2)

    ''' data3 '''
    labelVariable_3 = tk.StringVar()
    label_3 = tk.Label(frame, textvariable=labelVariable_3,
                          width = 55, wraplength=385,
                          anchor="nw", justify="left",
                          fg="black", bg=color[ind % 2])
    label_3.grid(column=2, row=ind, sticky="W",
                    padx=3, pady=3, ipadx=3, ipady=3)
    labelVariable_3.set(data3)

    ''' data4 '''
    labelVariable_4 = tk.StringVar()
    label_4 = tk.Label(frame, textvariable=labelVariable_4,
                          width = 45, wraplength=315,
                          anchor="nw", justify="left",
                          fg="black", bg=color[ind % 2])
    label_4.grid(column=3, row=ind, sticky="W",
                    padx=3, pady=3, ipadx=3, ipady=3)
    labelVariable_4.set(data4)

    ''' data5 '''
    labelVariable_5 = tk.StringVar()
    label_5 = tk.Label(frame, textvariable=labelVariable_5,
                          width = 20, wraplength=140,
                          anchor="nw", justify="left",
                          fg="black", bg=color[ind % 2])
    label_5.grid(column=4, row=ind, sticky="W",
                    padx=3, pady=3, ipadx=3, ipady=3)
    labelVariable_5.set(data5)



