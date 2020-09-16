import unittest
import fibonacci

class TestFibonacciMethods(unittest.TestCase):

    def test_calc(self):
        res = fibonacci.sequence_calc(10)
        self.assertEqual(res, [0, 1, 1, 2, 3, 5, 8, 13, 21, 34])

    
    def test_check_true(self):
        res = fibonacci.check_number(55)[0]
        self.assertTrue(res)

    def test_check_false(self):
        res = fibonacci.check_number(67)[0]
        self.assertFalse(res)

    """
    other corner-case situations (For example, entering wrong expressions into arguments like string, negative integer and flout number) handles with the argparse python library.
    """

if __name__ == '__main__':
    unittest.main()