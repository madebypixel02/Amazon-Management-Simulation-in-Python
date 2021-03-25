import sys, os
sys.path.append('./src')
from src.BinaryTree import BinaryTree

a = BinaryTree()

'''
# Test 1. -> Finally works!
a.insert(5)
a.insert(1)
a.insert(7)
a.insert(3)
a.insert(2)
a.insert(4)
'''

'''
# Test 2. No need to balance. -> Works!
a.insert(5)
a.insert(2)
a.insert(6)
'''

'''
# Test 3. Only left-left rotation needed. -> Works!
a.insert(3)
a.insert(2)
a.insert(1)
'''

'''
# Test 4. Left-left with sub branch on new root. -> Works!
a.insert(4)
a.insert(2)
a.insert(3)
a.insert(1)
'''

'''
# Test 5. Left-right simple. -> Works!
a.insert(4)
a.insert(2)
a.insert(3)
'''

'''
# Test 6. Complex (Zig Zag effect on left tree). -> Works!
a.insert(4)
a.insert(1)
a.insert(3)
a.insert(2)
'''

'''
# Test 7. Complex (multiple Zig Zag effects on right tree). -> Works!
a.insert(1)
a.insert(5)
a.insert(2)
a.insert(4)
a.insert(3)
'''


# Test 8. When root is balanced but sub branches arent't. -> Works!
a.insert(3)
a.insert(4)
a.insert(5)
a.insert(2)
a.insert(1)
a.insert(6)
a.insert(0)


"""
# Test 9. "<" shaped tree. -> Works!
a.insert(10)
a.insert(9)
a.insert(8)
a.insert(1)
a.insert(2)
a.insert(3)
a.insert(4)
a.insert(5)
"""

'''
# Test 10. Random online tree. -> Works!
a.insert(50)
a.insert(17)
a.insert(76)
a.insert(9)
a.insert(23)
a.insert(54)
a.insert(14)
a.insert(19)
a.insert(72)
a.insert(12)
a.insert(67)
'''


print("\nINORDER:", end= " ")
a.inorder()
b = a.heightBalance(a.root)
