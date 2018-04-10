import unittest
from danyuanceshi.mathfunc import *
import csv

class TestMathFunc(unittest.TestCase):

    date=None
    @classmethod
    def setUpClass(cls):
        TestMathFunc.date = csv.reader(open('user_list.csv', 'r'))
        print("this is setUpClass()")

    @classmethod
    def tearDownClass(cls):
        print("this is tearDownClass()")

    def setUp(self):

        print("this is setUp()")

    def tearDown(self):
        print("this is  teartDown()")

    def test_add(self):
        for user in TestMathFunc.date:
            #用户名
            print("用户名:",user[0],"密码:",user[1])

        print("this is  test_add()")
        """Test method add(a, b)"""
        self.assertEqual(3, add(1, 2))
        self.assertNotEqual(3, add(2, 2))

    def test_minus(self):
        print("this is  test_minus()")
        """Test method minus(a, b)"""
        self.assertEqual(1, minus(3, 2))

    def test_multi(self):
        print("this is  test_multi()")
        """Test method multi(a, b)"""
        self.assertEqual(6, multi(2, 3))

    # @unittest.skip("I don't want to run this case.")
    def test_divide(self):
        print("this is  test_divide()")
        """Test method divide(a, b)"""
        self.assertEqual(2, divide(6, 3))
        self.assertEqual(2.5, divide(5, 2))

if __name__ == '__main__':
    unittest.main()
