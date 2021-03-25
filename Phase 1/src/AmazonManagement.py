import random
from src.Orders import Orders
from src.Incident import Incidents
from src.DSMembers import DSMembers
from src.Delivered import Delivered
from src.Package import Package
class AmazonManagement:
    def __init__(self):
        self.__orders = Orders()
        self.__members = DSMembers()
        self.__incidents = Incidents()
        self.__delivered = Delivered()
    # T(n) = 15

    def loadOrders(self,package_number, deliver_address, postal_code):
        pack = Package(package_number, deliver_address, postal_code)
        self.__orders.addLast(pack)
    # T(n) = 21
    
    def loadDSMembers(self,iD, name, lastname, status):
        self.__members.addMember(iD, name, lastname, status)
    # T(n) = 4n² + 13n + 28

    
    def showDSMembers(self):
        nodelt = self.__members.head
        string = ''
        while nodelt != None:
            string+= nodelt.element.printInfo() # T(n) = 3n + 2
            nodelt = nodelt.next
        return string
    # T(n) = 1 + n + n(3n + 3) = 3n² + 4n + 1. Best: only one entry. Worst: Several entries
    
    def showOrders(self):
        nodelt = self.__orders.head
        string = ''
        while nodelt != None:
            string+= nodelt.element.printInfo() # T(n) = 3n + 2
            #string+="\n"
            nodelt = nodelt.next
        return string
    # T(n) = 3n² + 4n + 1
    
    def assignDistribution(self):
        while self.__orders.isEmpty() == False:
            package = self.__orders.removeFirst() # T(n) = 1 + 6 = 7
            zone = package.postcode
            nodelt = self.__members.head
            condition = True
            while nodelt != None: #CHECKS IF PACKAGE CAN BE ASSIGNED TO EXISTING ACTIVE MEMBER, T(n) = 14n
                if nodelt.element.deliv_zones.isEmpty(): 
                    nodelt = None
                else:
                    if nodelt.element.deliv_zones.contains(zone) and nodelt.element.status == "ACTIVE":
                        nodelt.element.assigned_packages.addLast(package)
                        condition = False
                        nodelt = None
                    if nodelt != None:
                        nodelt = nodelt.next
            if condition: #THIS SOLVES PACKAGES BEING DISTRIBUTED TWICE, 
                nodelt = self.__members.head
                indexelt = 0
                index_target = None
                zones = 9999
                while nodelt!=None: # T(n) = 6n
                    if nodelt.element.deliv_zones.size < zones and nodelt.element.status == "ACTIVE":
                        zones = nodelt.element.deliv_zones.size
                        index_target = indexelt
                    indexelt += 1
                    nodelt = nodelt.next
                if index_target == None:
                    self.__incidents.addIncident(package)
                else: # T(n) = 4n + 4 + 11 + 11 = 4n + 26
                    member = self.__members.getAt(index_target)
                    member.addZone(zone)
                    member.addPackage(package)
    # T(n) = n(24n + 40) + n = 24n² + 41n
    
    def deliverPackages(self, iD):
        nodelt = self.__members.head
        member = None
        while nodelt != None and member == None: # T(n) = 5n
            if nodelt.element.iD == str(iD):
                member = nodelt.element
            nodelt = nodelt.next
        if member == None:
            print("ID number not found")
            return
        print(member.name + ' ' + member.lastname + ':')
        while member.assigned_packages.size > 0: # T(n) = 30n
            package = member.assigned_packages.removeFirst()
            if package.strikes > 0:
                pure_chance = random.randint(0,1)
                if pure_chance == 1:
                    self.__delivered.addEntry(package, member)
                    print("Package " + str(package.packnumber)+': '
                          + "Correctly Delivered")
                else:
                    package.strikes -= 1
                    print("Package " + str(package.packnumber)+': '
                          + "Pending (" + str(package.strikes)+' remaining attempts)')
                    member.assigned_packages.addLast(package)
            else:
                self.__incidents.addIncident(package, member)
                print("Package " + str(package.packnumber)+': '
                          + "Removed")
        print()
    # T(n) = 35n + 7. Best: ID not found. Worst: ID found and the 3 package strikes happen.
                
    def deliver(self):
        nodelt = self.__members.head
        while nodelt != None:
            member_iD = nodelt.element.iD
            if nodelt.element.status == 'ACTIVE':
                self.deliverPackages(member_iD) # T(n) = 35n + 7
            nodelt = nodelt.next
    # T(n) = 1 + n + n(35n + 9) = 35n² + 10n + 1. Best: nodelt is head. Worst: nodelt is the last node (status is inactive for several members).
    
    def removeDSMembr(self, iD):
        nodelt = self.__members.head
        member = None
        while nodelt != None and member == None: # T(n) = 3n
            if nodelt.element.iD == str(iD):
                member = nodelt.element
            nodelt = nodelt.next
        member.status = "INACTIVE"
        while member.assigned_packages.isEmpty() is False: # T(n) = 18n
            package = member.assigned_packages.removeFirst()
            self.__orders.addLast(package)
        print('Member %s %s set Inactive'%(member.name, member.lastname))
        self.assignDistribution() # T(n) = 24n² + 41n
        print()
    # T(n) = 24n² + 62n + 5. Best: self.__members.head is None. Worst: nodelt is the last node.
    
    @property
    def orders(self):
        return self.__orders
    # T(n) = 1
    
    @property
    def incidents(self):
        return self.__incidents
    # T(n) = 1
    
    @property
    def delivered(self):
        return self.__delivered
    # T(n) = 1
    
    @property
    def members(self):
        return self.__members
    # T(n) = 1
        
            


