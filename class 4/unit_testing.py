


def my_sum(a, b):
    return a + b
    
    
import unittest

class MyTestCase(unittest.TestCase):
    
    def test_sum(self):
        self.assertEqual(my_sum(2,3), 5)
        
    def test_sum_negative_values(self):
        self.assertEqual(my_sum(5, -2), 3)



if __name__ == '__main__':
    unittest.main()