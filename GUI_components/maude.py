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
from scraper.maude_scraper import MAUDE_Scraper

color = ["#efefe9", "#e4e4dd"]


def Maude_GUI(canvas):
    frame = tk.Frame(canvas)
    frame.pack()
    scraper = MAUDE_Scraper()
    scraper.search_companies()
    date_received = scraper.date_received
    company_name = scraper.company_name
    brand_name = scraper.brand_name
    generic_name = scraper.generic_name
    report_key = scraper.report_key

    statement_frame = tk.LabelFrame(frame)
    statement_frame.pack()
    statement_frame.configure(bg="black", fg="white", relief="flat", labelanchor="n")
    statement = tk.Label(statement_frame, text="Reports may be obtained by looking up "
                                               "report key on the MAUDE database here. Click",
                         wraplength=1000, justify="left")
    statement.config(bg="black", fg="white", font=('courier', 12, 'bold'))

    url = tk.Label(statement_frame, text='here')
    url.config(bg="black", fg="white", font=('courier', 12, 'bold'))

    def open_url(event=None):
        webbrowser.open_new('https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfmaude/search.cfm')

    def blue_text(event=None):
        url.config(fg="blue")

    def white_text(event=None):
        url.config(fg="white")

    url.bind("<Button-1>", open_url)
    url.bind("<Enter>", blue_text)
    url.bind("<Leave>", white_text)

    statement.pack(side="left")
    url.pack(side="left")

    labelframe = tk.LabelFrame(frame, text=" MAUDE ")
    labelframe.configure(bg="white", fg="#e26306", font=('courier', 15, 'bold'),
                         relief="sunken", labelanchor="n")
    # labelframe.grid(row=0, sticky='WE', padx=5, pady=15, ipadx=5, ipady=5)
    labelframe.pack()
    label_list_4(labelframe, 'Date Received', 'Company Name', 'Brand Name', 'Generic Name', 'Report Key', 0,
               "black", ('Times', 10, 'bold'))
    total_cnt = len(scraper.date_received)
    for i in range(total_cnt):
        label_list_4(labelframe, date_received[i], company_name[i], brand_name[i],
                   generic_name[i], report_key[i], i + 1)

    print('Maude GUI is made!')
    # frame.update_idletasks()
    return frame

def label_list_4(labelframe, data1, data2, data3, data4, data5, ind,
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

    labelVariable_2 = tk.StringVar()
    label_2 = tk.Label(frame, textvariable=labelVariable_2,
                                  width=35, wraplength=245,
                                  anchor="nw", justify="left",
                                  fg=foreground, bg=color[ind % 2],
                                  font=fnt)
    label_2.grid(column=1, row=ind, sticky="W",
                            padx=5, pady=5, ipadx=5, ipady=5)
    labelVariable_2.set(data2)

    labelVariable_3 = tk.StringVar()
    label_3 = tk.Label(frame, textvariable=labelVariable_3,
                                width=40, wraplength=280,
                                anchor="nw", justify="left",
                                fg=foreground, bg=color[ind % 2],
                                font=fnt)
    label_3.grid(column=2, row=ind, sticky="W",
                          padx=5, pady=5, ipadx=5, ipady=5)
    labelVariable_3.set(data3)

    labelVariable_4 = tk.StringVar()
    label_4 = tk.Label(frame, textvariable=labelVariable_4,
                                  width=45, wraplength=315,
                                  anchor="nw", justify="left",
                                  fg=foreground, bg=color[ind % 2],
                                  font=fnt)
    label_4.grid(column=3, row=ind, sticky="W",
                            padx=5, pady=5, ipadx=5, ipady=5)
    labelVariable_4.set(data4)

    labelVariable_5 = tk.StringVar()
    label_5 = tk.Label(frame, textvariable=labelVariable_5,
                                width=10, wraplength=70,
                                anchor="nw", justify="left",
                                fg=foreground, bg=color[ind % 2],
                                font=fnt)
    label_5.grid(column=4, row=ind, sticky="W",
                          padx=5, pady=5, ipadx=5, ipady=5)
    labelVariable_5.set(data5)