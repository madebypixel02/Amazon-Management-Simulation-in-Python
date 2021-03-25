import sys, os
sys.path.append('./src')
import unittest
from src.AmazonManagement import AmazonManagement

class AmazonTestAdditions(unittest.TestCase):
    def setUp(self):
        self.amazon = AmazonManagement()
    
    def testLoadDsMembers(self):
        self.amazon.loadDSMembers(123956, 'Cicueto', 'Colombia', True)
        assert self.amazon.members.head.element.name == 'Cicueto'
    
    def testLoadOrders(self):
        self.amazon.loadOrders(111111111111111, 'The White House', 5)
        assert self.amazon.orders.head.element.address == 'The White House'
    
    def testShowDSMembers(self):
        self.amazon.loadDSMembers(123956, 'Cicueto', 'Colombia', True)
        a = self.amazon.showDSMembers()
        assert a == "Colombia, Cicueto ID:R123956 Status:ACTIVE Zones:  Packages: None"
    
    def testShowOrders(self):
        self.amazon.loadOrders(111111111111111, 'The White House', 5)
        a = self.amazon.showOrders()
        #print(self.amazon.showOrders())
        #self.assertTrue(a.startswith('ID'))
        assert a == "ID: 111-1111111-11111 Zone: 5"
    
    def testAssignDistribution(self):
        self.amazon.loadOrders(111111111111111, 'The White House', 5)
        self.amazon.loadDSMembers(123956, 'Cicueto', 'Colombia', True)
        self.amazon.assignDistribution()
        assert self.amazon.members.head.element.assigned_packages.head.element.address == 'The White House'
    
    def testDeliverPackages(self):
        self.amazon.loadDSMembers(123956, 'Cicueto', 'Colombia', True)
        self.amazon.loadOrders(111111111111111, 'The White House', 5)
        self.amazon.deliverPackages("R123956")
        assert self.amazon.members.head.element.assigned_packages.isEmpty()
        
    
    def testDeliver(self):
        self.amazon.loadOrders(111111111111111, 'The White House', 5)
        self.amazon.loadOrders(111111111111112, 'The White House', 5)
        self.amazon.loadOrders(111111111111113, 'The White House', 5)
        self.amazon.loadDSMembers(123956, 'Cicueto', 'Colombia', True)
        self.amazon.assignDistribution()
        self.amazon.deliver()
        packets = []
        nodelt = self.amazon.delivered.head
        while nodelt!= None: #delivered packages
            packets.append(nodelt)
            nodelt = nodelt.next
        nodelt = self.amazon.incidents.head
        while nodelt!=None: 
            packets.append(nodelt)
            nodelt = nodelt.next
        assert len(packets) == 3
    
    def testRemoveDSMember(self):
        self.amazon.loadDSMembers(123956, 'Cicueto', 'Colombia', True)
        self.amazon.removeDSMembr("R123956")
        assert self.amazon.members.head.element.status == "INACTIVE"
        
        
if __name__ == '__main__':
    unittest.main()
