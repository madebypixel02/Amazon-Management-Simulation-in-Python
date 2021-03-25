from src.queues import Queue
class Vertex:
    def __init__(self, vertex):
      """This constructor function takes the id of the vertes and creates
      and empty list to store its adjacent vertices"""
      self.id = vertex
      self.neighbors = []
        
    def addNeighbor(self, vertex):
      """This functions takes the id of a vertex 
      adds its id as a new adjacent vertex for the vertex"""
      if vertex.id not in self.neighbors:
          #we only have to save the id of the vertex
          self.neighbors.append(vertex.id)
          self.neighbors = sorted(self.neighbors)
     
        
    def getNeighbors(self):
      """Returns the list of adjacent vertices"""
      return self.neighbors
      
    def __str__(self):
      return str(self.id) + ' connectedTo: ' + str([x for x in self.neighbors])

class Graph:
    def __init__(self):
        self.vertices = {}
        self.visited = []
        self.queue = Queue()

    def addVertex(self,key):
        newVertex = Vertex(key)
        self.vertices[key] = newVertex

    def getVertex(self,n):
        if n in self.vertices:
            return self.vertices[n]
        else:
            return None

    def __contains__(self,n):
        return n in self.vertices

    def addEdge(self,start,end):
        if start not in self.vertices:
            self.addVertex(start)
        if end not in self.vertices:
            self.addVertex(end)
        self.vertices[start].addNeighbor(self.vertices[end])

    def getVertices(self):
        return self.vertices.keys()

    def __iter__(self):
        return iter(self.vertices.values())
      
    def __str__(self):
        result=''
        for x in iter(self):
            result+=str(x)+'\n'
            
        return result
    
    def breadthFirstTraversal(self, vertex):
        print("Breadth-first traversal: ", end='')
        self.visited.clear()
        self.queue.enqueue(vertex)
        while self.queue.isEmpty() == False:
            current = self.queue.dequeue()
            if current not in self.visited:
                print(current.id, end = ' ')
                self.visited.append(current)
                adjLst = self.vertices[current.id].neighbors
                for v in adjLst:
                    self.queue.enqueue(self.getVertex(v))
        
