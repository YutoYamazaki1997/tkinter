import tkinter as tk
from gui.controller import Controller
from gui.model import Model
from gui.view import View


def main():
    app = tk.Tk()
    model = Model()
    view = View(app, model)
    Controller(app, model, view)
    app.mainloop()


if __name__ == "__main__":
    main()
