import unittest
from exo2 import crypt

class TestCrypt(unittest.TestCase):
    def test_crypt_simple(self):
        # "abc" devient "bcd"
        self.assertEqual(crypt("abc"), "bcd")

    def test_crypt_with_wrap(self):
        # selon la table complète (ascii_letters + punctuation + digits + " "),
        # le caractère suivant de 'Z' est '!' (pas 'a')
        self.assertEqual(crypt("Z"), "!")

    def test_crypt_with_space(self):
        # l'espace est dans la table, donc il se déplace aussi
        result = crypt("a a")
        self.assertEqual(len(result), 3)

if __name__ == "__main__":
    unittest.main()
