from src.DoublyLinkedList import DList
from src.Zone import Zone
class Zones:
    def __init__(self):
        self.__root = None
        self.__temp = None #this attribute will be used to find the node with the lowest number of distributors
        self.__listTempLow = None #this attribute will be used to temporarily store lower nodes when deleting a zone
        self.__listTempHigh = None #this attribute will be used to temporarily store higher nodes when deleting a zone
    # T(n) = 1
    
    def _size(self, currentNode):
        if currentNode == None:
            return 0
        return 1 + self._size(currentNode.leftChild) + self._size(currentNode.rightChild)
    # T(n) = O(n)
    
    def size(self, node = None):
        "Returns the number of nodes"
        return self._size(node)
    # T(n) = O(n)
    
    def _height(self, currentNode):
        if currentNode == None:
            return -1
        return 1 + max(self._height(currentNode.leftChild), self._height(currentNode.rightChild))
    # T(n) = O(n). Best: currentNode is at the lowest level and has no children. Worst: currentNode is the root.
    
    def height(self):
        "Returns the height of a tree"
        return self._height(self.__root)
    # T(n) = O(n)
    
    def _depth(self, currentNode):
        if currentNode == None:
            return 0
        return 1 + self._depth(currentNode.parent)
    # T(n) = O(n). Best: currentNode is the root (no children). Worst: currentNode is at the lowest level.
    
    def depth(self):
        "Returns the depth of a node"
        return self._depth(self.root)
    # T(n) = O(n)
    
    def insert(self, x):
        if self.__root is None:
            self.__root = Zone(x)
        else:
            self.insertNode(self.__root, x)
        print(str(x)+" inserted!")
    # T(n) = O(n)
    
    
    def insertNode(self, node, x):
        if node.elem == x:
            print("X already exists!!")
            return
        if x < node.elem:
            if node.leftChild is None:
                newNode = Zone(x)
                node.leftChild = newNode
                newNode.parent = node
            else:
                self.insertNode(node.leftChild, x)
        else: #if x > node.elem
            if node.rightChild is None:
                newNode = Zone(x)
                node.rightChild = newNode
                newNode.parent = node
            else:
                self.insertNode(node.rightChild, x)
    # T(n) = O(n). Best: the value already exists at the starting node. Worst: the new node has either the smallest or the largest value in the tree (assuming it is balanced)
    
    def find(self, x):
        return self.findNode(self.__root, x)
    # T(n) = O(n)
    
    def findNode(self, node, x):
        if node is None:
            return None
        if node.elem == x:
            return node
        
        if x < node.elem:
            return self.findNode(node.leftChild, x)
        if x > node.elem:
            return self.findNode(node.rightChild, x)
    # T(n) = O(n). Best: Value is found at starting node. Worst: value is the largest of the tree or not on it.
    
    def remove(self, x):
        node = self.find(x)
        if node is None:
            print("Node to be removed not found")
            return
        self.removeNode(node)
    # T(n) = O(n)
    
    def removeNode(self, node):
        # First case: node doesn't have any children
        if node.leftChild is None and node.rightChild is None:
            if node.parent is not None:
                if node.parent.leftChild is node:    
                    node.parent.leftChild = None
                else:
                    node.parent.rightChild = None
                node.parent = None
            else: #node.parent == None
                self.__root = None #remove the root
        
        # Second case: only one child (the left child)
        if node.leftChild is not None and node.rightChild is None:
            if node.parent is not None:
                if node.parent.leftChild is node:
                    node.parent.leftChild = node.leftChild
                    node.leftChild.parent = node.parent
                else:
                    node.parent.rightChild = node.leftChild
                    node.leftChild.parent = node.parent
            else:
                self.__root = node.leftChild
            
        # Second case: only one child (the right child)
        if node.rightChild is not None and node.leftChild is None:
            if node.parent is not None:
                if node.parent.leftChild is node:
                    node.parent.leftChild = node.rightChild
                    node.rightChild.parent = node.parent
                else:
                    node.parent.rightChild = node.rightChild
                    node.rightChild.parent = node.parent
            else:
                self.__root = node.rightChild
        
        # Third case: two children
        
        if node.leftChild is not None and node.rightChild is not None:
            #find the successor of the node
            successor = node.rightChild
            while successor.leftChild is not None:
                successor = successor.leftChild
            node.elem = successor.elem #replace node's element by successor's
            self.removeNode(successor) #remove successor
    # T(n) = O(n). Best: node to remove is of the first case (node to remove is root and has no children). Worst: node to remove is of the third case (node to remove has two children)

    def createZone(self, zone_iD):
        self.insert(zone_iD) # T(n) = O(n)
        self.sizeBalanceTree()
    
    def isBalanced(self, node):
        if abs(self.size(node.leftChild) - self.size(node.rightChild)) < 2:
            return True
        else:
            return False
    # T(n) = O(n)
        
    def sizeBalanceTree(self):
        self.sizeBalance(self.__root)
        print("Balance Sequence Completed")
        return
    
    #PLEASE CARRY ALSO DSMEMBERS
    def sizeBalance(self, node):
        if node == None:
            print("is none", end = ' ')
            return
        print("Balancing "+str(node.elem))
        if self.isBalanced(node):
            print(str(node.elem)+" is balanced")
            self.sizeBalance(node.leftChild)
            print("left " + '('+str(node.elem)+')')
            self.sizeBalance(node.rightChild)
            print("right "+ '('+str(node.elem)+')')
        else:
            print(str(node.elem)+" is NOT balanced")
            if self.size(node.leftChild) > self.size(node.rightChild):
                print("Thera are more nodes on the left")
                predecessor = node.leftChild
                while predecessor.rightChild is not None:
                    predecessor = predecessor.rightChild
                successor = node.rightChild
                if successor is not None: #there might be no nodes in the right subtree yet
                    while successor.leftChild is not None:
                        successor = successor.leftChild
                newNode= Zone(node.elem)
                newNode.members = node.members
                if successor is not None:
                    successor.leftChild = newNode
                    newNode.parent = successor 
                else:
                    node.rightChild = newNode
                    newNode.parent = node
                node.elem = predecessor.elem
                node.members = predecessor.members
                self.remove(predecessor.elem)
                print()
                if node == self.__root:
                    print("NEW ROOT: " + str(node.elem))
                else:
                    print("NEW SUBTREE ROOT: "+ str(node.elem))
                print()
                self.sizeBalance(node)
                
                
            else:
                print("There are more nodes on the right")
                predecessor = node.leftChild
                if predecessor is not None:
                    while predecessor.rightChild is not None:
                        predecessor = predecessor.rightChild
                successor = node.rightChild
                while successor.leftChild is not None:
                    successor = successor.leftChild
                newNode = Zone(node.elem)
                newNode.members = node.members
                if predecessor is not None:
                    predecessor.rightChild = newNode
                    newNode.parent = predecessor
                else:
                    node.leftChild = newNode
                    newNode.parent = node
                node.elem = successor.elem 
                node.members = successor.members
                self.remove(successor.elem)
                print()
                if node == self.__root:
                    print("NEW ROOT: " + str(node.elem))
                else:
                    print("NEW SUBTREE ROOT: "+str(node.elem))
                print()
                self.sizeBalance(node)

    # Height balancing
    # Rotations            
    def leftLeft(self, node):
        print(f"\nStarting left-left rotation on {node.elem}...")
        if node.leftChild.leftChild is None:
            print(f"Pausing current rotation because {node.leftChild.elem} has no left child, performing left-right rotation first.")
            self.leftRight(node)
            print(f"\nResuming left-left rotation on {node.elem}...")
        if node.leftChild.leftChild is not None and node.leftChild.rightChild is not None:
            if self._height(node.leftChild.rightChild) > 0:
                print(f"Loop structure detected!!\nPatching (passing elements from the right to the left branch of {node.leftChild.elem})... \nNodes remaining: {self._size(node.leftChild.rightChild) - 1}")
                while node.leftChild.rightChild.rightChild is not None:
                    self.rightRight(node.leftChild)
                    if self._size(node.leftChild.rightChild) - 1 > 0:
                        print("Nodes remaining:", self._size(node.leftChild.rightChild))
                    else:
                        print("Nodes remaining: 0 -> Loop patched!\n")
        newRoot = node.leftChild
        if node.parent is not None and node.parent.rightChild == node:
            node.parent.rightChild = newRoot
        newRoot.parent = node.parent
        if newRoot.rightChild is not None:
            print(f"Found right child on {newRoot.elem} ({newRoot.rightChild.elem}), passing it to the right branch...")
            node.leftChild = newRoot.rightChild
            newRoot.rightChild.parent = node
        else:
            print(f"No right child found on {newRoot.elem}, skipping...")
            node.leftChild = None
        newRoot.rightChild = node
        node.parent = newRoot
        print(f"Left-left rotation done. New root is {newRoot.elem} (Children: {newRoot.leftChild.elem} and {newRoot.rightChild.elem})")
        return newRoot


    def rightRight(self, node):
        print(f"\nStarting right-right rotation on {node.elem}...")
        if node.rightChild.rightChild is None:
            print(f"Pausing current rotation because {node.rightChild.elem} has no right child. Performing right-left rotation first.")
            self.rightLeft(node)
            print(f"\nResuming right-right rotation on {node.elem}...")
        if node.rightChild.leftChild is not None and node.rightChild.rightChild is not None:
            if self._height(node.rightChild.leftChild) > 0:
                print(f"Loop structure detected!!\nPatching (passing elements from the left to the right branch of {node.rightChild.elem})... \nNodes remaining: {self._size(node.leftChild.rightChild) - 1}")
                while node.rightChild.leftChild.leftChild is not None:
                    self.leftLeft(node.rightChild)
                    if self._size(node.rightChild.leftChild) - 1 != 0:
                        print("Nodes remaining:", self._size(node.leftChild.rightChild)-1)
                    else:
                        print("Nodes remaining: 0 -> Loop patched!\n")
        newRoot = node.rightChild
        if node.parent is not None and node.parent.leftChild == node:
            node.parent.leftChild = newRoot
        newRoot.parent = node.parent
        if newRoot.leftChild is not None:
            print(f"Found left child on {newRoot.elem} ({newRoot.leftChild.elem}), passing it to the left branch...")
            node.rightChild = newRoot.leftChild
            newRoot.leftChild.parent = node
        else:
            print(f"No left child found on {newRoot.elem}, skipping...")
            node.rightChild = None
        newRoot.leftChild = node
        node.parent = newRoot
        print(f"Right-right rotation done. New root is {newRoot.elem} (Children: {newRoot.leftChild.elem} and {newRoot.rightChild.elem}).")
        return newRoot


    def leftRight(self, node):
        print(f"\nStarting left-right rotation on {node.elem}...")
        newChild = node.leftChild
        newParent = newChild.rightChild
        if newParent.rightChild is not None or newParent.leftChild is not None:
            if newParent.rightChild is not None:
                print(f"{newParent.elem} has a right child, restarting balance from {newChild.elem}...") 
            else:
                print(f"{newParent.elem} has a left child, restarting balance from {newChild.elem}...") 
            self.heightBalance(newChild)
            print(f"Left-right rotation was replaced with a height balance from {newChild.elem}. New left child of {node.elem} is {node.leftChild.elem}.")
        else:
            node.leftChild = newParent
            newParent.parent = node
            newChild.parent = newParent
            newParent.leftChild = newChild
            newChild.rightChild = None
            print(f"Left-right rotation done. New left child of {node.elem} is {node.leftChild.elem}")
        
    
    def rightLeft(self, node):
        print(f"\nStarting right-left rotation on {node.elem}...")
        newChild = node.rightChild
        newParent = newChild.leftChild  
        if newParent.rightChild is not None or newParent.leftChild is not None:
            if newParent.rightChild is not None:
                print(f"{newParent.elem} has a right child, restarting balance from {newChild.elem}...") 
            else:
                print(f"{newParent.elem} has a left child, restarting balance from {newChild.elem}...") 
            self.heightBalance(newChild)
            print(f"Right-left rotation was replaced with a height balance from {newChild.elem}. New right child of {node.elem} is {node.rightChild.elem}.")
        else:
            node.rightChild = newParent
            newParent.parent = node
            newChild.parent = newParent
            newParent.rightChild = newChild
            newChild.leftChild = None
            print(f"Right-left rotation done. New right child of {node.elem} is {node.rightChild.elem}")

    def isHeightBalanced(self, node):
        if abs(self._height(node.leftChild) - self._height(node.rightChild)) < 2:
            return True
        else:
            return False
    
    def heightBalanceTree(self):
        self.heightBalance(self.__root)
        return

    def heightBalance(self, node):
        print("\n\t****** Balancing " + str(node.elem) + " ******\n")
        print(f'Height of {node.elem} is {abs(self._height(node.leftChild) - self._height(node.rightChild))} (balanced if 0 or 1).')
        if self.isHeightBalanced(node):
            print(str(node.elem)+" is height balanced! Moving to sub branches (if any)...")
            if node.leftChild is not None:
                print("Moving to left sub branch containing " + str(node.leftChild.elem))
                self.heightBalance(node.leftChild)
            if node.rightChild is not None:
                print("Moving to right sub branch containing " + str(node.rightChild.elem))    
                self.heightBalance(node.rightChild)  
            else:
                print("\n\t****** HEIGHT BALANCE (ON SOME END NODE) COMPLETED! ******\n")
        else:
            print(str(node.elem)+" is NOT height balanced.", end= " ")
            if self._height(node.leftChild) > self._height(node.rightChild):
                print("Left subtree is taller, balancing...")
                newRoot = self.leftLeft(node)
                self.heightBalance(newRoot) 
            else:
                print("Right subtree is taller, balancing...")
                newRoot = self.rightRight(node)
                self.heightBalance(newRoot) 
            newZone = Zones()
            newZone.__root = newRoot
            return newZone
    # T(n) = O(n)              
    
    def _inorder(self,currentNode):
        string = ''
        if currentNode!=None:
            string+=self._inorder(currentNode.leftChild)
            print('\tZone ' + str(currentNode.elem) +': ', end='')
            string+= 'Zone '+ str(currentNode.elem) +': '
            string+=currentNode.members.printMembers() + '. '
            print()
            string+=self._inorder(currentNode.rightChild)
        return string
    # T(n) = O(n)
    
    def showZones(self):
        print('Zones:')
        string=self._inorder(self.root)
        print()
        return string
    # T(n) = O(n)
    
    def assignsDistributor(self, distributor, zone_iD):
        zone = self.find(zone_iD)
        if zone is None:
            print("That Zone has not been created")
            return
        else:
            zone.members.addCreatedMember(distributor)
    # T(n) = O(n)
    
    def deleteDistributor(self, distributor, zone_iD):
        zone = self.find(zone_iD)
        if zone is None:
            print("That Zone does not exist")
            return
        else:
            zone.members.deleteMember(distributor)
    # T(n) = O(n)
    
    def showDistributors(self,zone_iD):
        zone = self.find(zone_iD)
        print("Distributors for zone "+str(zone_iD)+': ',end='')
        string = zone.members.printMembers()
        return string
    # T(n) = O(n)
    
    
    def findLowestNumTree(self, node):
        if self.__temp is None:
            self.__temp = node
        target = self._findLowestNumTree(node)
        self.__temp = None
        return target
    # T(n) = O(n)
    
    def _findLowestNumTree(self,node):#returns the node with lowest number of members in a tree
        if node is None:
            return
        if self.__temp.members.size > node.members.size:
            self.__temp = node
        self.findLowestNumTree(node.leftChild)
        self.findLowestNumTree(node.rightChild)
        target = self.__temp
        return target
    # T(n) = O(n)
    
    def findLowestNumList(self, liste):
        node = liste.head
        self.__temp = node
        while node is not None:
            if node.element.members.size < self.__temp.element.members.size:
                self.__temp = node
            node = node.next
        target = self.__temp
        self.__temp = None
        return target
    # T(n) = O(n)
    
    def addMemberListTree(self, nodes, liste):
        while liste.size != 0:
            a = self.findLowestNumTree(nodes)
            a.members.addCreatedMember(liste.removeFirst()) # T(n) = 4n² + 13 + 23 + 6
        return
    # T(n) = O(n³)
    
    def addMemberListList(self, nodes, members):
        while members.isEmpty() == False:
            a = self.findLowestNumList(nodes)
            a.element.members.addCreatedMember(members.removeFirst())
        return
    # T(n) = O(n³)
    
    
    def listCreation(self,currentNode): #creates 2 lists containing the previous and next nodes of the zone to be deleted
        if currentNode!=None:
            self.listCreation(currentNode.leftChild)
            if currentNode.elem < self.__temp.elem:
                self.__listTempLow.addLast(currentNode)
            else:
                self.__listTempHigh.addLast(currentNode)
            self.listCreation(currentNode.rightChild)
    # T(n) = O(n)
    
    def deleteZone(self, zone_iD):
        zone = self.find(zone_iD) # T(n) = O(n)
        if zone is None:
            print("Zone does not exist")
            return
        print("Deleting zone "+str(zone_iD)+'. Delivery members will be redistributed.')
        print()
        members = zone.members
        self.__listTempLow = DList()
        self.__listTempHigh = DList()
        self.__temp = zone
        self.remove(zone_iD)
        self.listCreation(self.__root)
        if members.size % 2 != 0: #if there is an odd number of members to be distributed, the odd one out is given to the node with less members in the whole tree
            oddest = DList()
            oddest.addFirst(members.removeFirst())
            treeList = self.__listTempLow
            nodelt = self.__listTempHigh.head
            while nodelt is not None:
                treeList.addLast(nodelt.element)
                nodelt = nodelt.next
            self.addMemberListList(treeList, oddest)   
        members1 = DList()
        members2 = DList()
        for _ in range(members.size//2):
            m = members.removeFirst()
            #print("members 1: "+str(m.name))
            members1.addFirst(m)
        
        for _ in range(members.size):
            m = members.removeFirst()
            #print("members 2: "+str(m.name))
            members2.addFirst(m)

        if self.__listTempLow.isEmpty() == False and self.__listTempHigh.isEmpty() == False:
            self.addMemberListList(self.__listTempLow, members1)
            self.addMemberListList(self.__listTempHigh, members2)
        elif self.__listTempLow.isEmpty() == True and self.__listTempHigh.isEmpty() == False:
            self.addMemberListList(self.__listTempHigh, members1)
            self.addMemberListList(self.__listTempHigh, members2)
        elif self.__listTempLow.isEmpty() == False and self.__listTempHigh.isEmpty() == True:
            self.addMemberListList(self.__listTempLow, members1)
            self.addMemberListList(self.__listTempLow, members2)
        else:
            print("The zones tree is empty now. All workers have been fired.")
        """     
        self.__temp=None
        self.__listTempHigh=None
        self.__listTempLow=None
        """
    # T(n) = O(n). Best: Zone does not exist on the list. Worst: Otherwise

    @property
    def root(self):
        return self.__root
    # T(n) = 1
    
    @property
    def temp(self):
        return self.__temp
    # T(n) = 1

    @property
    def listTempLow(self):
        return self.__listTempLow
    # T(n) = 1
    
    @property
    def listTempHigh(self):
        return self.__listTempHigh
    # T(n) = 1

