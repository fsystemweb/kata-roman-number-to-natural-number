import unittest
from unittest.mock import patch
import kata


class TestKata(unittest.TestCase):
    @patch('kata.getRomanNumber', return_value='X')
    def test_getRomanNumber(self, input):
        self.assertEqual(kata.getRomanNumber(), 'X')

    def test_validateRomanNumber_returnFalse(self):
        self.assertFalse(kata.validateRomanNumber("t"))
        self.assertFalse(kata.validateRomanNumber(0))
        self.assertFalse(kata.validateRomanNumber("i"))

    def test_validateRomanNumber_returnTrue(self):
        self.assertTrue(kata.validateRomanNumber("I"))
        self.assertTrue(kata.validateRomanNumber("X"))
        self.assertTrue(kata.validateRomanNumber("V"))

    def test_validateIsString_returnTrue(self):
        self.assertTrue(kata.validateIsString("X"))
        self.assertTrue(kata.validateIsString("i"))
        self.assertTrue(kata.validateIsString("o"))

    def test_validateIsString_returnFalse(self):
        self.assertFalse(kata.validateIsString("2"))
        self.assertFalse(kata.validateIsString("0"))
        self.assertFalse(kata.validateIsString("4"))

    def test_runValidation_returnFalse(self):
        self.assertFalse(kata.runValidation("2"))
        self.assertFalse(kata.runValidation("i2f"))
        self.assertFalse(kata.runValidation("II2o"))

    def test_runValidation_returnTrue(self):
        self.assertTrue(kata.runValidation("MV"))
        self.assertTrue(kata.runValidation("LIII"))
        self.assertTrue(kata.runValidation("XCI"))

    def test_romano_a_arabigo(self):
        self.assertEqual(kata.romano_a_arabigo("V"), 5)
        self.assertEqual(kata.romano_a_arabigo("X"), 10)
        self.assertEqual(kata.romano_a_arabigo("III"), 3)
        self.assertEqual(kata.romano_a_arabigo("LI"), 51)
        self.assertEqual(kata.romano_a_arabigo("CX"), 110)
