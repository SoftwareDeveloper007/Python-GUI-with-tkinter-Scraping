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
from scraper.scraper_6 import AXIOS_Scraper

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

    label_list(labelframe, "Date", "Author", "Title", "Content", 0, "black", ('Times', 10, 'bold'))

    for i, line in enumerate(scraper.output_data):
        label_list(labelframe, line[0], line[1], line[2], line[3], i + 1)

    print('AXIOS GUI is made!')

    frame.update_idletasks()
    return frame

def label_list(labelframe, date, author, title, content, ind, foreground="black", fnt=('Times', 10, 'normal')):
    frame = tk.Frame(labelframe)
    frame.configure(background=color[ind % 2])
    frame.pack(padx=5, pady=5, ipadx=5, ipady=5)

    labelVariable_date = tk.StringVar()
    label_date = tk.Label(frame, textvariable=labelVariable_date,
                          width=7, wraplength=49,
                          anchor="nw", justify="left",
                          fg=foreground, bg=color[ind % 2],
                          font=fnt)
    label_date.grid(column=0, row=ind, columnspan=5, sticky="W",
                    padx=5, pady=5, ipadx=5, ipady=5)

    labelVariable_date.set(date)

    labelVariable_author = tk.StringVar()
    label_author = tk.Label(frame, textvariable=labelVariable_author,
                            width=12, wraplength=84,
                            anchor="nw", justify="left",
                            fg=foreground, bg=color[ind % 2],
                            font=fnt)
    label_author.grid(column=6, row=ind, columnspan=12, sticky="W",
                      padx=5, pady=5, ipadx=5, ipady=5)
    labelVariable_author.set(author)

    labelVariable_title = tk.StringVar()
    label_title = tk.Label(frame, textvariable=labelVariable_title,
                           width=40, wraplength=280,
                           anchor="nw", justify="left",
                           fg=foreground, bg=color[ind % 2],
                           font=fnt)
    label_title.grid(column=19, row=ind, columnspan=12, sticky="W",
                     padx=5, pady=5, ipadx=5, ipady=5)
    labelVariable_title.set(title)

    labelVariable_content = tk.StringVar()
    label_content = tk.Label(frame, textvariable=labelVariable_content,
                                 width=91, wraplength=637,
                                 anchor="nw", justify="left",
                                 fg=foreground, bg=color[ind % 2],
                                 font=fnt)
    label_content.grid(column=32, row=ind, columnspan=12, sticky="W",
                           padx=5, pady=5, ipadx=5, ipady=5)
    labelVariable_content.set(content)