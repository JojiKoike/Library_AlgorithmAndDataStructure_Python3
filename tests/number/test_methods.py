import unittest
from number.methods import power, is_prime, gcd


class NumberMethodTestCase(unittest.TestCase):

    def test_power_normal(self):
        self.assertEqual(power(5, 8, 1000000007), 390625)

    def test_is_prime_normal(self):
        # 0, 1
        self.assertEqual(False, is_prime(0))
        self.assertEqual(False, is_prime(1))
        # even
        self.assertEqual(False, is_prime(2))
        # not prime
        self.assertEqual(False, is_prime(9))
        # prime
        self.assertEqual(True, is_prime(3))

    def test_gcd_normal(self):
        self.assertEqual(21, gcd(147, 105))


if __name__ == '__main__':
    unittest.main()
