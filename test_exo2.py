import unittest
from exo2 import crypt, decrypt

class TestCrypt(unittest.TestCase):

    # Tests existants pour crypt
    def test_crypt_simple_pas_1(self):
        self.assertEqual(crypt("abc", 1), "bcd1")

    def test_crypt_simple_pas_3(self):
        self.assertEqual(crypt("abc", 3), "def3")

    def test_crypt_wrap(self):
        self.assertEqual(crypt("Z", 1), "!1")

    def test_crypt_with_space(self):
        self.assertEqual(crypt("a a", 2), "cbc2")

    # Nouveaux tests pour decrypt
    def test_decrypt_simple(self):
        message_crypte = crypt("abc", 1)
        self.assertEqual(decrypt(message_crypte), "abc")

    def test_decrypt_with_pas3(self):
        message_crypte = crypt("hello", 3)
        self.assertEqual(decrypt(message_crypte), "hello")

    def test_decrypt_with_wrap(self):
        message_crypte = crypt("Z", 1)
        self.assertEqual(decrypt(message_crypte), "Z")

    def test_decrypt_with_space(self):
        message_crypte = crypt("a a", 2)
        self.assertEqual(decrypt(message_crypte), "a a")

if __name__ == "__main__":
    unittest.main()
