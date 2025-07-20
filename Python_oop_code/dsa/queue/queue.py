class Queue:
    def __init__(self):
        self.q = []

    def enqueue(self, item):
        self.q.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.q.pop(0)
        return "Queue Underflow"

    def peek(self):
        if not self.is_empty():
            return self.q[0]
        return "Queue is empty"

    def is_empty(self):
        return len(self.q) == 0

    def size(self):
        return len(self.q)

    def display(self):
        print("Queue (front → rear):", self.q)
