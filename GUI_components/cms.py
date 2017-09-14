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
from scraper.scraper_3 import CMS_Scraper

color = ["#efefe9", "#e4e4dd"]

def CMS_GUI(canvas):
    frame = tk.Frame(canvas)
    frame.pack()
    scraper = CMS_Scraper()
    scraper.startScraping()

    labelframe = tk.LabelFrame(frame, text=" CMS Proposed/Draft Local Coverage Determinations (LCDs) Status Report ")
    labelframe.configure(bg="white", fg="#e26306", font=('courier', 15, 'bold'),
                         relief="sunken", labelanchor="n")
    labelframe.pack()

    label_list(labelframe, "PROPOSED/DRAFT LCD ID#", "PROPOSED/DRAFT LCD TITLE", "CONTRACTOR NAME",
               "PROPOSED/DRAFT STATUS", "COMMENT PERIOD START DATE", "COMMENT PERIOD END DATE",
               "DATE OF RELEASE FOR NOTICE", '', 0, "black", ('Times', 10, 'bold'))

    for i, line in enumerate(scraper.output_data):
        label_list(labelframe, line[0], line[1], line[2], line[3], line[4], line[5], line[6], scraper.urls[i], i+1)

    print('CMS GUI is made!')

    frame.update_idletasks()
    return frame

def label_list(labelframe, ID, title, contractor, status, start_date, end_date, release_date, url, ind,
               foreground="black", fnt=('Times', 10, 'normal')):
    frame = tk.Frame(labelframe)
    frame.configure(background=color[ind % 2])
    frame.pack(padx=5, pady=5, ipadx=5, ipady=5)

    labelVariable_ID = tk.StringVar()
    label_ID = tk.Label(frame, textvariable=labelVariable_ID,
                                   width=10, wraplength=70,
                                   anchor="nw", justify="left",
                                   fg=foreground, bg=color[ind % 2],
                                   font=fnt)
    label_ID.grid(column=0, row=ind, columnspan=5, sticky="W",
                             padx=5, pady=5, ipadx=5, ipady=5)

    labelVariable_ID.set(ID)


    def open_url(event=None):
        webbrowser.open_new(url)

    def blue_text(event=None):
        label_ID.config(fg="blue")

    def white_text(event=None):
        label_ID.config(fg="white")

    def black_text(event=None):
        label_ID.config(fg="black")

    def green_text(event=None):
        label_ID.config(fg="green")

    if url is not '':
        label_ID.bind("<Button-1>", open_url)
        label_ID.bind("<Enter>", blue_text)
        label_ID.bind("<Leave>", black_text)


    labelVariable_title = tk.StringVar()
    label_title = tk.Label(frame, textvariable=labelVariable_title,
                                  width=50, wraplength=350,
                                  anchor="nw", justify="left",
                                  fg=foreground, bg=color[ind % 2],
                                  font=fnt)
    label_title.grid(column=6, row=ind, columnspan=12, sticky="W",
                            padx=5, pady=5, ipadx=5, ipady=5)
    labelVariable_title.set(title)

    labelVariable_contractor = tk.StringVar()
    label_contractor = tk.Label(frame, textvariable=labelVariable_contractor,
                                width=15, wraplength=105,
                                anchor="nw", justify="left",
                                fg=foreground, bg=color[ind % 2],
                                font=fnt)
    label_contractor.grid(column=19, row=ind, columnspan=12, sticky="W",
                          padx=5, pady=5, ipadx=5, ipady=5)
    labelVariable_contractor.set(contractor)

    labelVariable_status = tk.StringVar()
    label_status = tk.Label(frame, textvariable=labelVariable_status,
                                  width=15, wraplength=105,
                                  anchor="nw", justify="left",
                                  fg=foreground, bg=color[ind % 2],
                                  font=fnt)
    label_status.grid(column=32, row=ind, columnspan=12, sticky="W",
                            padx=5, pady=5, ipadx=5, ipady=5)
    labelVariable_status.set(status)

    labelVariable_start_date = tk.StringVar()
    label_start_date = tk.Label(frame, textvariable=labelVariable_start_date,
                                width=15, wraplength=105,
                                anchor="nw", justify="left",
                                fg=foreground, bg=color[ind % 2],
                                font=fnt)
    label_start_date.grid(column=45, row=ind, columnspan=5, sticky="W",
                          padx=5, pady=5, ipadx=5, ipady=5)
    labelVariable_start_date.set(start_date)

    labelVariable_end_date = tk.StringVar()
    label_end_date = tk.Label(frame, textvariable=labelVariable_end_date,
                                width=15, wraplength=105,
                                anchor="nw", justify="left",
                                fg=foreground, bg=color[ind % 2],
                                font=fnt)
    label_end_date.grid(column=51, row=ind, columnspan=5, sticky="W",
                          padx=5, pady=5, ipadx=5, ipady=5)
    labelVariable_end_date.set(end_date)

    labelVariable_release_date = tk.StringVar()
    label_release_date = tk.Label(frame, textvariable=labelVariable_release_date,
                              width=15, wraplength=105,
                              anchor="nw", justify="left",
                              fg=foreground, bg=color[ind % 2],
                              font=fnt)
    label_release_date.grid(column=57, row=ind, columnspan=5, sticky="W",
                        padx=5, pady=5, ipadx=5, ipady=5)
    labelVariable_release_date.set(release_date)