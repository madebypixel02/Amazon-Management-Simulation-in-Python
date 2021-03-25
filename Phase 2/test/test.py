import sys, os
sys.path.append('./src')
from src.DSMember import DSMember
from src.Zones import Zones
import unittest



class ZoneTest(unittest.TestCase):
    def setUp(self):
        self.zones = Zones()
    
    def testCreateZone(self):
        self.zones.createZone(1)
        self.zones.createZone(2)
        assert self.zones.root.elem == 1 and self.zones.root.rightChild.elem == 2
    
    def testShowZones(self):
        self.zones.createZone(1)
        self.zones.createZone(2)
        c= DSMember(123956, 'Cicueto', 'Colombia', True)
        self.zones.assignsDistributor(c,1)
        s = self.zones.showZones()
        assert s=="Zone 1: Cicueto Colombia. Zone 2: . "
    
    def testSizeBalance(self):
        self.zones.createZone(1)
        self.zones.createZone(2)
        """At this point the tree has 1 as root and 2 as the root's rightchild"""
        self.zones.createZone(3)
        """Since Size Balance is executed right after creating a new Zone, now the tree should
        have 2 as root and 1 and 3 as its left and right child respectively."""
        assert self.zones.root.elem == 2 and self.zones.root.rightChild.elem == 3 and self.zones.root.leftChild.elem == 1
    
    def testHeightBalance(self):
        a = Zones()
        nodes = [5,1,4,2,3]
        for i in nodes: # since createZone() uses size balancing, this test uses insert() instead.
            a.insert(i)
        b = a.heightBalance(a.root)
        assert b.root.elem == 3 and b.root.leftChild.elem == 1 and b.root.rightChild.elem == 5 and b.root.leftChild.rightChild.elem == 2 and b.root.rightChild.leftChild.elem == 4

    
    def testFind(self):
        self.zones.createZone(1)
        self.zones.createZone(2)
        a = self.zones.find(2)
        assert a.elem == 2
    
    def testDeleteZone(self):
        self.zones.createZone(1)
        self.zones.createZone(2)
        self.zones.createZone(3)
        c= DSMember(123956, 'Cicueto', 'Colombia', True)
        d= DSMember(123957, 'Zarina', 'Zuzumba', True)
        self.zones.assignsDistributor(c,2)
        self.zones.assignsDistributor(d,2)
        self.zones.deleteZone(2)
        a = self.zones.root.members.size
        b = self.zones.root.leftChild.members.size
        assert a == 1 and b == 1 and self.zones.find(2) == None
    
    def testShowDistributors(self):
        self.zones.createZone(1)
        self.zones.createZone(2)
        c= DSMember(123956, 'Cicueto', 'Colombia', True)
        d= DSMember(123957, 'Zarina', 'Zuzumba', True)
        self.zones.assignsDistributor(c,1)
        self.zones.assignsDistributor(d,1)
        s = self.zones.showDistributors(1)
        assert s == "Cicueto Colombia, Zarina Zuzumba"
        
    
    def testAssignDistributor(self):
        self.zones.createZone(1)
        c= DSMember(123956, 'Cicueto', 'Colombia', True)
        a = self.zones.root.members.isEmpty()
        self.zones.assignsDistributor(c,1)
        b = self.zones.root.members.isEmpty()
        assert a == True and b == False
    
    def testDeleteDistributor(self):
        self.zones.createZone(1)
        c= DSMember(123956, 'Cicueto', 'Colombia', True)
        self.zones.assignsDistributor(c,1)
        a = self.zones.root.members.isEmpty()
        self.zones.deleteDistributor(c,1)
        b = self.zones.root.members.isEmpty()
        assert a == False and b == True
    
a = Zones()
a.createZone(1)
a.createZone(2)
a.insert(3)
c= DSMember(123956, 'Cicueto', 'Colombia', True)
d= DSMember(123957, 'Zarina', 'Zuzumba', True)
a.assignsDistributor(c,1)
a.assignsDistributor(d,1)
b = a.showDistributors(1)
print(b)
if __name__ == '__main__':
    unittest.main()
