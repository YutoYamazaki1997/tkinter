import tkinter as tk


class View(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.master, text="0")
        self.label.pack(side="top")
        self.increment_button = tk.Button(self.master, text="Increment")
        self.increment_button.pack(side="left")
        self.decrement_button = tk.Button(self.master, text="Decrement")
        self.decrement_button.pack(side="right")
        self.quit_button = tk.Button(
            self.master, text="Quit", command=self.master.quit)
        self.quit_button.pack(side="bottom")
