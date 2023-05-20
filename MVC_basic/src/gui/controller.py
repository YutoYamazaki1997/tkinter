class Controller():
    def __init__(self, master, model, view):
        self.master = master
        self.model = model
        self.view = view

        self.master.bind("<space>", self.moveController)

    def moveController(self, event):
        self.model.moveModel(self.view.canvas, "id1")
