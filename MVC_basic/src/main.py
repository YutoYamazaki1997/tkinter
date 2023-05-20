
import tkinter as tk
from gui.controller import Controller
from gui.model import Model
from gui.view import View


class Application(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()

        self.model = Model()
        master.geometry(str(self.model.width)+"x"+str(self.model.height))
        master.title("雛形")
        self.view = View(master, self.model)
        self.controller = Controller(master, self.model, self.view)


def main():
    win = tk.Tk()
    app = Application(master=win)
    app.mainloop()


if __name__ == "__main__":
    main()
