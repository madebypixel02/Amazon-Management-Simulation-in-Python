class DNode:
    def __init__(self, e, n=None, p = None):
        self.__element = e
        self.__next = n
        self.__prev = p
    # T(n) = 3
    
    @property
    def element(self):
        return self.__element
    # T(n) = 1
    
    @property
    def next(self):
        return self.__next
    # T(n) = 1

    @property
    def prev(self):
        return self.__prev
    # T(n) = 1
    
    @element.setter
    def element(self, value):
        self.__element = value
    # T(n) = 1
    
    @next.setter
    def next(self, value):
        self.__next = value
    # T(n) = 1
    
    @prev.setter
    def prev(self, value):
        self.__prev = value
    # T(n) = 1

class DList:
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__size = 0
    # T(n) = 3
    
    def isEmpty(self):
        return self.__size == 0
    # T(n) = 2
    
    def addFirst(self, e):
        if self.isEmpty():
            newNode = DNode(e)
            self.__head = newNode
            self.__tail = newNode
            self.__size += 1
        else:
            newNode = DNode(e)
            newNode.next = self.__head
            self.__head.prev = newNode
            self.__head = newNode
            self.__size += 1
    # T(n) = 9
    
    def addLast(self, e):
        if self.isEmpty():
            newNode = DNode(e)
            self.__head = newNode
            self.__tail = newNode
            self.__size += 1
            return
        else:
            newNode = DNode(e)
            newNode.prev = self.__tail
            self.__tail.next = newNode
            self.__tail = newNode
            self.__size += 1
            return
    # T(n) = 10
    
    def removeFirst(self):
        if self.isEmpty():
            print("Can't remove element from an empty list!!")
            return None
        else:
            elem = self.__head.element
            self.__head = self.__head.next
            if self.__head == None: #In case the list only has one node
                self.__tail = None
            else:
                self.__head.prev = None
            self.__size -= 1
            return elem
    # T(n) = 6
    
    def removeLast(self):
        if self.isEmpty():
            print("Can't remove elements from an empty list!!")
            return None
        else:
            elem = self.__tail.element
            self.__tail = self.__tail.prev
            if self.__tail is None:
                self.__head = None
            else:
                self.__tail.next = None
            self.__size -= 1
            return elem
    # T(n) = 6
    
    def insertAt(self, index, e):
        if index == 0:
            self.addFirst(e)
        elif index > self.__size - 1:
            while self.__size <  index:
                self.addLast(0)
            self.addLast(e)
        else:
            node = self.__head
            counter = index - 1
            while counter > 0:
                node = node.next
                counter -= 1
            newNode = DNode(e)
            node.next.prev = newNode
            node.next = newNode
            self.__size += 1
    # T(n) = 4n + 11. Best: Index is first node. Worst: index is the last node.
            
    def getAt(self, index):
        if index < 0 or index > self.__size - 1:
            print("Index out of range")
        else:
            node = self.__head
            counter = index
            while counter > 0:
                node = node.next
                counter -= 1
            return node.element
    # T(n) = 4n + 3. Best: Search value is at the head. Worst: Search value is not on the list or is at the last node.
    
    def contains(self, e):
        node = self.__head
        while 0 == 0:
            if node.element == e:
                return True
            elif node.next is None:
                return None
            else:
                node = node.next
    # T(n) = 2n + 1. Best: Search value is at the head. Worst: Value is not on the list or is at the last node
    
    def removeAt(self, index):
        if index < 0 or index > self.__size - 1:
            print("Index out of range")
            return
        elif index == 0:
            self.removeFirst()
            return
        elif index == self.__size - 1:
            self.removeLast()
            return
        else:
            prevNode = self.__head
            nextNode = prevNode.next.next
            counter = index - 1
            while counter > 0:
                prevNode = prevNode.next
                nextNode = nextNode.next
                counter -= 1
            prevNode.next = nextNode
            nextNode.prev = prevNode
    # T(n) = 5n + 6. Best: index out of rance. Worst: Index at last node.
    
    def printElements(self):
        node = self.__head
        string = ''
        while node != None:
            string+= str(node.element)
            node = node.next
            if node != None:
                string+=', '
        return string
    # T(n) = 3n + 2. Best: List is empty. Worst: List is not empty.
                
    """
    def removeAll(self, e):
        if self.isEmpty():
            print("Can't remove elements from an empty list")
            return
        else:
            node = self.__head
            while 0 == 0:
                if node.element == e:
                    node.next.prev = node.prev
    # T(n) = 2n + 1
            
        """
    
    #getters
    @property
    def size(self):
        return self.__size
    # T(n) = 1
    
    @property
    def head(self):
        return self.__head
    # T(n) = 1
    
    @property
    def tail(self):
        return self.__tail
    # T(n) = 1
    
    #setters
    @size.setter
    def size(self,value):
        self.__size = value
    # T(n) = 1
    
    @head.setter
    def head(self,value):
        self.__head = value
    # T(n) = 1
        
    @tail.setter
    def tail(self,value):
        self.__tail = value
    # T(n) = 1
    
        
        