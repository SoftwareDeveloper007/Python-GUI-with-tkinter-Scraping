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
from scraper.orange_scraper_new import ORANGE_Scraper_New

color = ["#efefe9", "#e4e4dd"]


def ORANGE_GUI_New(canvas):
    frame = tk.Frame(canvas)
    frame.pack()
    scraper = ORANGE_Scraper_New()
    scraper.startScraping()
    scraper.save_csv()
    display_data = scraper.display_data

    statement_frame = tk.LabelFrame(frame)
    statement_frame.pack()
    statement_frame.configure(bg="black", fg="white", relief="flat", labelanchor="n")
    statement = tk.Label(statement_frame, text="Reports may be obtained by looking up "
                                               "report key on the ORANGE database here. Click",
                         wraplength=1000, justify="left")
    statement.config(bg="black", fg="white", font=('courier', 12, 'bold'))

    url = tk.Label(statement_frame, text='here')
    url.config(bg="black", fg="white", font=('courier', 12, 'bold'))

    def open_url(event=None):
        webbrowser.open_new('https://www.accessdata.fda.gov/scripts/cder/daf/index.cfm?event=reportsSearch.process')

    def blue_text(event=None):
        url.config(fg="blue")

    def white_text(event=None):
        url.config(fg="white")

    url.bind("<Button-1>", open_url)
    url.bind("<Enter>", blue_text)
    url.bind("<Leave>", white_text)

    statement.pack(side="left")
    url.pack(side="left")

    labelframe = tk.LabelFrame(frame, text=" ORANGE ")
    labelframe.configure(bg="white", fg="#e26306", font=('courier', 15, 'bold'),
                         relief="sunken", labelanchor="n")
    # labelframe.grid(row=0, sticky='WE', padx=5, pady=15, ipadx=5, ipady=5)
    labelframe.pack()
    label_list_10(labelframe, 'Approval Date', 'Drug Name', 'Submission', 'Active Ingredients', 'Company',
               'Submission Classification', 'Submission Status', 0,
               "black", ('Times', 10, 'bold'))

    for i, row in enumerate(display_data):
        label_list_10(labelframe, row[0], row[1], row[2], row[3], row[4], row[5], row[6], i + 1)

    print('NEW ORANGE GUI  is made!')
    # frame.update_idletasks()
    return frame

def label_list_10(labelframe, data_1, data_2, data_3, data_4, data_5, data_6, data_7, ind,
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

    labelVariable_1.set(data_1)

    labelVariable_2 = tk.StringVar()
    label_2 = tk.Label(frame, textvariable=labelVariable_2,
                                  width=25, wraplength=175,
                                  anchor="nw", justify="left",
                                  fg=foreground, bg=color[ind % 2],
                                  font=fnt)
    label_2.grid(column=1, row=ind, sticky="W",
                            padx=5, pady=5, ipadx=5, ipady=5)
    labelVariable_2.set(data_2)

    labelVariable_3 = tk.StringVar()
    label_3 = tk.Label(frame, textvariable=labelVariable_3,
                                width=10, wraplength=70,
                                anchor="nw", justify="left",
                                fg=foreground, bg=color[ind % 2],
                                font=fnt)
    label_3.grid(column=2, row=ind, sticky="W",
                          padx=5, pady=5, ipadx=5, ipady=5)
    labelVariable_3.set(data_3)

    labelVariable_4 = tk.StringVar()
    label_4 = tk.Label(frame, textvariable=labelVariable_4,
                                  width=45, wraplength=315,
                                  anchor="nw", justify="left",
                                  fg=foreground, bg=color[ind % 2],
                                  font=fnt)
    label_4.grid(column=3, row=ind, sticky="W",
                            padx=5, pady=5, ipadx=5, ipady=5)
    labelVariable_4.set(data_4)

    labelVariable_5 = tk.StringVar()
    label_5 = tk.Label(frame, textvariable=labelVariable_5,
                                width=25, wraplength=175,
                                anchor="nw", justify="left",
                                fg=foreground, bg=color[ind % 2],
                                font=fnt)
    label_5.grid(column=4, row=ind, sticky="W",
                          padx=5, pady=5, ipadx=5, ipady=5)
    labelVariable_5.set(data_5)

    labelVariable_6 = tk.StringVar()
    label_6 = tk.Label(frame, textvariable=labelVariable_6,
                       width=15, wraplength=105,
                       anchor="nw", justify="left",
                       fg=foreground, bg=color[ind % 2],
                       font=fnt)
    label_6.grid(column=5, row=ind, sticky="W",
                 padx=5, pady=5, ipadx=5, ipady=5)
    labelVariable_6.set(data_6)

    labelVariable_7 = tk.StringVar()
    label_7 = tk.Label(frame, textvariable=labelVariable_7,
                       width=10, wraplength=70,
                       anchor="nw", justify="left",
                       fg=foreground, bg=color[ind % 2],
                       font=fnt)
    label_7.grid(column=6, row=ind, sticky="W",
                 padx=5, pady=5, ipadx=5, ipady=5)
    labelVariable_7.set(data_7)