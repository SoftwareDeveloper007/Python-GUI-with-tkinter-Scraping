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
from scraper.scraper_2 import scraper_2

color = ["#329fea", "#cc93e8"]

def Maude_GUI(frame):

    scraper = scraper_2()
    scraper.search_companies()
    date_received = scraper.date_received
    company_name = scraper.company_name
    brand_name = scraper.brand_name
    generic_name = scraper.generic_name
    report_key = scraper.report_key

    statement_frame = tk.LabelFrame(frame)
    statement_frame.configure(bg="black", fg="white", relief="flat", labelanchor="n")
    statement_frame.pack()

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
    labelframe.configure(bg="#4f617b", fg="#e26306", font=('courier', 15, 'bold'),
                              relief="sunken", labelanchor="n")
    # labelframe.grid(row=0, sticky='WE', padx=5, pady=15, ipadx=5, ipady=5)
    labelframe.pack()
    label_list(labelframe, 'Date Received', 'Company Name', 'Brand Name', 'Generic Name', 'Report Key', 0,
                    "#ffc233", ('Times', 10, 'bold'))
    total_cnt = len(scraper.date_received)
    #print(total_cnt)
    for i in range(total_cnt):
        label_list(labelframe, date_received[i], company_name[i], brand_name[i],
                        generic_name[i], report_key[i], i + 1)

    print('Maude GUI is made!')

def label_list(labelframe, date_received, company_name, brand_name, generic_name, report_key, ind,
               foreground="black", fnt=('Times', 10, 'normal')):
    frame = tk.Frame(labelframe)
    frame.configure(background=color[ind % 2])
    frame.pack(padx=5, pady=5, ipadx=5, ipady=5)

    labelVariable_date_received = tk.StringVar()
    label_date_received = tk.Label(frame, textvariable=labelVariable_date_received,
                                   width=15, wraplength=120,
                                   anchor="nw", justify="left",
                                   fg=foreground, bg=color[ind % 2],
                                   font=fnt)
    label_date_received.grid(column=0, row=ind, columnspan=5, sticky="W",
                             padx=5, pady=5, ipadx=5, ipady=5)

    labelVariable_date_received.set(date_received)

    labelVariable_company_name = tk.StringVar()
    label_company_name = tk.Label(frame, textvariable=labelVariable_company_name,
                                  width=30, wraplength=240,
                                  anchor="nw", justify="left",
                                  fg=foreground, bg=color[ind % 2],
                                  font=fnt)
    label_company_name.grid(column=6, row=ind, columnspan=12, sticky="W",
                            padx=5, pady=5, ipadx=5, ipady=5)
    labelVariable_company_name.set(company_name)

    labelVariable_brand_name = tk.StringVar()
    label_brand_name = tk.Label(frame, textvariable=labelVariable_brand_name,
                                width=40, wraplength=360,
                                anchor="nw", justify="left",
                                fg=foreground, bg=color[ind % 2],
                                font=fnt)
    label_brand_name.grid(column=19, row=ind, columnspan=12, sticky="W",
                          padx=5, pady=5, ipadx=5, ipady=5)
    labelVariable_brand_name.set(brand_name)

    labelVariable_generic_name = tk.StringVar()
    label_generic_name = tk.Label(frame, textvariable=labelVariable_generic_name,
                                  width=40, wraplength=360,
                                  anchor="nw", justify="left",
                                  fg=foreground, bg=color[ind % 2],
                                  font=fnt)
    label_generic_name.grid(column=32, row=ind, columnspan=12, sticky="W",
                            padx=5, pady=5, ipadx=5, ipady=5)
    labelVariable_generic_name.set(generic_name)

    labelVariable_report_key = tk.StringVar()
    label_report_key = tk.Label(frame, textvariable=labelVariable_report_key,
                                width=10, wraplength=80,
                                anchor="nw", justify="left",
                                fg=foreground, bg=color[ind % 2],
                                font=fnt)
    label_report_key.grid(column=45, row=ind, columnspan=5, sticky="W",
                          padx=5, pady=5, ipadx=5, ipady=5)
    labelVariable_report_key.set(report_key)


