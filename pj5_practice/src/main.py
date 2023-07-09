import tkinter as tk
from gui.controller import Controller
from gui.model import Model
from gui.view import View
import ctypes


def main():
    ctypes.windll.shcore.SetProcessDpiAwareness(True)

    app = tk.Tk()
    model = Model()
    view = View(app, model)
    Controller(app, model, view)
    app.mainloop()


if __name__ == "__main__":
    main()
