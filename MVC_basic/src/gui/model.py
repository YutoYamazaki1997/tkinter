class Model():
    def __init__(self):
        self.width = 300
        self.height = 300

    def moveModel(self, canvas, id):
        canvas.move(id, 5, 5)
