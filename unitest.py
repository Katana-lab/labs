import unittest
from lab1 import monoton

class TestMonotonicArray(unittest.TestCase):
    def test_increasing(self):
        self.assertTrue(monoton([1, 2, 3, 4, 5]))
    
    def test_decreasing(self):
        self.assertTrue(monoton([5, 4, 3, 2, 1]))
    
    def test_not_monotonic(self):
        self.assertFalse(monoton([1, 2, 2, 3, 2, 4]))
    
    def test_equal_elements(self):
        self.assertTrue(monoton([3, 3, 3, 3]))
    
    def test_single_element(self):
        self.assertTrue(monoton([7]))
    
    def test_empty_list(self):
        self.assertTrue(monoton([]))

if __name__ == "__main__":
    unittest.main()
