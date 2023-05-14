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

    
newList = UnorderedList()
newList.append(12)
newList.add(7)
newList.add(4)
print(newList.size())
print(newList.index(22))