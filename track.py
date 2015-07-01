__author__ = 'azubko'


class Track(object):
    def __init__(self, path):
        self._path = path
        self._plays = 0
        self.available = True

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
        if self._plays < 1:
            self._plays = value
        else:
            self.available = False

    __repr__ = __str__
