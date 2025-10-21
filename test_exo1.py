import unittest
from exo1 import affiche

class TestFizzBuzz(unittest.TestCase):
    def test_affiche_5_10(self):
        attendu = "BuzzFizz78FizzBuzz"
        self.assertEqual(affiche(5, 10), attendu)

    def test_affiche_10_16(self):
        attendu = "Buzz11Fizz1314FrisBee16"
        self.assertEqual(affiche(10, 16), attendu)

    def test_affiche_1_5(self):
        attendu = "12Fizz4Buzz"
        self.assertEqual(affiche(1, 5), attendu)

if __name__ == "__main__":
    unittest.main()
