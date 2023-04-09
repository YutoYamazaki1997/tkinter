class Model:
    def __init__(self):
        self._data = 0

    def increment(self):
        self._data += 1

    def decrement(self):
        self._data -= 1

    @property
    def data(self):
        return self._data
