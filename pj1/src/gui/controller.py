class Controller:
    def __init__(self, model, view):
        self._model = model
        self._view = view
        self._view.increment_button.config(command=self.increment)
        self._view.decrement_button.config(command=self.decrement)
        self._view.label.config(text=str(self._model.data))

    def increment(self):
        self._model.increment()
        self._view.label.config(text=str(self._model.data))

    def decrement(self):
        self._model.decrement()
        self._view.label.config(text=str(self._model.data))
