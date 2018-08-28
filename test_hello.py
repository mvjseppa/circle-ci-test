import unittest
from hello import hello

class TestHello(unittest.TestCase):
    def test_hello(self):
        self.assertEqual('hello Mikko', hello('Mikko'))

if __name__ == '__main__':
    unittest.main()
