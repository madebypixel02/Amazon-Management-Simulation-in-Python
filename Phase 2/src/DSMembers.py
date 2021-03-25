from src.DoublyLinkedList import DList
from src.DSMember import DSMember
class DSMembers(DList):
    def __init__(self):
        super().__init__()
    # T(n) = 3
    
    def addMember(self,iD, name, lastname, status):
        member = DSMember(iD, name, lastname, status)
        if self.__size == 0:
            self.addFirst(member)
        else:
            nodelt = self.__head
            index = 0
            while nodelt != None:
                if nodelt.element.lastname > member.lastname:
                    return self.insertAt(index, member)
                else:
                    index +=1
                    nodelt = nodelt.next
            return self.addLast(member)
    # T(n) = 4n² + 13n + 38. Best: List is empty. Worst: List is not empty and the lastname goes at the end of the members list.
    
    def addCreatedMember(self, member):
        if self.size == 0:
            self.addFirst(member)
        else:
            nodelt = self.head
            index = 0
            while nodelt != None:
                if nodelt.element.lastname > member.lastname:
                    return self.insertAt(index, member)
                else:
                    index +=1
                    nodelt = nodelt.next
            return self.addLast(member)
    # T(n) = 4n² + 13 + 23. Best: List is empty. Worst: List is not empty and the lastname goes at the end of the members list.
    
    def printMembers(self):
        nodelt = self.head
        string = ''
        while nodelt is not None:
            if nodelt.next is not None:
                print(str(nodelt.element.name) + ' ' + str(nodelt.element.lastname) +',', end=' ')
                string+=str(nodelt.element.name) + ' ' + str(nodelt.element.lastname) +', '
               
            else:
                print(str(nodelt.element.name) + ' ' + str(nodelt.element.lastname), end = '')
                string+=str(nodelt.element.name) + ' ' + str(nodelt.element.lastname)
            nodelt = nodelt.next
        return string
    # T(n) = 6n + 1. Best: The member list has no entries. Worst: List is rather long.

    
    def deleteMember(self, member):
        nodelt = self.head
        index = 0
        while nodelt != None:
            if nodelt.element == member:
                self.removeAt(index) # T(n) = 5n + 6
                return
            else:
                index +=1
                nodelt = nodelt.next
        print("Distributor could not be found in that zone")
    # T(n) = n(5n + 7) + 2 = 5n² + 7n + 2. Best: Member to be removed is at the first node. Worst: member is not in the zone.
                

