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
from scraper.hhs_scraper import HHS_Scraper

color = ["#efefe9", "#e4e4dd"]


def HHS_GUI(canvas):
    frame = tk.Frame(canvas)
    frame.pack()
    scraper = HHS_Scraper()
    scraper.urlGeneration()
    scraper.startScraping()

    labelframe = tk.LabelFrame(frame, text=" Federal Register - HHS ")
    labelframe.configure(bg="white", fg="#e26306", font=('courier', 15, 'bold'),
                         relief="sunken", labelanchor="n")
    labelframe.pack()

    label_list_6(labelframe, "Date", "Agency", "Title", "Description", 0, "black", ('Times', 10, 'bold'))

    for i, line in enumerate(scraper.output_data):
        label_list_6(labelframe, line[2], line[1], line[0], line[3], i + 1)

    print('HHS GUI is made!')

    frame.update_idletasks()
    return frame

def label_list_6(labelframe, data1, data2, data3, data4, ind, foreground="black", fnt=('Times', 10, 'normal')):
    frame = tk.Frame(labelframe)
    frame.configure(background=color[ind % 2])
    frame.pack(padx=5, pady=5, ipadx=5, ipady=5)

    labelVariable_1 = tk.StringVar()
    label_1 = tk.Label(frame, textvariable=labelVariable_1,
                          width=10, wraplength=70,
                          anchor="nw", justify="left",
                          fg=foreground, bg=color[ind % 2],
                          font=fnt)
    label_1.grid(column=0, row=ind, sticky="W",
                    padx=5, pady=5, ipadx=5, ipady=5)

    labelVariable_1.set(data1)

    labelVariable_2 = tk.StringVar()
    label_2 = tk.Label(frame, textvariable=labelVariable_2,
                            width=30, wraplength=210,
                            anchor="nw", justify="left",
                            fg=foreground, bg=color[ind % 2],
                            font=fnt)
    label_2.grid(column=1, row=ind, sticky="W",
                      padx=5, pady=5, ipadx=5, ipady=5)
    labelVariable_2.set(data2)

    labelVariable_3 = tk.StringVar()
    label_3 = tk.Label(frame, textvariable=labelVariable_3,
                           width=45, wraplength=315,
                           anchor="nw", justify="left",
                           fg=foreground, bg=color[ind % 2],
                           font=fnt)
    label_3.grid(column=2, row=ind, sticky="W",
                     padx=5, pady=5, ipadx=5, ipady=5)
    labelVariable_3.set(data3)

    labelVariable_4 = tk.StringVar()
    label_4 = tk.Label(frame, textvariable=labelVariable_4,
                                 width=65, wraplength=455,
                                 anchor="nw", justify="left",
                                 fg=foreground, bg=color[ind % 2],
                                 font=fnt)
    label_4.grid(column=3, row=ind, sticky="W",
                           padx=5, pady=5, ipadx=5, ipady=5)
    labelVariable_4.set(data4)
