try:
    import tkinter as tk
    from tkinter import messagebox
except:
    import Tkinter as tk
    import tkMessageBox as messagebox

import ttk
import time
from scraper.fda_scraper import FDA_MedWatch

color = ["#efefe9", "#e4e4dd"]


def FDA_MedWatch_GUI(canvas):
    frame = tk.Frame(canvas)
    frame.pack()
    parse_ctrl = FDA_MedWatch()
    parse_ctrl.parse()

    total_cnt = len(parse_ctrl.dates)
    links = parse_ctrl.dates
    titles = parse_ctrl.titles
    descs = parse_ctrl.descs
    dates = parse_ctrl.dates

    labelframe = tk.LabelFrame(frame, text=" FDA MedWatch ")
    labelframe.pack()
    labelframe.configure(bg="white", fg="#e26306", font=('courier', 15, 'bold'),
                         relief="sunken", labelanchor="n")
    # labelframe.grid(row=0, sticky='WE', padx=5, pady=15, ipadx=5, ipady=5)

    for i in range(total_cnt):
        label_list_1(labelframe, titles[i], descs[i], dates[i], i)

    print('FDA GUI is made!')
    frame.update_idletasks()
    return frame


def label_list_1(labelframe, data1, data2, data3, ind):
    frame = tk.Frame(labelframe)
    frame.configure(background=color[ind % 2])
    frame.pack(padx=5, pady=5, ipadx=5, ipady=5)

    labelVariable_1 = tk.StringVar()
    label_1 = tk.Label(frame, textvariable=labelVariable_1,
                           width=70, wraplength=490,
                           anchor="nw", justify="left",
                           fg="black", bg=color[ind % 2])
    label_1.grid(column=0, row=ind, sticky="W",
                     padx=3, pady=3, ipadx=3, ipady=3)

    labelVariable_1.set(data1)

    labelVariable_2 = tk.StringVar()
    label_2 = tk.Label(frame, textvariable=labelVariable_2,
                          width=75, wraplength=525,
                          anchor="nw", justify="left",
                          fg="black", bg=color[ind % 2])
    label_2.grid(column=1, row=ind, sticky="W",
                    padx=3, pady=3, ipadx=3, ipady=3)
    labelVariable_2.set(data2)

    labelVariable_3 = tk.StringVar()
    label_3 = tk.Label(frame, textvariable=labelVariable_3,
                          width=10, wraplength=80,
                          anchor="nw", justify="left",
                          fg="black", bg=color[ind % 2])
    label_3.grid(column=2, row=ind, sticky="W",
                    padx=3, pady=3, ipadx=3, ipady=3)
    labelVariable_3.set(data3)
