class Queue:
    def __init__(self):
        self.__list = []
    
    def enqueue(self, e):
        self.__list.append(e)
    
    def dequeue(self):
        return self.__list.pop(0)
    
    def isEmpty(self):
        if len(self.__list) == 0:
            return True
        else:
            return False
    
q = Queue()
a = [1,2,3,4,5,6,7,8,9,10,11,12,13]
