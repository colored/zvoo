__author__ = 'azubko'


class Track:
    def __init__(self, path):
        self._path = path
        self.__plays = 5
        self.available = True

    def __str__(self):
        return self._path

    @property
    def path(self):
        return self._path

    @property
    def plays(self):
        return "HUI"  # self.__plays

    @plays.setter
    def plays(self, value):
        if self.__plays < 1:
            self.__plays += 1
        else:
            self.available = False

    __repr__ = __str__
