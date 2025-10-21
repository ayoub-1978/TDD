import unittest
from exo1 import affiche

class TestFizzBuzz(unittest.TestCase):
    def test_affiche_5(self):
        attendu = "12Fizz4Buzz"
        self.assertEqual(affiche(5), attendu)

    def test_affiche_15(self):
        attendu = "12Fizz4BuzzFizz78FizzBuzz11Fizz1314FrisBee"
        self.assertEqual(affiche(15), attendu)

    def test_affiche_1(self):
        attendu = "1"
        self.assertEqual(affiche(1), attendu)

if __name__ == "__main__":
    unittest.main()
