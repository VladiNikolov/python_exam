class Stack:

    def __init__(self):
        self.data = []

    def push(self, element):
        self.data.append(element)

    def pop(self):
        result = self.data.pop()
        return result

    def top(self):
        last_el =self.data[-1]
        return last_el

    def is_empty(self):
        if len(self.data) == 0:
            return True
        return False

    def __str__(self):
        return f'[{", ".join(reversed(self.data))}]'

