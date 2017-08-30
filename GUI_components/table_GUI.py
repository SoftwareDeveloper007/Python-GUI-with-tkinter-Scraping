try:
    import tkinter as tk
    from tkinter import messagebox
except:
    import Tkinter as tk
    import tkMessageBox as messagebox

import ttk

color = ["#329fea", "#cc93e8"]

class table_GUI():
    def __init__(self, *header, title, *width, *data):
        self.header = header
        self.title = title
        self.width = width
        self.data = data

        self.mainFrame = tk.Frame()
        self.table_frame = tk.LabelFrame(self.mainFrame, text=title)
        self.table_frame.pack()

        self.header_frame = tk.Frame(self.table_frame)
        self.header_frame.pack()
        self.body_frame = tk.Frame(self.table_frame)
        self.body_frame.pack()



    def make_header(self):
        for i in range(len(self.header)):





