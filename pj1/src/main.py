import tkinter as tk
from gui.controller import Controller
from gui.model import Model
from gui.view import View


def main():
    root = tk.Tk()
    app = View(master=root)
    model = Model()
    Controller(model, app)
    app.mainloop()


if __name__ == "__main__":
    main()
