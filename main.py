class Stack:
    stack = []

    def isEmpty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)


s = Stack()
s.push(125)
print(s.size())
print(s.peek())
print(s.pop())
print(s.size())
print(s.isEmpty())
