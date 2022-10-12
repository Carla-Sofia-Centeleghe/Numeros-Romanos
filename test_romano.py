# test para romano
# Carla S. Centeleghe

import unittest
import numeroromanos


class TestRomanToNumber(unittest.TestCase):

    def test_1(self):
        roman = numeroromanos.Roman(1)
        self.assertEqual(roman, "I")

    def test_4(self):
        roman = numeroromanos.Roman(4)
        self.assertEqual(roman, "IV")

    def test_5(self):
        roman = numeroromanos.Roman(5)
        self.assertEqual(roman, "V")

    def test_9(self):
        roman = numeroromanos.Roman(9)
        self.assertEqual(roman, "IX")

    def test_10(self):
        roman = numeroromanos.Roman(10)
        self.assertEqual(roman, "X")

    def test_40(self):
        roman = numeroromanos.Roman(40)
        self.assertEqual(roman, "XL")

    def test_50(self):
        roman = numeroromanos.Roman(50)
        self.assertEqual(roman, "L")

    def test_100(self):
        roman = numeroromanos.Roman(100)
        self.assertEqual(roman, "C")

    def test_500(self):
        roman = numeroromanos.Roman(500)
        self.assertEqual(roman, "D")

    def test_900(self):
        roman = numeroromanos.Roman(900)
        self.assertEqual(roman, "CM")

    def test_1000(self):
        roman = numeroromanos.Roman(1000)
        self.assertEqual(roman, "M")

    def test_1549(self):
        roman = numeroromanos.Roman(1549)
        self.assertEqual(roman, "MDXLIX")

    def test_3999(self):
        roman = numeroromanos.Roman(3999)
        self.assertEqual(roman, "MMMCMXCIX")


if __name__ == '__main__':
    unittest.main()
