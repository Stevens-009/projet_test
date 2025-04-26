import unittest
from encryption_utilities import passwordEncrypt, passwordDecrypt

class TestEncryptionMethods(unittest.TestCase):

    def test_encrypt_password(self):
        unencryptedPassword = "XqffoZeo"
        expectedEncryptedPassword = "NgvvePue"
        encryptedPassword = passwordEncrypt(unencryptedPassword, 16)
        self.assertEqual(encryptedPassword, expectedEncryptedPassword)

    def test_decrypt_password(self):
        encryptedPassword = "NgvvePue"
        expectedDecryptedPassword = "XqffoZeo"
        decryptedPassword = passwordDecrypt(encryptedPassword, 16)
        self.assertEqual(decryptedPassword, expectedDecryptedPassword)

if __name__ == '__main__':
    unittest.main()
