# def sum(nums):
#     result = 0
#     for n in nums:
#         result += n
#     return result
#     # return 0

# # sum_3 = sum[1,2,3]
# print(sum([1,2,3]))
# assert sum([1, 2, 3]) == 6, "Should be 6"

# import unittest
# from unittest.case import TestCase

# class TestSum(unittest.TestCase):

#     def tets_sum(self):
#         self.assertEqual(sum([1,2,3]),6, "Should be 6")
    
#     def tets_sum_tuple(self):
#         self.assertEqual(sum([1,2,2]),6, "Should be 6")

# if __name__ == "__main__":
#     # test_sum()
#     # test_sum_tuple()
#     unittest.main()
#     print("Everything passed")

def test_sum():
    assert sum([1, 2, 3]) == 6, "Should be 6"
 
def test_sum_tuple():
    assert sum((1, 2, 2)) == 6, "Should be 6"

