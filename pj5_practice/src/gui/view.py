import tkinter as tk


class View:
    HEIGHT = 600
    WIDTH = 800

    def __init__(self, app, model):
        self.master = app
        self.model = model

        self.monitor_height = app.winfo_screenheight()
        print(self.monitor_height)
        self.master.geometry(f"{View.WIDTH}x{View.HEIGHT}")
        App_text = tk.Label(self.master, text="HELLO APP")
        App_text.grid(column=0, row=0)
        Frame_left = tk.Frame(self.master, height=200, width=400)
        Frame_left.grid(column=0, row=1)
        Frame_right = tk.Frame(self.master)
        Frame_right.grid(column=1, row=1)

        canvas1 = tk.Canvas(Frame_right, width=200, height=200, bg="green")
        canvas1.grid(column=0, row=0)

        button1 = tk.Button(Frame_left, text="test", height=20, width=30)
        button1.grid(column=0, row=0)
