#A function or method that takes in two numbers and returns the result of adding the two numbers.
#A main entry function to call the function pythonor method created in step 1.
#A unit test that, when run, automatically tests the method created in step 1.

def TwoSum(a, b):
        return a + b

print(TwoSum(1, 5)) 


import unittest

class Tests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(TwoSum(-8, -10), -18)

    def test_2(self):
        self.assertEqual(TwoSum(9, 20), 29)
         
    def test_3(self):
        self.assertEqual(TwoSum(8, 800), 808)

if __name__ == '__main__':
    unittest.main()





