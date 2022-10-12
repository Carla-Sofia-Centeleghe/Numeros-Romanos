# Decimales test
# Carla S. Centeleghe


import unittest
from decimal import decimal


class test_romano_a_decimal(unittest.TestCase):
    def test_1(self):
        resultado = decimal.romano_a_decimal('II')
        self.assertEqual(resultado, 2)

    def test_4(self):
        resultado = decimal.romano_a_decimal('IV')
        self.assertEqual(resultado, 4)

    def test_8(self):
        resultado = decimal.romano_a_decimal('VIII')
        self.assertEqual(resultado, 8)

    def test_10(self):
        resultado = decimal.romano_a_decimal('X')
        self.assertEqual(resultado, 10)

    def test_12(self):
        resultado = decimal.romano_a_decimal('XII')
        self.assertEqual(resultado, 12)

    def test_20(self):
        resultado = decimal.romano_a_decimal('XX')
        self.assertEqual(resultado, 20)

    def test_25(self):
        resultado = decimal.romano_a_decimal('XXV')
        self.assertEqual(resultado, 25)

    def test_50(self):
        resultado = decimal.romano_a_decimal('L')
        self.assertEqual(resultado, 50)

    def test_53(self):
        resultado = decimal.romano_a_decimal('LIII')
        self.assertEqual(resultado, 53)

    def test_61(self):
        resultado = decimal.romano_a_decimal('LX')
        self.assertEqual(resultado, 60)

    def test_69(self):
        resultado = decimal.romano_a_decimal('LXIX')
        self.assertEqual(resultado, 69)

    def test_100(self):
        resultado = decimal.romano_a_decimal('C')
        self.assertEqual(resultado, 100)

    def test_120(self):
        resultado = decimal.romano_a_decimal('CXX')
        self.assertEqual(resultado, 120)

    def test_155(self):
        resultado = decimal.romano_a_decimal('CLV')
        self.assertEqual(resultado, 155)

    def test_220(self):
        resultado = decimal.romano_a_decimal('CCXX')
        self.assertEqual(resultado, 220)

    def test_300(self):
        resultado = decimal.romano_a_decimal('CCC')
        self.assertEqual(resultado, 300)

    def test_350(self):
        resultado = decimal.romano_a_decimal("CCCL")
        self.assertEqual(resultado, 350)


if __name__ == '__main__':
    unittest.main()
