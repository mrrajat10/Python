class Stack:
    def __init__(self):
        self.stack = []

    # Push: Add element to the top
    def push(self, item):
        self.stack.append(item)

    # Pop: Remove and return the top element
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return "Stack Underflow"

    # Peek: Return top element without removing
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return "Stack is empty"

    # Check if stack is empty
    def is_empty(self):
        return len(self.stack) == 0

    # Return the size of the stack
    def size(self):
        return len(self.stack)

    # Display stack from top to bottom
    def display(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            print("Stack (top → bottom):", self.stack[::-1])
