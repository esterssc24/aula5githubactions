
import unittest
from tabuada import tabuada  # Assuming your function is in a file named 'tabuada.py'

class TestTabuada(unittest.TestCase):

    def test_tabuada(self):
        # Test a simple case
        self.assertEqual(tabuada(2, 5), [2, 4, 6, 8, 10])

        # Test with a larger number and a longer range
        self.assertEqual(tabuada(7, 10), [7, 14, 21, 28, 35, 42, 49, 56, 63, 70])

        # Test with a negative number
        self.assertEqual(tabuada(-3, 4), [-3, -6, -9, -12])

if __name__ == "__main__":
    unittest.main()