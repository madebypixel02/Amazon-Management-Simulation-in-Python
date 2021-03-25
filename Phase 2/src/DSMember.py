from src.DoublyLinkedList import DList
class DSMember:
    def __init__(self,iD, name, lastname, status):
        self.__iD = 'R'+ str(iD)
        self.__name = name
        self.__lastname = lastname
        if status == True:
            self.__status = 'ACTIVE'
        else:
            self.__status = 'INACTIVE'
        self.__deliv_zones = DList()
        self.__assigned_packages = DList()
    # T(n) = 14
    
    
    def addZone(self, zone):
        self.__deliv_zones.addLast(zone)
        return
    # T(n) = 11
    
    def addPackage(self, package):
        self.__assigned_packages.addLast(package)
        return
    # T(n) = 11
    
    
    def printInfo(self):
        print(self.__lastname + ', '  + self.__name 
              + '\n\tID:' + str(self.__iD) 
              + '\n\tStatus:' + self.__status 
              + '\n\tZones: ', end = '') # T(n) = 9
        if self.__deliv_zones.isEmpty():
            print('None', end = '')
        else: 
            self.__deliv_zones.printElements() # T(n) = 3n + 2
        print('\n\tPackages: ', end = '')
        if self.__assigned_packages.size == 0:
            print("None")
            print()
            return
        else:
            nodelt = self.__assigned_packages.head
            while nodelt != None:
                print(nodelt.element.packnumber, end = '')
                if nodelt.next != None:
                    print(', ', end = '')
                nodelt = nodelt.next
            print()
            print()
            return
    # T(n) = 4n + 4 + 1 + 3n + 2 + 9 = 7n + 16
        
    
    @property
    def iD(self):
        return self.__iD
    # T(n) = 1
    
    @property
    def deliv_zones(self):
        return self.__deliv_zones
    # T(n) = 1
    
    @property
    def status(self):
        return self.__status
    # T(n) = 1
    
    @property
    def name(self):
        return self.__name
    # T(n) = 1
    
    @property
    def lastname(self):
        return self.__lastname
    # T(n) = 1
    
    @property
    def assigned_packages(self):
        return self.__assigned_packages
    # T(n) = 1
    
    @status.setter
    def status(self, value):
        self.__status = value
    # T(n) = 1