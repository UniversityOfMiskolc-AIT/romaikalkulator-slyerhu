import unittest 
import roman as r
class TestEncodingString(unittest.TestCase):

    
    def test_converting(self):
        self.assertEqual(r.roman_to_int("V"),5)
        self.assertEqual(r.int_to_roman(6),"VI")


    def test_add(self):
        self.assertEqual(r.add("i","ii"),"III")


    def test_substract(self):
        self.assertEqual(r.subtract("x","i"),"IX")


    def test_multiply(self):
        self.assertEqual(r.multiply("x","ii"),"XX")


    def test_divide(self):
        self.assertEqual(r.divide("xx","iv"),"V")



