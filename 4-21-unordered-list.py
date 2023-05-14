#!/usr/bin/python3
class Node:
    def __init__(self,initdata) -> None:
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data
    
    def getNext(self):
        return self.next
    
    def setData(self, newData):
        self.data = newData

    def setNext(self, nextNode):
        self.next = nextNode

class UnorderedList:
    def __init__(self) -> None:
        self.head = None

    def getHead(self):
        return self.head
    
    def isEmpty(self):
        empty = True
        if self.head != None:
            empty = False
        return empty

    def add(self, item):
        n = Node(item)
        n.setNext(self.head)
        self.head = n

    def size(self) -> int:
        count = 0
        current = self.head
        while current != None:
            count += 1
            current = current.getNext()
        return count
    
    def search(self, term) -> bool:
        present = False
        current = self.head
        while current != None:
            if term == current.getData():
                present = True
                break
            else:
                current = current.getNext()
        return present
    
    def remove(self, term):
        found = False
        current = self.head
        prev = None
        while not found and current != None:
            if term == current.getData():
                found = True
            else:
                prev = current
                current = current.getNext()
        if not found:
            raise LookupError("{} not present in list\n".format(term))
        if prev == None:
            self.head = current.getNext()
        else:
            prev.setNext(current.getNext())
    
    def append(self, item):
        current = self.head
        n = Node(item)
        if current == None:
            self.head = n
        else:
            while current.getNext() != None:
                current = current.getNext()
            current.setNext(n)

    def index(self, item) -> int:
        current = self.head
        if current == None:
            raise LookupError("Empty List!")
        found = False
        count = 0
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                count += 1
                current = current.getNext()
        if not found:
            raise LookupError("{} not present in list".format(item))
        return count
    
    def pop(self):
        current = self.head
        prev = None
        while current.getNext() != None:
            prev = current
            current = current.getNext()
        prev.setNext(None)
        return current.getData()
    
    def insert(self,index,item):
        current = self.head
        prev = None
        for i in range(index):
            prev = current
            current = current.getNext()
        n = Node(item)
        prev.setNext(n)
        n.setNext(current)
    
newList = UnorderedList()
for i in [1, 2, 3, 4, 5]:
    newList.add(i)
print(newList.size())
newList.insert(2, 10)
c = newList.getHead()
while c != None:
    print(c.getData())
    c = c.getNext()