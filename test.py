import unittest
from convert import *


class PyxerterTest(object):

    def setUp(self):
        # no juncina
        pass

    def test_cambio_base(self):
        esperado = 111
        actual = cambio_base(numerito, base)
        # para que haga el PyxerterTest
        self.assertEqual(actual, esperado)


def tearDown(self):
    pass


if __name__ == '__main__':
    unittest.main()
