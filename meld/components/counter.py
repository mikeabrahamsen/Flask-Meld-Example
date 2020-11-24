from flask_meld.component import Component


class Counter(Component):
    _count = 0

    @property
    def count(self):
        return self._count

    @count.setter
    def count(self, value):
        if value is not None:
            self._count = int(value)

    def add(self):
        self.count = self.count + 1

    def subtract(self):
        self.count = self.count - 1
