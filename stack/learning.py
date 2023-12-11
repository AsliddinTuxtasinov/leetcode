class Stack:
    def __init__(self) -> None:
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, value):
        self.stack.append(value)
        return

    def pop(self):
        if self.is_empty():
            return None
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.stack[-1]


if __name__ == '__main__':
    stack = Stack()
    print(f"stack.is_empty() -> {stack.is_empty()}")

    stack.push(1)
    stack.push(2)
    print(f"stack.is_empty() -> {stack.is_empty()}")
    print(f"stack.peek() -> {stack.peek()}")
    print(f"type(stack) -> {type(stack)}")
