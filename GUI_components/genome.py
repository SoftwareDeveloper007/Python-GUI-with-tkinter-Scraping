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

    label_list_7(labelframe, "Date", "Content", 0, "black", ('Times', 10, 'bold'))

    for i, line in enumerate(scraper.output_data):
        label_list_7(labelframe, line[0], line[1], i + 1)

    print('GENOME GUI is made!')

    frame.update_idletasks()
    return frame

def label_list_7(labelframe, data1, data2, ind, foreground="black", fnt=('Times', 10, 'normal')):
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
                            width=150, wraplength=1050,
                            anchor="nw", justify="left",
                            fg=foreground, bg=color[ind % 2],
                            font=fnt)
    label_2.grid(column=1, row=ind, sticky="W",
                      padx=5, pady=5, ipadx=5, ipady=5)
    labelVariable_2.set(data2)


