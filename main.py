from __future__ import absolute_import, division, print_function, unicode_literals

try:
    import tkinter as tk
except:
    import Tkinter as tk

import ttk
from tkinter import *
import time
from GUI_components.fda import *
from GUI_components.press import *
from GUI_components.drug import *
from GUI_components.maude import *

class main_GUI(tk.Tk):
    def __init__(self, parent):
        tk.Tk.__init__(self, parent)
        self.parent = parent
        self.resizable(0,0)

        #self.grid()
        self.geometry("1200x800")
        self.nb = ttk.Notebook(self)
        self.nb.pack(expand=True, fill=BOTH)

        fda = Frame(self.nb,relief=tk.SOLID, background="black")
        fda.pack(fill=BOTH, expand=True)
        press = Frame(self.nb,relief=tk.SOLID, background="black")
        press.pack(fill=BOTH, expand=True)
        drug = Frame(self.nb,relief=tk.SOLID, background="black")
        drug.pack(fill=BOTH, expand=True)
        maude = Frame(self.nb,relief=tk.SOLID, background="black")
        maude.pack(fill=BOTH, expand=True)

        self.nb.add(fda, text='FDA MedWatch')
        self.nb.add(press, text='Press Announcement')
        self.nb.add(drug, text='Drug Recalls')
        self.nb.add(maude, text='MAUDE')

        #scrollbar_add(fda)
        #scrollbar_add(press)
        #scrollbar_add(drug)
        #scrollbar_add(maude)

        FDA_MedWatch_GUI(fda)
        Press_GUI(press)
        Drug_GUI(drug)
        Maude_GUI(maude)


def scrollbar_add(frame):
    canvas = Canvas(frame, width=1200, height=800)
    scrollbar = Scrollbar(frame, orient="vertical", command=canvas.yview)
    canvas.config(yscrollcommand=scrollbar.set, background="black", scrollregion=(0,0,100,1000))
    canvas.pack(side=LEFT, fill=BOTH, expand=True)
    #canvas.create_window((0, 0), window=frame, anchor="nw", tags="frame")
    scrollbar.pack(side=RIGHT, fill=Y)


if __name__ == '__main__':
    app = main_GUI(None)
    app.title("What's New")
    app.mainloop()
