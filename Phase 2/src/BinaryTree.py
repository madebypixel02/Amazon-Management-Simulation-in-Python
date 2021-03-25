import queue
class Node:
    def __init__(self, elem = None):
        self.__elem = elem
        self.__leftChild = None
        self.__rightChild = None
        self.__parent = None
    # T(n) = 4

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
    
    @elem.setter
    def elem(self, value):
        self.__elem = value
    # T(n) = 1
        
    @leftChild.setter
    def leftChild(self,value):
        self.__leftChild = value
        
    @rightChild.setter
    def rightChild(self, value):
        self.__rightChild = value
    # T(n) = 1
    
    @parent.setter
    def parent(self, value):
        self.__parent = value
    # T(n) = 1

class BinaryTree:
    def __init__(self):
        self.__root = None
        self.__size = 0
    # T(n) = 2
    
    def _size(self, currentNode):
        if currentNode == None:
            return 0
        return 1 + self._size(currentNode.leftChild) + self._size(currentNode.rightChild) 
    # T(n) = O(n)
    
    def size(self):
        "Returns the number of nodes"
        return self._size(self.__root)
    # T(n) = O(n)
    
    def _height(self, currentNode):
        if currentNode == None:
            return -1
        return 1 + max(self._height(currentNode.leftChild), self._height(currentNode.rightChild))
    # T(n) = O(n)
    
    def height(self):
        "Returns the height of a tree"
        return self._height(self.__root)
    # T(n) = O(n)
    
    def _depth(self, currentNode):
        if currentNode == None:
            return 0
        return 1 + self._depth(currentNode.parent)
    # T(n) = O(n)
    
    def depth(self):
        "Returns the depth of a node"
        return self._depth(self.__root)
    # T(n) = O(n)
    
    def _preorder(self, currentNode):
        if currentNode != None:
            print(currentNode.elem, end = ' ')
            self._preorder(currentNode.leftChild)
            self._preorder(currentNode.rightChild)
    # T(n) = O(n)
    
    def preorder(self):
        print("Pre-order traversal")
        self._preorder(self.__root)
        print()
    # T(n) = O(n)
    
    def _postorder(self,currentNode):
        if currentNode!=None:
            self._postorder(currentNode.leftChild)
            self._postorder(currentNode.rightChild)
            print(currentNode.elem,end=' ')
    # T(n) = O(n)
    
    def postorder(self):
        print('post-order traversal')
        self._postorder(self.__root)
        print()
    # T(n) = O(n)
    
    def _inorder(self,currentNode):
        if currentNode!=None:
            self._inorder(currentNode.leftChild)
            print(currentNode.elem,end=' ')
            self._inorder(currentNode.rightChild)
    # T(n) = O(n)
    
    def inorder(self):
        self._inorder(self.__root)
        print()
    # T(n) = O(n)

    def levelorder(self):
        if self.__root==None:
            print('tree is empty')
            return
        print('level-order traversal')
        q=queue.Queue()
        q.put(self.__root) #we save the root
        while q.empty()==False:
            current=q.get() #dequeue
            print(current.elem, end=' ')
            if current.leftChild:
                q.put(current.leftChild)
                if current.rightChild:
                    q.put(current.rightChild)
        print()
    # T(n) = O(n)
    
    def search(self, x):
        self.searchNode(self.__root, x)
    # T(n) = O(n)
    
    def searchNode(self, node,x):
        if node is None:
            return False
        
        if node.elem == x:
            return True
        
        if x < node.elem:
            return self.searchNode(node.leftChild, x)
        
        if x > node.elem:
            return self.searchNode(node.rightChild, x)
    # T(n) = O(n). Best: x is starting node. Worst: x is not on the tree or is the last on the tree.
    
    def insert(self, x):
        if self.__root is None:
            self.__root = Node(x)
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
                newNode = Node(x)
                node.leftChild = newNode
                newNode.parent = node
            else:
                self.insertNode(node.leftChild, x)
        else: #if x > node.elem
            if node.rightChild is None:
                newNode = Node(x)
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
                else:
                    node.parent.rightChild = node.leftChild
            else:
                self.__root = node.leftChild
            
        # Second case: only one child (the right child)
        if node.rightChild is not None and node.leftChild is None:
            if node.parent is not None:
                if node.parent.leftChild is node:
                    node.parent.leftChild = node.rightChild
                else:
                    node.parent.rightChild = node.rightChild
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

    def isBalanced(self, node):
        if abs(self._size(node.leftChild) - self._size(node.rightChild)) < 2:
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
            if self._size(node.leftChild) > self._size(node.rightChild):
                print("Thera are more nodes on the left")
                predecessor = node.leftChild
                while predecessor.rightChild is not None:
                    predecessor = predecessor.rightChild
                successor = node.rightChild
                if successor is not None: #there might be no nodes in the right subtree yet
                    while successor.leftChild is not None:
                        successor = successor.leftChild
                newNode= Node(node.elem)
                #newNode.members = node.members
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
                    print("NEW SUBTREE ROOT: "+str(node.elem))
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
                newNode = Node(node.elem)
                #newNode.members = node.members
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
            tree = BinaryTree()
            tree.__root = newRoot
            return tree
    # T(n) = O(n)

    @property
    def root(self):
        return self.__root

    @root.setter
    def root(self, value):
        self.__root = value