__author__ = 'azubko'


class Track:
    def __init__(self, path):
        self._path = path

    @property
    def path(self):
        return self._path
