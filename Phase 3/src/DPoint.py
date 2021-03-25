class DPoint:
    def __init__(self, Id, street_name, number, postal_code):
      self.__Id = Id
      self.__streetName = street_name
      self.__number = number
      self.__postalCode = postal_code
      self.__neighbors = []
        
    def addNeighbor(self, vertex):
      """This functions takes the id of a vertex 
      adds its id as a new adjacent vertex for the vertex"""
      if vertex.id not in self.__neighbors:
          #we only have to save the id of the vertex
          self.__neighbors.append(vertex.id)
          self.__neighbors = sorted(self.__neighbors)
     
        
    def getNeighbors(self):
      """Returns the list of adjacent vertices"""
      return self.__neighbors
      
    def __str__(self):
        result = ''
        result+="\tDZone "+str(self.__Id) + ' connected to: '
        for i in self.__neighbors:
            result+="\n\t\tDZone "+str(i[0])+" (distance "+str(i[1])+")"
        return result
    
    def generateRoute(self):
        return
    

    @property
    def Id(self):
        return self.__Id
    
    @property
    def streetName(self):
        return self.__streetName
    
    @property
    def number(self):
        return self.__number
    
    @property
    def postalCode(self):
        return self.__postalCode
    
    @property
    def neighbors(self):
        return self.__neighbors
    
    @Id.setter
    def Id(self, value):
        self.__Id = value
    
    @neighbors.setter
    def neighbors(self, value):
        self.__neighbors = value

