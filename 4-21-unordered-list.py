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

    
newList = UnorderedList()
newList.add(1)
newList.add(3)
newList.add(9)