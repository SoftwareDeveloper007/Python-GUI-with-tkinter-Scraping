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
from scraper.cms_scraper import CMS_Scraper

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

    label_list_5(labelframe, "PROPOSED/DRAFT LCD ID#", "PROPOSED/DRAFT LCD TITLE", "CONTRACTOR NAME",
               "PROPOSED/DRAFT STATUS", "COMMENT PERIOD START DATE", "COMMENT PERIOD END DATE",
               "DATE OF RELEASE FOR NOTICE", '', 0, "black", ('Times', 10, 'bold'))

    for i, line in enumerate(scraper.output_data):
        label_list_5(labelframe, line[0], line[1], line[2], line[3], line[4], line[5], line[6], scraper.urls[i], i+1)

    print('CMS GUI is made!')

    frame.update_idletasks()
    return frame

def label_list_5(labelframe, data1, data2, data3, data4, data5, data6, data7, url, ind,
               foreground="black", fnt=('Times', 10, 'normal')):
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


    def open_url(event=None):
        webbrowser.open_new(url)

    def blue_text(event=None):
        label_1.config(fg="blue")

    def white_text(event=None):
        label_1.config(fg="white")

    def black_text(event=None):
        label_1.config(fg="black")

    def green_text(event=None):
        label_1.config(fg="green")

    if url is not '':
        label_1.bind("<Button-1>", open_url)
        label_1.bind("<Enter>", blue_text)
        label_1.bind("<Leave>", black_text)


    labelVariable_2 = tk.StringVar()
    label_2 = tk.Label(frame, textvariable=labelVariable_2,
                                  width=50, wraplength=350,
                                  anchor="nw", justify="left",
                                  fg=foreground, bg=color[ind % 2],
                                  font=fnt)
    label_2.grid(column=1, row=ind, sticky="W",
                            padx=5, pady=5, ipadx=5, ipady=5)
    labelVariable_2.set(data2)

    labelVariable_3 = tk.StringVar()
    label_3 = tk.Label(frame, textvariable=labelVariable_3,
                                width=15, wraplength=105,
                                anchor="nw", justify="left",
                                fg=foreground, bg=color[ind % 2],
                                font=fnt)
    label_3.grid(column=2, row=ind, sticky="W",
                          padx=5, pady=5, ipadx=5, ipady=5)
    labelVariable_3.set(data3)

    labelVariable_4 = tk.StringVar()
    label_4 = tk.Label(frame, textvariable=labelVariable_4,
                                  width=15, wraplength=105,
                                  anchor="nw", justify="left",
                                  fg=foreground, bg=color[ind % 2],
                                  font=fnt)
    label_4.grid(column=3, row=ind, sticky="W",
                            padx=5, pady=5, ipadx=5, ipady=5)
    labelVariable_4.set(data4)

    labelVariable_5 = tk.StringVar()
    label_5 = tk.Label(frame, textvariable=labelVariable_5,
                                width=15, wraplength=105,
                                anchor="nw", justify="left",
                                fg=foreground, bg=color[ind % 2],
                                font=fnt)
    label_5.grid(column=4, row=ind, sticky="W",
                          padx=5, pady=5, ipadx=5, ipady=5)
    labelVariable_5.set(data5)

    labelVariable_6 = tk.StringVar()
    label_6 = tk.Label(frame, textvariable=labelVariable_6,
                                width=15, wraplength=105,
                                anchor="nw", justify="left",
                                fg=foreground, bg=color[ind % 2],
                                font=fnt)
    label_6.grid(column=5, row=ind, sticky="W",
                          padx=5, pady=5, ipadx=5, ipady=5)
    labelVariable_6.set(data6)

    labelVariable_7 = tk.StringVar()
    label_7 = tk.Label(frame, textvariable=labelVariable_7,
                              width=15, wraplength=105,
                              anchor="nw", justify="left",
                              fg=foreground, bg=color[ind % 2],
                              font=fnt)
    label_7.grid(column=6, row=ind, sticky="W",
                        padx=5, pady=5, ipadx=5, ipady=5)
    labelVariable_7.set(data7)

