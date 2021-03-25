from src.DoublyLinkedList import DList

class DeliveredPackage():
    def __init__(self, packId, deliverId):
        self.__packId = packId
        self.__deliverId = deliverId
    # T(n) = 2

class Delivered(DList):
    def __init__(self):
        super().__init__()
    # T(n) = 3
    
    def addEntry(self, package, deliveryman):
        packId = package.packnumber
        deliverId = deliveryman.iD
        entry = DeliveredPackage(packId, deliverId)
        self.addLast(entry)
    # T(n) = 15
    