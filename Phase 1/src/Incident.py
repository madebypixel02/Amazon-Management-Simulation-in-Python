from src.DoublyLinkedList import DList

class Incident:
    def __init__(self, packId, deliverId):
        self.__packId = packId
        if deliverId != None: #ATTEMPTS EXCEEDED
            self.__reason = 'Number of delivery attempts exceeded'
            self.__deliverId = deliverId
        else: #STAFF NOT AVAILABLE
            self.__reason = 'No delivery staff members available'
            self.__deliverId = None
    # T(n) = 3
            
class Incidents(DList):
    def __init__(self):
        super().__init__()
    # T(n) = 3
    
    def addIncident(self, package, deliverman = None):
        packiD = package.packnumber
        if deliverman != None:
            deliverId = deliverman.iD
        else:
            deliverId = None
        entry = Incident(packiD, deliverId) # T(n) = 3
        self.addLast(entry) # T(n) = 10
    # T(n) = 15