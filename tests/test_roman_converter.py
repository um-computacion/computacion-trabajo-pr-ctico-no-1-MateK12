
import unittest

class Test_roman_converter(unittest.TestCase):
    def test_1(self):
        self.assertEqual(romanConverter(1),'I')
    def test_2(self):
        self.assertEqual(romanConverter(2),'II')
    def test_3(self):
        self.assertEqual(romanConverter(3),'III')
    def test_4(self):
        self.assertEqual(romanConverter(4),'IV')
    def test_5(self):
        self.assertEqual(romanConverter(5),'V')
    def test_6(self):
        self.assertEqual(romanConverter(6),'VI')
    def test_7(self):
        self.assertEqual(romanConverter(7),'VII')
    def test_8(self):
        self.assertEqual(romanConverter(8),'VIII')
    def test_9(self):
        self.assertEqual(romanConverter(9),'VIV')
    def test_10(self):
        self.assertEqual(romanConverter(10),'X')
    def test_23(self):
        self.assertEqual(romanConverter(23),'XXIII')
    def test_24(self):
        self.assertEqual(romanConverter(24),'XXIV')
    def test_27(self):
        self.assertEqual(romanConverter(27),'XXVII')
    def test_50(self):
        self.assertEqual(romanConverter(50),'L')
    def test_53(self):
        self.assertEqual(romanConverter(53),'LIII')
    def test_54(self):
        self.assertEqual(romanConverter(54),'LIV')
    def test_56(self):
        self.assertEqual(romanConverter(56),'LVI')
    def test_100(self):
        self.assertEqual(romanConverter(100),'C')
    def test_101(self):
        self.assertEqual(romanConverter(101),'CI')
    def test_104(self):
        self.assertEqual(romanConverter(104),'CIV')
    def test_105(self):
        self.assertEqual(romanConverter(105),'CV')
    def test_500(self):
        self.assertEqual(romanConverter(500),'D')
    def test_501(self):
        self.assertEqual(romanConverter(501),'DI')
    def test_504(self):
        self.assertEqual(romanConverter(504),'DIV')
    def test_508(self):
        self.assertEqual(romanConverter(508),'DVIII')
    def test_1000(self):
        self.assertEqual(romanConverter(1000),'M')
    def test_1002(self):
        self.assertEqual(romanConverter(1002),'MII')
    def test_1004(self):
        self.assertEqual(romanConverter(1004),'MIV')
    def test_1009(self):
        self.assertEqual(romanConverter(1009),'MVIV')
    def test_2025(self):
        self.assertEqual(romanConverter(2025),'MMXXV')

if __name__ == "__main__":
    unittest.main()