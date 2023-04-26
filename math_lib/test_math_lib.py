from math_lib import pover, root

import unittest

class MathLibTestCase(unittest.TestCase):
    def testPover(self): 
        self.assertEqual(pover(0, 2), 0)
        self.assertEqual(pover(2, 0), 1)
        self.assertEqual(pover(-2, 0), 1)
        self.assertEqual(pover(2, -2), 0.25)

    def testRoot(self):
        self.assertEqual(root(10, 1), 10)
        self.assertEqual(root(10, 2), 3.1622776601683795)


if __name__ == '__main__':
    unittest.main()
    
# # Unit testing
# if __name__ == "__main__":  
#     # assert ( expression ) , (AssertionErrorText)
    
#     assert pover(0, 2) == 0, f"{pover(0, 2)}"
#     print("pover(0, 2) == 0 ...successfully")
    
#     assert pover(2, 0) == 1, f"{pover(2, 0)}"
#     print("pover(2, 0) == 1 ...successfully")
    
#     assert pover(-2, 0) == 1, f"{pover(-2, 0)}"
#     print("pover(-2, 0) == 1 ...successfully")
    
#     assert pover(2, -2) == 0.25, f"{pover(2, -2)}"
#     print("pover(2, -2) == 0.25 ...successfully")
    
#     assert root(10, 1) == 10 , f"{root(10, 1)}"   
#     print("root(10, 1) == 10 ...successfully")
    
#     assert root(10, 2) == 3.1622776601683795, f"{root(10, 2)}"   
#     print("root(10, 2) == 3.1622776601683795  ...successfully")
    
#     print("Unit tests completed")