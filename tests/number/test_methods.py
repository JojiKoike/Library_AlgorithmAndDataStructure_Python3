import unittest
from number.methods import power


class NumberMethodTestCase(unittest.TestCase):

    def test_power_normal(self):
        self.assertEqual(power(5, 8, 1000000007), 390625)


if __name__ == '__main__':
    unittest.main()
