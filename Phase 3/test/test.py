import sys, os
sys.path.append('./src')
from src.Map import Map
import unittest

class MapTest(unittest.TestCase):
    def setUp(self):
        self.map = Map()
    
    def testAddDeliveryPoint(self):
        self.map.addDeliveryPoint("Downing Street", 12, 3)
        assert len(self.map.deliveryZones)>0 and self.map.deliveryZones[1].streetName == "Downing Street"

    def testAddConnection(self):
        self.map.addDeliveryPoint("Downing Street", 12, 3)
        self.map.addDeliveryPoint("The White House", 43, 6)
        self.map.addConnection(1,2, 10) #Zones are given a number by the order they are created
        assert len(self.map.deliveryZones[1].neighbors) > 0 and len(self.map.deliveryZones[2].neighbors) > 0 and self.map.deliveryZones[1].neighbors[0][0] == 2 and self.map.deliveryZones[1].neighbors[0][1] == 10 and self.map.deliveryZones[2].neighbors[0][0] == 1
    
    def testRemoveConnection(self):
        self.map.addDeliveryPoint("Downing Street", 12, 3)
        self.map.addDeliveryPoint("The White House", 43, 6)
        self.map.addConnection(1,2, 10)
        self.map.removeConnection(1,2)
        assert len(self.map.deliveryZones[1].neighbors) == 0 and len(self.map.deliveryZones[2].neighbors) == 0
    
    def testAreConnected(self):
        self.map.addDeliveryPoint("Downing Street", 12, 3)
        self.map.addDeliveryPoint("The White House", 43, 6)
        self.map.addConnection(1,2, 10)
        d = self.map.areConnected(1, 2)
        assert d == 10
    
    def testGenerateRoute(self):
        self.map.addDeliveryPoint("Hello", 3, 47004)
        self.map.addDeliveryPoint("How", 5, 25995)
        self.map.addDeliveryPoint("Are", 6, 12352)
        self.map.addDeliveryPoint("You", 7, 14352)
        self.map.addConnection(1, 2, 5)
        self.map.addConnection(1,3,8)
        self.map.addConnection(4,2,6)
        self.map.addConnection(3,2,6)
        c = self.map.generateRoute()
        l = [1, 2, 4, 3]
        assert c == l
    
    def testMinRoute(self):
        self.map.addDeliveryPoint("Hello", 3, 47004)
        self.map.addDeliveryPoint("How", 5, 25995)
        self.map.addDeliveryPoint("Are", 6, 12352)
        self.map.addDeliveryPoint("You", 7, 14352)
        self.map.addConnection(1, 2, 5)
        self.map.addConnection(1,3,8)
        self.map.addConnection(4,2,6)
        self.map.addConnection(3,2,6)
        c = self.map.minRoute(1, 4)
        l = [1, 2, 4, 11]
        assert c == l


if __name__ == '__main__':
    unittest.main()