class ArrayQueue:
    """Circular queue using a fixed-size array."""

    def __init__(self, capacity=5):
        if capacity <= 0:
            raise ValueError("Capacity must be positive.")

        self.capacity = capacity
        self.items = [None] * capacity
        self.front = 0
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.capacity

    def enqueue(self, item):
        if self.is_full():
            raise OverflowError("Queue overflow: queue is full.")

        rear = (self.front + self.size) % self.capacity
        self.items[rear] = item
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue underflow: queue is empty.")

        item = self.items[self.front]
        self.items[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.size -= 1

        if self.is_empty():
            self.front = 0

        return item

    def peek_front(self):
        if self.is_empty():
            raise IndexError("Queue is empty. Nothing to peek.")

        return self.items[self.front]

    def __str__(self):
        values = [
            self.items[(self.front + i) % self.capacity]
            for i in range(self.size)
        ]
        return f"Queue: {values}"
