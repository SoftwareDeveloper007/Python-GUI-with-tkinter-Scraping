try:
    import tkinter as tk
    from tkinter import messagebox
except:
    import Tkinter as tk
    import tkMessageBox as messagebox
from tkinter import *
import ttk
import time
import webbrowser
from scraper.axios_scraper import AXIOS_Scraper

color = ["#efefe9", "#e4e4dd"]

def AXIOS_GUI(canvas):
    frame = tk.Frame(canvas)
    frame.pack()
    scraper = AXIOS_Scraper()
    scraper.startScraping()

    labelframe = tk.LabelFrame(frame, text=" AXIOS - Health Care ")
    labelframe.configure(bg="white", fg="#e26306", font=('courier', 15, 'bold'),
                         relief="sunken", labelanchor="n")
    labelframe.pack()

    label_list_8(labelframe, "Date", "Author", "Title", "Content", 0, "black", ('Times', 10, 'bold'))

    for i, line in enumerate(scraper.output_data):
        label_list_8(labelframe, line[0], line[1], line[2], line[3], i + 1)

    print('AXIOS GUI is made!')

    frame.update_idletasks()
    return frame

def label_list_8(labelframe, data1, data2, data3, data4, ind, foreground="black", fnt=('Times', 10, 'normal')):
    frame = tk.Frame(labelframe)
    frame.configure(background=color[ind % 2])
    frame.pack(padx=5, pady=5, ipadx=5, ipady=5)

    labelVariable_1 = tk.StringVar()
    label_1 = tk.Label(frame, textvariable=labelVariable_1,
                          width=7, wraplength=49,
                          anchor="nw", justify="left",
                          fg=foreground, bg=color[ind % 2],
                          font=fnt)
    label_1.grid(column=0, row=ind, sticky="W",
                    padx=5, pady=5, ipadx=5, ipady=5)

    labelVariable_1.set(data1)

    labelVariable_2 = tk.StringVar()
    label_2 = tk.Label(frame, textvariable=labelVariable_2,
                            width=12, wraplength=84,
                            anchor="nw", justify="left",
                            fg=foreground, bg=color[ind % 2],
                            font=fnt)
    label_2.grid(column=1, row=ind, sticky="W",
                      padx=5, pady=5, ipadx=5, ipady=5)
    labelVariable_2.set(data2)

    labelVariable_3 = tk.StringVar()
    label_3 = tk.Label(frame, textvariable=labelVariable_3,
                           width=31, wraplength=217,
                           anchor="nw", justify="left",
                           fg=foreground, bg=color[ind % 2],
                           font=fnt)
    label_3.grid(column=2, row=ind, sticky="W",
                     padx=5, pady=5, ipadx=5, ipady=5)
    labelVariable_3.set(data3)

    labelVariable_4 = tk.StringVar()
    label_4 = tk.Label(frame, textvariable=labelVariable_4,
                                 width=100, wraplength=700,
                                 anchor="nw", justify="left",
                                 fg=foreground, bg=color[ind % 2],
                                 font=fnt)
    label_4.grid(column=3, row=ind, sticky="W",
                           padx=5, pady=5, ipadx=5, ipady=5)
    labelVariable_4.set(data4)