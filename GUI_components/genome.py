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
from scraper.genome_scraper import GENOME_Scraper

color = ["#efefe9", "#e4e4dd"]


def GENOME_GUI(canvas):
    frame = tk.Frame(canvas)
    frame.pack()
    scraper = GENOME_Scraper()
    scraper.startScraping()

    labelframe = tk.LabelFrame(frame, text=" genomeweb – Breaking News ")
    labelframe.configure(bg="white", fg="#e26306", font=('courier', 15, 'bold'),
                         relief="sunken", labelanchor="n")
    labelframe.pack()

    label_list(labelframe, "Date", "Content", 0, "black", ('Times', 10, 'bold'))

    for i, line in enumerate(scraper.output_data):
        label_list(labelframe, line[0], line[1], i + 1)

    print('GENOME GUI is made!')

    frame.update_idletasks()
    return frame


def label_list(labelframe, date, content, ind, foreground="black", fnt=('Times', 10, 'normal')):
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

    labelVariable_content = tk.StringVar()
    label_content = tk.Label(frame, textvariable=labelVariable_content,
                            width=150, wraplength=1050,
                            anchor="nw", justify="left",
                            fg=foreground, bg=color[ind % 2],
                            font=fnt)
    label_content.grid(column=6, row=ind, columnspan=12, sticky="W",
                      padx=5, pady=5, ipadx=5, ipady=5)
    labelVariable_content.set(content)


