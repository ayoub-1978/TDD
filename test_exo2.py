import unittest
from exo2 import crypt

class TestCrypt(unittest.TestCase):

    def test_crypt_simple_pas_1(self):
        # 'abc' + pas 1 -> 'bcd1'
        self.assertEqual(crypt("abc", 1), "bcd1")

    def test_crypt_simple_pas_3(self):
        # 'abc' + pas 3 -> 'def3'
        self.assertEqual(crypt("abc", 3), "def3")

    def test_crypt_wrap(self):
        # 'Z' + pas 1 -> '!' (suivant dans la table complète) + '1'
        self.assertEqual(crypt("Z", 1), "!1")

    def test_crypt_with_space(self):
        # 'a a' + pas 2 selon la table complète -> 'cbc2'
        self.assertEqual(crypt("a a", 2), "cbc2")


if __name__ == "__main__":
    unittest.main()