import unittest
import calc

class TestCalc(unittest.TestCase):

    def test_add(self):
        expected = 3
        result = calc.add(1, 2)
        self.assertEqual(result, expected)

    def test_add_negative(self):
        self.assertEqual(calc.add(-1, 2), 1)
        self.assertEqual(calc.add(-1, -2), -3)

