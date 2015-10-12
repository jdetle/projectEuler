import unittest
import Nprime as prime

class TestPrime(unittest.TestCase):
    def test_nextPrime1(self):
        result = prime.nextPrime([2,3,5,7])
        self.assertEqual(result, 11)
        result = prime.nextPrime([2])
        self.assertEqual(result, 3)

if __name__ == '__main__':
    unittest.main()
