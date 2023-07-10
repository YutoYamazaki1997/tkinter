import tkinter as tk


class UnderlineEntry(tk.Entry):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.config(borderwidth=0, relief="flat", insertwidth=1)
        self.underline_color = "white"  # 下線の色を指定

    def paint_underline(self):
        x, y, width, height = self.bbox("insert")
        self.create_line(x, y + height - 1, x + width, y + height - 1, fill=self.underline_color)

    def on_configure(self, event=None):
        self.delete("underline")
        self.paint_underline()

    def on_key_press(self, event=None):
        self.after(1, self.on_configure)


class View:
    def __init__(self, app, model):
        self.master = app
        self.model = model
        self.frame_main = tk.Frame(self.master, width=300, height=200, bg="black")
        self.frame_main.grid(column=0, row=0)
        self.frame_main.rowconfigure(0, minsize=400)
        entry = UnderlineEntry(self.frame_main, width=200)
        entry.rowconfigure(0, minsize=400)
        entry.pack()
