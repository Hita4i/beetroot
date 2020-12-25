class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

    def get_from_stack(self, e):
        if e in self.items:
            self.items.remove(e)
            return e
        else:
            raise ValueError(f'Элемент {e} не найден')

    def show_stack(self):
        stack_items = [item for item in self.items[::-1]]
        return stack_items

    def __str__(self):
        return f'{self.items}'
