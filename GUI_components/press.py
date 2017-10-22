try:
    import tkinter as tk
    from tkinter import messagebox
except:
    import Tkinter as tk
    import tkMessageBox as messagebox

import ttk
import time
from scraper.press_scraper import Press_Announcements

color = ["#efefe9", "#e4e4dd"]

def Press_GUI(canvas):
    frame = tk.Frame(canvas)

    parse_ctrl = Press_Announcements()
    parse_ctrl.parse()

    body_cnt = len(parse_ctrl.total_data)

    mainlabelframe = tk.LabelFrame(frame, text="Press Announcements")
    mainlabelframe.pack()
    mainlabelframe.configure(bg="white", fg="#e26306", font=('courier', 15, 'bold'),
                         relief="sunken", labelanchor="n")
    # labelframe.grid(row=i, sticky='WE', padx=5, pady=15, ipadx=5, ipady=5)

    labelframes = []
    k = 0
    for i in range(body_cnt):
        labelframe = tk.LabelFrame(mainlabelframe, text=parse_ctrl.month_name[i])
        labelframe.configure(bg="white", fg="#3233ea", font=('courier', 12, 'bold', 'italic'),
                              relief="flat", labelanchor="n")
        #labelframe.grid(row=i, sticky='WE', padx=5, pady=15, ipadx=5, ipady=5)
        labelframe.pack()
        labelframes.append(labelframe)

        body_data = parse_ctrl.total_data[i]
        for line in body_data:
            label_list(labelframes, line['date'], line['content'], i, k)
            k += 1

    print('Press GUI is made!')
    frame.update_idletasks()
    return frame

def label_list(labelframes, date, content, i, ind):
    frame = tk.Frame(labelframes[i])
    frame.configure(background=color[ind % 2])
    frame.pack(padx=5, pady=5, ipadx=5, ipady=5)

    labelVariable_date = tk.StringVar()
    label_date = tk.Label(frame, textvariable=labelVariable_date,
                           width = 70, wraplength=490,
                           anchor="nw", justify="left",
                           fg="black", bg=color[ind % 2])
    label_date.grid(column=0, row=ind, columnspan = 4, sticky="W",
                     padx=3, pady=3, ipadx=3, ipady=3)

    labelVariable_date.set(date)

    labelVariable_content = tk.StringVar()
    label_content = tk.Label(frame, textvariable=labelVariable_content,
                          width = 90, wraplength=630,
                          anchor="nw", justify="left",
                          fg="black", bg=color[ind % 2])
    label_content.grid(column=9, row=ind, columnspan = 50, sticky="W",
                    padx=3, pady=3, ipadx=3, ipady=3)
    labelVariable_content.set(content)



