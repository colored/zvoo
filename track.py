__author__ = 'azubko'


class Track:
    def __init__(self, path):
        self._path = path
        self._plays = 0

    def __str__(self):
        return self._path

    @property
    def path(self):
        return self._path

    @property
    def plays(self):
        return self._plays

    @plays.setter
    def plays(self, value):
        self._plays += 1

    __repr__ = __str__
