
import unittest
from src.roman_converter import roman_converter
class Test_roman_converter(unittest.TestCase):
    def test_1(self):
        self.assertEqual(roman_converter(1),'I')
    def test_2(self):
        self.assertEqual(roman_converter(2),'II')
    def test_3(self):
        self.assertEqual(roman_converter(3),'III')
    def test_4(self):
        self.assertEqual(roman_converter(4),'IV')
    def test_5(self):
        self.assertEqual(roman_converter(5),'V')
    def test_6(self):
        self.assertEqual(roman_converter(6),'VI')
    def test_7(self):
        self.assertEqual(roman_converter(7),'VII')
    def test_8(self):
        self.assertEqual(roman_converter(8),'VIII')
    def test_9(self):
        self.assertEqual(roman_converter(9),'IX')
    def test_10(self):
        self.assertEqual(roman_converter(10),'X')
    def test_23(self):
        self.assertEqual(roman_converter(23),'XXIII')
    def test_24(self):
        self.assertEqual(roman_converter(24),'XXIV')
    def test_27(self):
        self.assertEqual(roman_converter(27),'XXVII')
    def test_50(self):
        self.assertEqual(roman_converter(50),'L')
    def test_53(self):
        self.assertEqual(roman_converter(53),'LIII')
    def test_54(self):
        self.assertEqual(roman_converter(54),'LIV')
    def test_56(self):
        self.assertEqual(roman_converter(56),'LVI')
    def test_100(self):
        self.assertEqual(roman_converter(100),'C')
    def test_101(self):
        self.assertEqual(roman_converter(101),'CI')
    def test_104(self):
        self.assertEqual(roman_converter(104),'CIV')
    def test_105(self):
        self.assertEqual(roman_converter(105),'CV')
    def test_500(self):
        self.assertEqual(roman_converter(500),'D')
    def test_501(self):
        self.assertEqual(roman_converter(501),'DI')
    def test_504(self):
        self.assertEqual(roman_converter(504),'DIV')
    def test_508(self):
        self.assertEqual(roman_converter(508),'DVIII')
    def test_1000(self):
        self.assertEqual(roman_converter(1000),'M')
    def test_1002(self):
        self.assertEqual(roman_converter(1002),'MII')
    def test_1004(self):
        self.assertEqual(roman_converter(1004),'MIV')
    def test_1009(self):
        self.assertEqual(roman_converter(1009),'MIX')
    def test_2025(self):
        self.assertEqual(roman_converter(2025),'MMXXV')
    def test_3999(self):
        self.assertEqual(roman_converter(3999),"MMMCMXCIX")
    def test_999(self):
        self.assertEqual(roman_converter(999),"CMXCIX")
    def test_499(self):
        self.assertEqual(roman_converter(499),"CDXCIX")
    def test_40(self):
        self.assertEqual(roman_converter(40),"XL")
    def test_90(self):
        self.assertEqual(roman_converter(90),"XC")
    def test_350(self):
        self.assertEqual(roman_converter(90),"XC")


if __name__ == "__roman_converter__":
    unittest.roman_converter()