import MD5Hashing
import unittest

class MD5Tests(unittest.TestCase):
    def setUp(self):
        pass

    def test_MD5ExampleInput(self):
        secret = 'abcdef'
        result = MD5Hashing.HashSecret(secret, '00000')
        self.assertEqual('609043', result)

    def test_SecondMD5ExampleInput(self):
        secret = 'pqrstuv'
        result = MD5Hashing.HashSecret(secret, '00000')
        self.assertEqual('1048970', result)