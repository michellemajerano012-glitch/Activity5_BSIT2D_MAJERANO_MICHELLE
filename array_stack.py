class ArrayStack:
    """Stack implemented using an array."""

    def __init__(self, capacity=5):
        self.capacity = capacity
        self.items = [None] * capacity
        self.top = -1

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == self.capacity - 1

    def push(self, item):
        if self.is_full():
            raise OverflowError("Stack overflow: stack is full.")

        self.top += 1
        self.items[self.top] = item

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack underflow: stack is empty.")

        item = self.items[self.top]
        self.items[self.top] = None
        self.top -= 1
        return item

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty.")

        return self.items[self.top]

    def __str__(self):
        return str(self.items[:self.top + 1])
