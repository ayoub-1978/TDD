import unittest
from exo2 import crypt

class TestCrypt(unittest.TestCase):
    def test_crypt_simple(self):
        self.assertEqual(crypt("abc"), "bcd")

    def test_crypt_with_wrap(self):
        # Exemple : 'Z' devient 'a'
        self.assertEqual(crypt("Z"), "a")

    def test_crypt_with_space(self):
        result = crypt("a a")
        self.assertEqual(len(result), 3)

if __name__ == "__main__":
    unittest.main()
