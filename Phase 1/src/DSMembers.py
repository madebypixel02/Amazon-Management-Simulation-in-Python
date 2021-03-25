from src.DoublyLinkedList import DList
from src.DSMember import DSMember
class DSMembers(DList):
    def __init__(self):
        super().__init__()
    # T(n) = 3
    
    def addMember(self,iD, name, lastname, status):
        member = DSMember(iD, name, lastname, status) # T(n) = 1 + 14 = 15
        if self.size == 0:
            self.addFirst(member) # T(n) = 9
        else:
            nodelt = self.head
            index = 0
            while nodelt != None:
                if nodelt.element.lastname > member.lastname:
                    return self.insertAt(index, member) # T(n) = 1 + (4n + 11) = 4n + 12
                else:
                    index +=1
                    nodelt = nodelt.next
            return self.addLast(member) # T(n) = 1 + 10 = 11
    # T(n) = 38 + n(4n + 12) + n = 4n² + 13n + 38. Best: List is empty. Worst: List is not empty and the lastname goes at the end of the members list.
        

