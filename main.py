from __future__ import absolute_import, division, print_function, unicode_literals

try:
    import tkinter as tk
except:
    import Tkinter as tk

import ttk
from tkinter import *
import time
'''
from GUI_components.fda import *
from GUI_components.press import *
from GUI_components.drug import *
from GUI_components.maude import *
from GUI_components.cms import *
from GUI_components.hhs import *
from GUI_components.genome import *
from GUI_components.axios import *
'''

from GUI_components.fda import *
from GUI_components.orange import *
from GUI_components.orange_new import *

class main_GUI(tk.Tk):
    def __init__(self, parent):
        tk.Tk.__init__(self, parent)
        self.parent = parent
        self.resizable(0, 0)

        # self.grid()
        self.geometry("1200x800")
        self.nb = ttk.Notebook(self)
        self.nb.pack(expand=True, fill=BOTH)
        self.nb.bind('<1>', self.on_focus_tab)

        '''
        fda = Canvas(self.nb, relief=tk.SOLID, background="black")
        fda.pack(fill=BOTH, expand=True)
        self.nb.add(fda, text='FDA MedWatch')
        self.fda_canvas = scrollbar_add(fda)
        self.fda_frame = FDA_MedWatch_GUI(self.fda_canvas)
        self.fda_canvas.create_window(0, 0, anchor=CENTER, window=self.fda_frame)
        self.fda_canvas.config(scrollregion=self.fda_canvas.bbox("all"))

        press = Canvas(self.nb, relief=tk.SOLID, background="black")
        press.pack(fill=BOTH, expand=True)
        self.nb.add(press, text='Press Announcement')
        self.press_canvas = scrollbar_add(press)
        self.press_frame = Press_GUI(self.press_canvas)
        self.press_canvas.create_window(0, 0, anchor=NW, window=self.press_frame)
        self.press_canvas.config(scrollregion=self.press_canvas.bbox("all"))

        drug = Canvas(self.nb, relief=tk.SOLID, background="black")
        drug.pack(fill=BOTH, expand=True)
        self.nb.add(drug, text='Drug Recalls')
        self.drug_canvas = scrollbar_add(drug)
        self.drug_frame = Drug_GUI(self.drug_canvas)
        self.drug_canvas.create_window(0, 0, anchor=NW, window=self.drug_frame)
        self.drug_canvas.config(scrollregion=self.drug_canvas.bbox("all"))

        maude = Canvas(self.nb, relief=tk.SOLID, background="black")
        maude.pack(fill=BOTH, expand=True)
        self.nb.add(maude, text='maude Recalls')
        self.maude_canvas = scrollbar_add(maude)
        self.maude_frame = Maude_GUI(self.maude_canvas)
        self.maude_canvas.create_window(0, 0, anchor=NW, window=self.maude_frame)
        self.maude_canvas.config(scrollregion=self.maude_canvas.bbox("all"))

        cms = Canvas(self.nb, relief=tk.SOLID, background="black")
        cms.pack(fill=BOTH, expand=True)
        self.nb.add(cms, text='CMS')
        self.cms_canvas = scrollbar_add(cms)
        self.cms_frame = CMS_GUI(self.cms_canvas)
        self.cms_canvas.create_window(0, 0, anchor=NW, window=self.cms_frame)
        self.cms_canvas.config(scrollregion=self.cms_canvas.bbox("all"))

        hhs = Canvas(self.nb, relief=tk.SOLID, background="black")
        hhs.pack(fill=BOTH, expand=True)
        self.nb.add(hhs, text='HHS')
        self.hhs_canvas = scrollbar_add(hhs)
        self.hhs_frame = HHS_GUI(self.hhs_canvas)
        self.hhs_canvas.create_window(0, 0, anchor=NW, window=self.hhs_frame)
        self.hhs_canvas.config(scrollregion=self.hhs_canvas.bbox("all"))

        genome = Canvas(self.nb, relief=tk.SOLID, background="black")
        genome.pack(fill=BOTH, expand=True)
        self.nb.add(genome, text='GENOME')
        self.genome_canvas = scrollbar_add(genome)
        self.genome_frame = GENOME_GUI(self.genome_canvas)
        self.genome_canvas.create_window(0, 0, anchor=NW, window=self.genome_frame)
        self.genome_canvas.config(scrollregion=self.genome_canvas.bbox("all"))

        axios = Canvas(self.nb, relief=tk.SOLID, background="black")
        axios.pack(fill=BOTH, expand=True)
        self.nb.add(axios, text='AXIOS')
        self.axios_canvas = scrollbar_add(axios)
        self.axios_frame = AXIOS_GUI(self.axios_canvas)
        self.axios_canvas.create_window(0, 0, anchor=NW, window=self.axios_frame)
        self.axios_canvas.config(scrollregion=self.axios_canvas.bbox("all"))
        
        '''

        fda = Canvas(self.nb, relief=tk.SOLID, background="black")
        fda.pack(fill=BOTH, expand=True)
        self.nb.add(fda, text='FDA MedWatch')
        self.fda_canvas = scrollbar_add(fda)
        self.fda_frame = FDA_MedWatch_GUI(self.fda_canvas)
        self.fda_canvas.create_window(0, 0, anchor=CENTER, window=self.fda_frame)
        self.fda_canvas.config(scrollregion=self.fda_canvas.bbox("all"))

        orange = Canvas(self.nb, relief=tk.SOLID, background="black")
        orange.pack(fill=BOTH, expand=True)
        self.nb.add(orange, text='ORANGE')
        self.orange_canvas = scrollbar_add(orange)
        self.orange_frame = ORANGE_GUI(self.orange_canvas)
        self.orange_canvas.create_window(0, 0, anchor=NW, window=self.orange_frame)
        self.orange_canvas.config(scrollregion=self.orange_canvas.bbox("all"))

        orange_new = Canvas(self.nb, relief=tk.SOLID, background="black")
        orange_new.pack(fill=BOTH, expand=True)
        self.nb.add(orange_new, text='ORANGE NEW')
        self.orange_new_canvas = scrollbar_add(orange_new)
        self.orange_new_frame = ORANGE_GUI_New(self.orange_new_canvas)
        self.orange_new_canvas.create_window(0, 0, anchor=NW, window=self.orange_new_frame)
        self.orange_new_canvas.config(scrollregion=self.orange_new_canvas.bbox("all"))

    def on_focus_tab(self, event):
        index = event.widget.index('@%d,%d' % (event.x, event.y))
        print(index)

        '''
        if index is 0:
            self.fda_frame.bind("<Configure>",
                                lambda x: self.fda_canvas.configure(scrollregion=self.fda_canvas.bbox("all")))
            self.bind("<Down>", lambda x: self.fda_canvas.yview_scroll(3, 'units'))  # bind "Down" to scroll down
            self.bind("<Up>", lambda x: self.fda_canvas.yview_scroll(-3, 'units'))  # bind "Up" to scroll up
            # bind the mousewheel to scroll up/down
            self.bind("<MouseWheel>", lambda x: self.fda_canvas.yview_scroll(int(-1 * (x.delta / 40)), "units"))

        elif index is 1:
            self.press_frame.bind("<Configure>",
                                  lambda x: self.press_canvas.configure(scrollregion=self.press_canvas.bbox("all")))
            self.bind("<Down>", lambda x: self.press_canvas.yview_scroll(3, 'units'))  # bind "Down" to scroll down
            self.bind("<Up>", lambda x: self.press_canvas.yview_scroll(-3, 'units'))  # bind "Up" to scroll up
            # bind the mousewheel to scroll up/down
            self.bind("<MouseWheel>", lambda x: self.press_canvas.yview_scroll(int(-1 * (x.delta / 40)), "units"))

        elif index is 2:
            self.drug_frame.bind("<Configure>",
                                 lambda x: self.drug_canvas.configure(scrollregion=self.drug_canvas.bbox("all")))
            self.bind("<Down>", lambda x: self.drug_canvas.yview_scroll(3, 'units'))  # bind "Down" to scroll down
            self.bind("<Up>", lambda x: self.drug_canvas.yview_scroll(-3, 'units'))  # bind "Up" to scroll up
            # bind the mousewheel to scroll up/down
            self.bind("<MouseWheel>", lambda x: self.drug_canvas.yview_scroll(int(-1 * (x.delta / 40)), "units"))

        elif index is 3:
            self.maude_frame.bind("<Configure>",
                                  lambda x: self.maude_canvas.configure(scrollregion=self.maude_canvas.bbox("all")))
            self.bind("<Down>", lambda x: self.maude_canvas.yview_scroll(3, 'units'))  # bind "Down" to scroll down
            self.bind("<Up>", lambda x: self.maude_canvas.yview_scroll(-3, 'units'))  # bind "Up" to scroll up
            # bind the mousewheel to scroll up/down
            self.bind("<MouseWheel>", lambda x: self.maude_canvas.yview_scroll(int(-1 * (x.delta / 40)), "units"))

        elif index is 4:
            self.cms_frame.bind("<Configure>",
                                lambda x: self.cms_canvas.configure(scrollregion=self.cms_canvas.bbox("all")))
            self.bind("<Down>", lambda x: self.cms_canvas.yview_scroll(3, 'units'))  # bind "Down" to scroll down
            self.bind("<Up>", lambda x: self.cms_canvas.yview_scroll(-3, 'units'))  # bind "Up" to scroll up
            # bind the mousewheel to scroll up/down
            self.bind("<MouseWheel>", lambda x: self.cms_canvas.yview_scroll(int(-1 * (x.delta / 40)), "units"))

        elif index is 5:
            self.hhs_frame.bind("<Configure>",
                                lambda x: self.hhs_canvas.configure(scrollregion=self.hhs_canvas.bbox("all")))
            self.bind("<Down>", lambda x: self.hhs_canvas.yview_scroll(3, 'units'))  # bind "Down" to scroll down
            self.bind("<Up>", lambda x: self.hhs_canvas.yview_scroll(-3, 'units'))  # bind "Up" to scroll up
            # bind the mousewheel to scroll up/down
            self.bind("<MouseWheel>", lambda x: self.hhs_canvas.yview_scroll(int(-1 * (x.delta / 40)), "units"))

        elif index is 6:
            self.genome_frame.bind("<Configure>",
                                   lambda x: self.genome_canvas.configure(scrollregion=self.genome_canvas.bbox("all")))
            self.bind("<Down>", lambda x: self.genome_canvas.yview_scroll(3, 'units'))  # bind "Down" to scroll down
            self.bind("<Up>", lambda x: self.genome_canvas.yview_scroll(-3, 'units'))  # bind "Up" to scroll up
            # bind the mousewheel to scroll up/down
            self.bind("<MouseWheel>", lambda x: self.genome_canvas.yview_scroll(int(-1 * (x.delta / 40)), "units"))

        elif index is 7:
            self.axios_frame.bind("<Configure>",
                                  lambda x: self.axios_canvas.configure(scrollregion=self.axios_canvas.bbox("all")))
            self.bind("<Down>", lambda x: self.axios_canvas.yview_scroll(3, 'units'))  # bind "Down" to scroll down
            self.bind("<Up>", lambda x: self.axios_canvas.yview_scroll(-3, 'units'))  # bind "Up" to scroll up
            # bind the mousewheel to scroll up/down
            self.bind("<MouseWheel>", lambda x: self.axios_canvas.yview_scroll(int(-1 * (x.delta / 40)), "units"))

        elif index is 8:
            self.orange_frame.bind("<Configure>",
                                   lambda x: self.orange_canvas.configure(scrollregion=self.orange_canvas.bbox("all")))
            self.bind("<Down>", lambda x: self.orange_canvas.yview_scroll(3, 'units'))  # bind "Down" to scroll down
            self.bind("<Up>", lambda x: self.orange_canvas.yview_scroll(-3, 'units'))  # bind "Up" to scroll up
            # bind the mousewheel to scroll up/down
            self.bind("<MouseWheel>", lambda x: self.orange_canvas.yview_scroll(int(-1 * (x.delta / 40)), "units"))
        '''
        if index is 0:
            self.fda_frame.bind("<Configure>",
                                lambda x: self.fda_canvas.configure(scrollregion=self.fda_canvas.bbox("all")))
            self.bind("<Down>", lambda x: self.fda_canvas.yview_scroll(3, 'units'))  # bind "Down" to scroll down
            self.bind("<Up>", lambda x: self.fda_canvas.yview_scroll(-3, 'units'))  # bind "Up" to scroll up
            # bind the mousewheel to scroll up/down
            self.bind("<MouseWheel>", lambda x: self.fda_canvas.yview_scroll(int(-1 * (x.delta / 40)), "units"))
        elif index is 1:
            self.orange_frame.bind("<Configure>",
                                   lambda x: self.orange_canvas.configure(scrollregion=self.orange_canvas.bbox("all")))
            self.bind("<Down>", lambda x: self.orange_canvas.yview_scroll(3, 'units'))  # bind "Down" to scroll down
            self.bind("<Up>", lambda x: self.orange_canvas.yview_scroll(-3, 'units'))  # bind "Up" to scroll up
            # bind the mousewheel to scroll up/down
            self.bind("<MouseWheel>", lambda x: self.orange_canvas.yview_scroll(int(-1 * (x.delta / 40)), "units"))

        else:
            self.orange_new_frame.bind("<Configure>",
                                       lambda x: self.orange_new_canvas.configure(
                                           scrollregion=self.orange_new_canvas.bbox("all")))
            self.bind("<Down>", lambda x: self.orange_new_canvas.yview_scroll(3, 'units'))  # bind "Down" to scroll down
            self.bind("<Up>", lambda x: self.orange_new_canvas.yview_scroll(-3, 'units'))  # bind "Up" to scroll up
            # bind the mousewheel to scroll up/down
            self.bind("<MouseWheel>", lambda x: self.orange_new_canvas.yview_scroll(int(-1 * (x.delta / 40)), "units"))


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
