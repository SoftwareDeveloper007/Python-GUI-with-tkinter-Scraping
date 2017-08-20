try:
    import tkinter as tk
    from tkinter import messagebox
except:
    import Tkinter as tk
    import tkMessageBox as messagebox

import ttk
import time
from scraper.scraper_1 import FDA_MedWatch

color = ["#329fea", "#cc93e8"]


def FDA_MedWatch_GUI(frame):
    parse_ctrl = FDA_MedWatch()
    parse_ctrl.parse()

    total_cnt = len(parse_ctrl.dates)
    links = parse_ctrl.dates
    titles = parse_ctrl.titles
    descs = parse_ctrl.descs
    dates = parse_ctrl.dates

    labelframe = tk.LabelFrame(frame, text=" FDA MedWatch ")
    labelframe.configure(bg="#4f617b", fg="#e26306", font=('courier', 15, 'bold'),
                         relief="sunken", labelanchor="n")
    # labelframe.grid(row=0, sticky='WE', padx=5, pady=15, ipadx=5, ipady=5)
    labelframe.pack()
    for i in range(total_cnt):
        label_list(labelframe, titles[i], descs[i], dates[i], i)

    print('FDA GUI is made!')


def label_list(labelframe, title, desc, date, ind):
    frame = tk.Frame(labelframe)
    frame.configure(background=color[ind % 2])
    frame.pack(padx=5, pady=5, ipadx=5, ipady=5)

    labelVariable_title = tk.StringVar()
    label_title = tk.Label(frame, textvariable=labelVariable_title,
                           width=50, wraplength=350,
                           anchor="nw", justify="left",
                           fg="black", bg=color[ind % 2])
    label_title.grid(column=0, row=ind, columnspan=7, sticky="W",
                     padx=3, pady=3, ipadx=3, ipady=3)

    labelVariable_title.set(title)

    labelVariable_desc = tk.StringVar()
    label_desc = tk.Label(frame, textvariable=labelVariable_desc,
                          width=70, wraplength=490,
                          anchor="nw", justify="left",
                          fg="black", bg=color[ind % 2])
    label_desc.grid(column=9, row=ind, columnspan=50, sticky="W",
                    padx=3, pady=3, ipadx=3, ipady=3)
    labelVariable_desc.set(desc)

    labelVariable_date = tk.StringVar()
    label_date = tk.Label(frame, textvariable=labelVariable_date,
                          width=10, wraplength=80,
                          anchor="nw", justify="left",
                          fg="black", bg=color[ind % 2])
    label_date.grid(column=61, row=ind, columnspan=5, sticky="W",
                    padx=3, pady=3, ipadx=3, ipady=3)
    labelVariable_date.set(date)
