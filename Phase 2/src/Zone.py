from src.DSMembers import DSMembers
class Zone:
    def __init__(self, elem = None):
        self.__elem = elem
        self.__members = DSMembers()
        self.__leftChild = None
        self.__rightChild = None
        self.__parent = None
    # T(n) = 7
        
    
    @property
    def elem(self):
        return self.__elem
    # T(n) = 1
    
    @property
    def leftChild(self):
        return self.__leftChild
    # T(n) = 1
    
    @property
    def rightChild(self):
        return self.__rightChild
    # T(n) = 1
    
    @property
    def parent(self):
        return self.__parent
    # T(n) = 1
    
    @property
    def members(self):
        return self.__members
    # T(n) = 1
    
    @elem.setter
    def elem(self, value):
        self.__elem = value
    # T(n) = 1
    
     
    @leftChild.setter
    def leftChild(self,value):
        self.__leftChild = value
    # T(n) = 1
        
    @rightChild.setter
    def rightChild(self, value):
        self.__rightChild = value
    # T(n) = 1
    
    @parent.setter
    def parent(self, value):
        self.__parent = value
    # T(n) = 1
    
    @members.setter
    def members(self,value):
        self.__members = value
    # T(n) = 1

