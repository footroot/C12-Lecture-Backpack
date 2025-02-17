import unittest


def add(num1, num2):
    return num1 + num2


class TestAdd(unittest.TestCase):
    
    def test_basic_addition(self):
        self.assertEqual(add(2,3), 5)
    
    def test_basic_addition_with_neagtive(self):
        self.assertEqual(add(-1, 1), 0)

    def test_basic_addition_with_zeros(self):
        self.assertEqual(add(0, 0), 0)

if __name__ == "__main__":
    unittest.main()