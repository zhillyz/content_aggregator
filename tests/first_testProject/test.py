import unittest

from my_sum import Sum
from fractions import Fraction

class TestSum(unittest.TestCase):
    def test_list_fraction(self):
        """Test that is can sum a list of fractions."""
        data = [Fraction(1,4), Fraction(1,4), Fraction(2,5)]
        result = Sum(data)
        self.assertEqual(result,Fraction(9,10))

    def test_list_int(self):
        """ Test that it can sum a list of integers."""
        data = [1,2,3]
        result = Sum(data)
        self.assertEqual(result,6)

    def test_bad_type(self):
        data = "banana"
        with self.assertRaises(TypeError):
            result = Sum(data)



if __name__ == '__main__':
    unittest.main()