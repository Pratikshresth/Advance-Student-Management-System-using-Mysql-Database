import unittest
from Queries import *

class Testing(unittest.TestCase):
    Obj=Mainqry()
    def test_new_students(self):   # Test to add
        result=self.Obj.Adding_To_Database("pratik","shrestha","Lalitpur","44700","Bagmati","Male","abcd@gmail.com",
                                           "9860779458","1/26/00","BSc(Hons) Ethical Hacking and Cybersecurity","ES19A","19015")
        self.assertTrue(result)

    def test_new_students1(self):   # Test to add
        result=self.Obj.Adding_To_Database("","","","","","","",
                                           "","","","","")
        self.assertFalse(result)

    def test_search_students(self):
        data=self.Obj.Students_Details()
        result=len(data)
        expected=4
        self.assertEqual(result,expected)

    def test_search_students1(self):
        data=self.Obj.Students_Details()
        result=len(data)
        expected=10
        self.assertNotEqual(result,expected)

    def test_Login(self):
        data=self.Obj.Login("Admin","Admin@12")
        result=len(data)
        expected=1
        self.assertEqual(result,expected)

    def test_Login1(self):
        data=self.Obj.Login("a","admin")
        result=len(data)
        expected=0
        self.assertEqual(result,expected)

    def test_Login2(self):
        data=self.Obj.Login("","")
        self.assertFalse(data)


    def test_section(self):
        data=self.Obj.inst_comp("")
        self.assertFalse(data)

    def test_section1(self):
        data=self.Obj.inst_comp("CS19F")
        self.assertTrue(data)


    def test_fetch(self):
        data=self.Obj.fetch_computing()
        result=len(data)
        expected=4
        self.assertEqual(result,expected)


    def test_fetch1(self):
        data=self.Obj.fetch_computing()
        result=len(data)
        expected=3
        self.assertNotEqual(result,expected)

