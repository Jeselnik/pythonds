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

def parChecker(str):
    balanced = True
    index = 0
    s = Stack()
    while index < len(str) and balanced:
        char = str[index]
        if char == '(': 
            s.push('(') 
        else:
            if s.isEmpty():
                balanced = False
            else:
                s.pop()
        index += 1
    if balanced and s.isEmpty():
        balanced = True
    else:
        balanced = False
    return balanced

def baseConverter(int, base):
    numeralSet = "0123456789ABCDEF"
    if int > 0:
        s = Stack()
        while int != 0:
            s.push(numeralSet[int%base])
            int = int // base

        binary = ""
        while not s.isEmpty():
            binary += str(s.pop())
        return binary
    else:
        raise ValueError("Number must be positive")

print(revStr("Hello"))
print(parChecker("(()"))
print(baseConverter(26, 26))