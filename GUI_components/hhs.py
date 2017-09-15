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
from scraper.scraper_4 import HHS_Scraper

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

    label_list(labelframe, "Date", "Agency", "Title", "Description", 0, "black", ('Times', 10, 'bold'))

    for i, line in enumerate(scraper.output_data):
        label_list(labelframe, line[2], line[1], line[0], line[3], i + 1)

    print('HHS GUI is made!')

    frame.update_idletasks()
    return frame


def label_list(labelframe, date, agency, title, description, ind, foreground="black", fnt=('Times', 10, 'normal')):
    frame = tk.Frame(labelframe)
    frame.configure(background=color[ind % 2])
    frame.pack(padx=5, pady=5, ipadx=5, ipady=5)

    labelVariable_date = tk.StringVar()
    label_date = tk.Label(frame, textvariable=labelVariable_date,
                          width=10, wraplength=70,
                          anchor="nw", justify="left",
                          fg=foreground, bg=color[ind % 2],
                          font=fnt)
    label_date.grid(column=0, row=ind, columnspan=5, sticky="W",
                    padx=5, pady=5, ipadx=5, ipady=5)

    labelVariable_date.set(date)

    labelVariable_agency = tk.StringVar()
    label_agency = tk.Label(frame, textvariable=labelVariable_agency,
                            width=50, wraplength=350,
                            anchor="nw", justify="left",
                            fg=foreground, bg=color[ind % 2],
                            font=fnt)
    label_agency.grid(column=6, row=ind, columnspan=12, sticky="W",
                      padx=5, pady=5, ipadx=5, ipady=5)
    labelVariable_agency.set(agency)

    labelVariable_title = tk.StringVar()
    label_title = tk.Label(frame, textvariable=labelVariable_title,
                           width=15, wraplength=105,
                           anchor="nw", justify="left",
                           fg=foreground, bg=color[ind % 2],
                           font=fnt)
    label_title.grid(column=19, row=ind, columnspan=12, sticky="W",
                     padx=5, pady=5, ipadx=5, ipady=5)
    labelVariable_title.set(title)

    labelVariable_description = tk.StringVar()
    label_description = tk.Label(frame, textvariable=labelVariable_description,
                                 width=15, wraplength=105,
                                 anchor="nw", justify="left",
                                 fg=foreground, bg=color[ind % 2],
                                 font=fnt)
    label_description.grid(column=32, row=ind, columnspan=12, sticky="W",
                           padx=5, pady=5, ipadx=5, ipady=5)
    labelVariable_description.set(description)
