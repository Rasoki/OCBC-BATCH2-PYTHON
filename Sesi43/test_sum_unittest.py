import unittest
# from unittest.case import TestCase

class TestSum(unittest.TestCase):

    def tets_sum(self):
        self.assertEqual(sum([1,2,3]),6, "Should be 6")
    
    def tets_sum_tuple(self):
        self.assertEqual(sum([1,2,2]),6, "Should be 6")

if __name__ == "__main__":
    # test_sum()
    # test_sum_tuple()
    unittest.main()
    print("Everything passed")