#!/usr/bin/python3
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
        return self.items[len(self.items)-1]
    
    def size(self):
        return len(self.items)
    
def revStr(str):
    s = Stack()
    reversed = ""
    for x in str:
        s.push(x)
    while not s.isEmpty():
        reversed += s.pop()
    return reversed

print(revStr("Hello"))