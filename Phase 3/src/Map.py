from src.queues import Queue

from src.DPoint import DPoint

import sys

class Map:
    def __init__(self):
        self.__deliveryZones = {}
        self.__route = []
        self.__queue = Queue()
        self.__counter = 0 #keeps track of the number of available delivery points
    
    def addDeliveryPoint(self, street_name, number, postal_code):
        self.__counter += 1
        self.__deliveryZones[self.__counter] = DPoint(self.__counter, street_name, number, postal_code)
        print("Delivery zone "+str(self.__counter)+" added!")
    
    def addConnection(self, zone1, zone2, distance):
        self.__deliveryZones[zone1].neighbors.append([zone2, distance])
        self.__deliveryZones[zone2].neighbors.append([zone1, distance])
    
    def removeConnection(self, zone1, zone2):
        if zone1 not in self.__deliveryZones.keys() or zone2 not in self.__deliveryZones.keys(): #check that both zones exist
            print("Delivery Zone not found")
            return
        condition = self.areConnected(zone1, zone2)
        if condition == -1:
            print("DZone "+str(zone1)+" and DZone "+str(zone2)+" are not directly connected...")
            return
        else:
            n1 = self.__deliveryZones[zone1].neighbors
            n2 = self.__deliveryZones[zone2].neighbors
            c1 = True
            c2 = True
            i=0
            while c1:
                if n1[i][0] == zone2:
                    n1.pop(i)
                    c1 = False
                else:
                    i+=1
            
            i=0
            while c2:
                if n2[i][0] == zone1:
                    n2.pop(i)
                    c2 = False
                else:
                    i+=1
            print("(DZone "+str(zone1)+" - DZone "+str(zone2)+") connection removed.")
    
    def __str__(self):
        result=''
        result +="Delivery zones:\n"
        for i in self.__deliveryZones.values():
            result+=str(i)+'\n'
        return result
    
    def areConnected(self, zone1, zone2):
        if zone1 not in self.__deliveryZones.keys() or zone2 not in self.__deliveryZones.keys(): #check that both zones exist
            print("Delivery Zone not found")
            return
        n1 = self.__deliveryZones[zone1].neighbors
        d = -1
        for i in range(len(n1)):
            if n1[i][0] == zone2:
                d = n1[i][1]
                return d
        return d
    
    """
    def dfs(self): 
        ""This function prints all vertices of the graph by the DFS traversal.""
        
        print('dfs traversal:')
        # Mark all the vertices as not visited 
        visited={}
        for v in self.__deliveryZones.keys():
            visited[v]=False
    
        for v in  self.__deliveryZones.keys():
            if visited[v]==False:
              self._dfs(v, visited)
        print() 
    

    def _dfs(self, v, visited): 
        # Mark the current node as visited and print it 
        visited[v] = True
        #print(v, end = ' ') 
        #Instead of printing the index, we have to print its label
        print(v,end=' ')
        # Recur for all the vertices  adjacent to this vertex 
        for adj in self.__deliveryZones[v].neighbors: 
            if visited[adj[0]] == False: 
                self._dfs(adj[0], visited)
    """
    
    
    def _dfs2list(self, v, visited): 
        # Mark the current node as visited and print it 
        visited[v] = True
        #print(v, end = ' ') 
        #Instead of printing the index, we have to print its label
        self.__route.append(v)
        # Recur for all the vertices  adjacent to this vertex 
        for adj in self.__deliveryZones[v].neighbors: 
            if visited[adj[0]] == False: 
                self._dfs2list(adj[0], visited)
    
    
    def generateRoute(self):
        self.__route = []
        print('Generated route: ', end = '')
        # Mark all the vertices as not visited 
        visited={}
        for v in self.__deliveryZones.keys():
            visited[v]=False
    
        for v in  self.__deliveryZones.keys():
            if visited[v]==False:
              self._dfs2list(v, visited)
        print(str(self.__route))
        return self.__route
    
    
    def minDistance(self, distances, visited): 
        """This functions returns the vertex (index) whose associated value in
        the dictionary distances is the smallest value. We 
        only consider the set of vertices that have not been visited"""
        # Initilaize minimum distance for next node 
        min = sys.maxsize 

        #returns the vertex with minimum distance from the non-visited vertices
        for vertex in self.__deliveryZones.keys(): 
            if distances[vertex] <= min and visited[vertex] == False: 
                min = distances[vertex] #update the new smallest
                min_vertex = vertex      #update the index of the smallest
    
        return min_vertex 
    
    
    def dijkstra(self, origin, destination): 
        """"This function takes a vertex v and calculates its mininum path 
        to the rest of vertices by using the Dijkstra algoritm"""  
        
        #visisted is a dictionary whose keys are the verticies of our graph. 
        #When we visite a vertex, we must mark it as True. 
        #Initially, all vertices are defined as False (not visited)
        visited={}
        for v in self.__deliveryZones.keys():
            visited[v]=False

        #this dictionary will save the previous vertex for the key in the minimum path
        previous={}
        for v in self.__deliveryZones.keys():
            #initially, we defines the previous vertex for any vertex as None
            previous[v]=None


        #This distance will save the accumulate distance from the  
        #origin to the vertex (key)
        distances={}
        for v in self.__deliveryZones.keys():
            distances[v]=sys.maxsize


        #The distance from origin to itself is 0
        distances[origin] = 0
        
        for n in range(len(self.__deliveryZones)): 
            # Pick the vertex with the minimum distance vertex.
            # u is always equal to origin in first iteration 
            u = self.minDistance(distances, visited) 

            visited[u] = True
            
            # Update distance value of the u's adjacent vertices only if the current  
            # distance is greater than new distance and the vertex in not in the shotest path tree 
            
            #we must visit all adjacent vertices (neighbours) for u
            for adj in self.__deliveryZones[u].neighbors: 
                i=adj[0]
                w=adj[1]
                if visited[i]==False and distances[i]>distances[u]+w:
                    #we must update because its distance is greater than the new distance
                    distances[i]=distances[u]+w   
                    previous[i]=u       
                
        #finally, we print the minimum path from origin to the other vertices
        return self.printSolution(distances,previous,origin, destination)
    
    
    def printSolution(self, distances, previous, origin, destination):
        if distances[destination]==sys.maxsize:
                print("There is not path from ",origin,' to ',destination)
        else: 
            #minimum_path is the list wich contains the minimum path from v to i
            minimum_path=[]
            prev=previous[destination]
            #this loop helps us to build the path
            while prev!=None:
                minimum_path.insert(0,prev)
                prev=previous[prev]
            
            #we append the last vertex, which is i
            minimum_path.append(destination)
            minimum_path.append(distances[destination])
            #we print the path from v to i and the distance
            print(origin,'->',destination,":", minimum_path,distances[destination])
            return minimum_path
    
    def minRoute(self, origin, destination):
        print("Computing shortest path from "+str(origin)+" to "+str(destination)+":")
        return self.dijkstra(origin, destination)
    
    @property
    def deliveryZones(self):
        return self.__deliveryZones
    
    @property
    def route(self):
        return self.__route
    
    @property
    def queue(self):
        return self.__queue
    
    @property
    def counter(self):
        return self.__counter

