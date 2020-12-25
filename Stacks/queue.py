class Queue:
    def __init__(self):
        self._items = []

    def is_empty(self):
        return bool(self._items)

    def add(self, item):
        self._items.insert(0, item)

    def get(self):
        return self._items.pop()

    def size(self):
        return len(self._items)

    def get_from_stack(self, e):
        if e in self._items:
            self._items.remove(e)
            return e
        else:
            raise ValueError(f'Элемент {e} не найден')

    def __repr__(self):
        representation = "<Queue>\n"
        for ind, item in enumerate(reversed(self._items), 1):
            representation += f"{ind}: {str(item)}\n"
        return representation

    def __str__(self):
        return self.__repr__()
