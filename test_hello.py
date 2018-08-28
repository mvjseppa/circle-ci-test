import unittest
from hello import hello, numpy_hello

class TestHello(unittest.TestCase):
    def test_hello(self):
        self.assertEqual('hello Mikko', hello('Mikko'))

    def test_numpy_hello(self):
        nph = numpy_hello((3,4))
        self.assertEqual((3,4), nph.shape)
        for i in range(nph.shape[0]):
            for j in range(nph.shape[1]):
                self.assertEqual(0, nph[i][j])

if __name__ == '__main__':
    unittest.main()
