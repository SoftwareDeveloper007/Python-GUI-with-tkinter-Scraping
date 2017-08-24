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
        self.nb.bind('<1>', self.on_focus_tab)

        fda = Canvas(self.nb,relief=tk.SOLID, background="black")
        fda.pack(fill=BOTH, expand=True)
        press = Canvas(self.nb,relief=tk.SOLID, background="black")
        press.pack(fill=BOTH, expand=True)
        drug = Canvas(self.nb,relief=tk.SOLID, background="black")
        drug.pack(fill=BOTH, expand=True)
        maude = Canvas(self.nb,relief=tk.SOLID, background="black")
        maude.pack(fill=BOTH, expand=True)

        self.nb.add(fda, text='FDA MedWatch')
        self.nb.add(press, text='Press Announcement')
        self.nb.add(drug, text='Drug Recalls')
        self.nb.add(maude, text='MAUDE')

        self.fda_canvas = scrollbar_add(fda)
        self.press_canvas = scrollbar_add(press)
        self.drug_canvas = scrollbar_add(drug)
        self.maude_canvas = scrollbar_add(maude)

        self.fda_frame = FDA_MedWatch_GUI(self.fda_canvas)
        self.press_frame = Press_GUI(self.press_canvas)
        self.drug_frame = Drug_GUI(self.drug_canvas)
        self.maude_frame = Maude_GUI(self.maude_canvas)

        self.fda_canvas.create_window(0, 0, anchor=CENTER, window=self.fda_frame)
        self.fda_canvas.config(scrollregion=self.fda_canvas.bbox("all"))

        self.press_canvas.create_window(0, 0, anchor=NW, window=self.press_frame)
        self.press_canvas.config(scrollregion=self.press_canvas.bbox("all"))

        self.drug_canvas.create_window(0, 0, anchor=NW, window=self.drug_frame)
        self.drug_canvas.config(scrollregion=self.drug_canvas.bbox("all"))

        self.maude_canvas.create_window(0, 0, anchor=NW, window=self.maude_frame)
        self.maude_canvas.config(scrollregion=self.maude_canvas.bbox("all"))

    def on_focus_tab(self, event):
        index = event.widget.index('@%d,%d' % (event.x, event.y))
        print(index)
        if index is 0:
            self.fda_frame.bind("<Configure>", lambda x: self.fda_canvas.configure(scrollregion=self.fda_canvas.bbox("all")))
            self.bind("<Down>", lambda x: self.fda_canvas.yview_scroll(3, 'units'))  # bind "Down" to scroll down
            self.bind("<Up>", lambda x: self.fda_canvas.yview_scroll(-3, 'units'))  # bind "Up" to scroll up
            # bind the mousewheel to scroll up/down
            self.bind("<MouseWheel>", lambda x: self.fda_canvas.yview_scroll(int(-1 * (x.delta / 40)), "units"))
        elif index is 1:
            self.press_frame.bind("<Configure>", lambda x: self.press_canvas.configure(scrollregion=self.press_canvas.bbox("all")))
            self.bind("<Down>", lambda x: self.press_canvas.yview_scroll(3, 'units'))  # bind "Down" to scroll down
            self.bind("<Up>", lambda x: self.press_canvas.yview_scroll(-3, 'units'))  # bind "Up" to scroll up
            # bind the mousewheel to scroll up/down
            self.bind("<MouseWheel>", lambda x: self.press_canvas.yview_scroll(int(-1 * (x.delta / 40)), "units"))
        elif index is 2:
            self.drug_frame.bind("<Configure>", lambda x: self.drug_canvas.configure(scrollregion=self.drug_canvas.bbox("all")))
            self.bind("<Down>", lambda x: self.drug_canvas.yview_scroll(3, 'units'))  # bind "Down" to scroll down
            self.bind("<Up>", lambda x: self.drug_canvas.yview_scroll(-3, 'units'))  # bind "Up" to scroll up
            # bind the mousewheel to scroll up/down
            self.bind("<MouseWheel>", lambda x: self.drug_canvas.yview_scroll(int(-1 * (x.delta / 40)), "units"))
        else:
            self.maude_frame.bind("<Configure>", lambda x: self.maude_canvas.configure(scrollregion=self.maude_canvas.bbox("all")))
            self.bind("<Down>", lambda x: self.maude_canvas.yview_scroll(3, 'units'))  # bind "Down" to scroll down
            self.bind("<Up>", lambda x: self.maude_canvas.yview_scroll(-3, 'units'))  # bind "Up" to scroll up
            # bind the mousewheel to scroll up/down
            self.bind("<MouseWheel>", lambda x: self.maude_canvas.yview_scroll(int(-1 * (x.delta / 40)), "units"))


def scrollbar_add(frame):
    scrollbar = Scrollbar(frame, orient="vertical")
    scrollbar.pack(side=RIGHT, fill=Y)

    canvas = Canvas(frame, width=1200, height=800)
    canvas.pack(side=LEFT, fill=Y, expand=True)
    canvas.config(yscrollcommand=scrollbar.set, background="black", scrollregion=(0, 0, 100, 1000))
    # canvas.config(yscrollcommand=scrollbar.set, scrollregion=(0, 0, 100, 1000))
    scrollbar.config(command=canvas.yview)
    return canvas


if __name__ == '__main__':
    app = main_GUI(None)
    app.title("What's New")
    app.mainloop()