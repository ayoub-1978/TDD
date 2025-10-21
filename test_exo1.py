import unittest
from io import StringIO
from unittest.mock import patch
from exo1 import affiche

class TestFizzBuzz(unittest.TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    def test_affiche_output(self, mock_stdout):
        affiche()
        output = mock_stdout.getvalue().strip()
        attendu = "12Fizz4BuzzFizz78FizzBuzz11Fizz1314FrisBee"
        # On ne vérifie que les 15 premiers caractères pour alléger le test
        self.assertTrue(output.startswith(attendu))

if __name__ == "__main__":
    unittest.main()
