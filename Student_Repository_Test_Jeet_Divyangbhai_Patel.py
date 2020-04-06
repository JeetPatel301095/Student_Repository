"""Test File for Homework 09"""

import unittest
from HW09_Jeet_Divyangbhai_Patel import University,Student,Instructor

class HW09Test(unittest.TestCase):
    """Test Class for HW-09"""
    def test_studict(self) -> None:
        """Test class to test the Student Dictionary for Stevens"""
        path="C:/Users/Jeet/Jeet/SW-810/HW09JeetDivyangbhaiPatel/TextFiles/"
        try:
            a:University = University(path,"Stevens Institute of Technology")
        except FileNotFoundError as e:
            print(e)
        except ValueError as e:
            print(e)
        s1: Student = Student("10103","Baldwin, C","SFEN")
        s2: Student = Student("10115","Wyatt, X","SFEN")
        s3: Student = Student("10172","Forbes, I","SFEN")
        s4: Student = Student("10175","Erickson, D","SFEN")
        s5: Student = Student("10183","Chapman, O","SFEN")
        s6: Student = Student("11399","Cordova, I","SYEN")
        s7: Student = Student("11461","Wright, U","SYEN")
        s8: Student = Student("11658","Kelly, P","SYEN")
        s9: Student = Student("11714","Morton, A","SYEN")
        s10: Student = Student("11788","Fuller, E","SYEN")
        s1.courses["CS 501"] =  "B"
        s1.courses["SSW 564"] = "A-"
        s1.courses["SSW 567"] = "A"
        s1.courses["SSW 687"] = "B"
        s2.courses["CS 545"] = "A"
        s2.courses["SSW 564"] = "B+"
        s2.courses["SSW 567"] = "A"
        s2.courses["SSW 687"] = "A"
        s3.courses["SSW 555"] = "A"
        s3.courses["SSW 567"] = "A-"
        s4.courses["SSW 564"] = "A"
        s4.courses["SSW 567"] = "A"
        s4.courses["SSW 687"] = "B-"
        s5.courses["SSW 689"] = "A"
        s6.courses["SSW 540"] = "B"
        s7.courses["SYS 611"] = "A"
        s7.courses["SYS 750"] = "A-"
        s7.courses["SYS 800"] = "A"
        s8.courses["SSW 540"] = "F"
        s9.courses["SYS 611"] = "A"
        s9.courses["SYS 645"] = "C"
        s10.courses["SSW 540"] = "A"
        expected:Dict[str,Student]={
            '10103': s1,
            '10115': s2,
            '10172': s3,
            '10175': s4,
            '10183': s5,
            '11399': s6,
            '11461': s7,
            '11658': s8,
            '11714': s9,
            '11788': s10,
        }
        self.assertEqual(a.studict["10103"].cwid,expected["10103"].cwid)
        self.assertEqual(a.studict["10103"].name,expected["10103"].name)
        self.assertEqual(a.studict["10103"].major,expected["10103"].major)
        self.assertEqual(a.studict["10103"].courses.keys(),expected["10103"].courses.keys())

        self.assertEqual(a.studict["10115"].cwid,expected["10115"].cwid)
        self.assertEqual(a.studict["10115"].name,expected["10115"].name)
        self.assertEqual(a.studict["10115"].major,expected["10115"].major)
        self.assertEqual(a.studict["10115"].courses.keys(),expected["10115"].courses.keys())

        self.assertEqual(a.studict["10172"].cwid,expected["10172"].cwid)
        self.assertEqual(a.studict["10172"].name,expected["10172"].name)
        self.assertEqual(a.studict["10172"].major,expected["10172"].major)
        self.assertEqual(a.studict["10172"].courses.keys(),expected["10172"].courses.keys())

        self.assertEqual(a.studict["10175"].cwid,expected["10175"].cwid)
        self.assertEqual(a.studict["10175"].name,expected["10175"].name)
        self.assertEqual(a.studict["10175"].major,expected["10175"].major)
        self.assertEqual(a.studict["10175"].courses.keys(),expected["10175"].courses.keys())

        self.assertEqual(a.studict["10183"].cwid,expected["10183"].cwid)
        self.assertEqual(a.studict["10183"].name,expected["10183"].name)
        self.assertEqual(a.studict["10183"].major,expected["10183"].major)
        self.assertEqual(a.studict["10183"].courses.keys(),expected["10183"].courses.keys())

        self.assertEqual(a.studict["11399"].cwid,expected["11399"].cwid)
        self.assertEqual(a.studict["11399"].name,expected["11399"].name)
        self.assertEqual(a.studict["11399"].major,expected["11399"].major)
        self.assertEqual(a.studict["11399"].courses.keys(),expected["11399"].courses.keys())

        self.assertEqual(a.studict["11461"].cwid,expected["11461"].cwid)
        self.assertEqual(a.studict["11461"].name,expected["11461"].name)
        self.assertEqual(a.studict["11461"].major,expected["11461"].major)
        self.assertEqual(a.studict["11461"].courses.keys(),expected["11461"].courses.keys())

        self.assertEqual(a.studict["11658"].cwid,expected["11658"].cwid)
        self.assertEqual(a.studict["11658"].name,expected["11658"].name)
        self.assertEqual(a.studict["11658"].major,expected["11658"].major)
        self.assertEqual(a.studict["11658"].courses.keys(),expected["11658"].courses.keys())

        self.assertEqual(a.studict["11714"].cwid,expected["11714"].cwid)
        self.assertEqual(a.studict["11714"].name,expected["11714"].name)
        self.assertEqual(a.studict["11714"].major,expected["11714"].major)
        self.assertEqual(a.studict["11714"].courses.keys(),expected["11714"].courses.keys())

        self.assertEqual(a.studict["11788"].cwid,expected["11788"].cwid)
        self.assertEqual(a.studict["11788"].name,expected["11788"].name)
        self.assertEqual(a.studict["11788"].major,expected["11788"].major)
        self.assertEqual(a.studict["11788"].courses.keys(),expected["11788"].courses.keys())

    def test_instdict(self) -> None:
        """Test class to test the Instructor Dictionary for Stevens"""
        path="C:/Users/Jeet/Jeet/SW-810/HW09JeetDivyangbhaiPatel/TextFiles/"
        try:
            a:University = University(path,"Stevens Institute of Technology")
        except FileNotFoundError as e:
            print(e)
        except ValueError as e:
            print(e)
        i1 : Instructor = Instructor("98765","Einstein, A","SFEN")
        i2 : Instructor = Instructor("98764","Feynman, R","SFEN")
        i3 : Instructor = Instructor("98763","Newton, I","SFEN")
        i4 : Instructor = Instructor("98762","Hawking, S","SYEN")
        i5 : Instructor = Instructor("98761","Edison, A","SYEN")
        i6 : Instructor = Instructor("98760","Darwin, C","SYEN")

        i1.courses["SSW 567"] = 4
        i1.courses["SSW 540"] = 3
        i2.courses["SSW 687"] = 3
        i2.courses["SSW 564"] = 3
        i2.courses["CS 501"] = 1
        i2.courses["CS 545"] = 1
        i3.courses["SSW 555"] = 1
        i3.courses["SSW 689"] = 1
        i6.courses["SYS 750"] = 1
        i6.courses["SYS 800"] = 1
        i6.courses["SYS 611"] = 2
        i6.courses["SYS 645"] = 1

        expected: Dict[str,Instructor] ={
            "98765": i1,
            "98764": i2,
            "98763": i3,
            "98762": i4,
            "98761": i5,
            "98760": i6,
        }

        self.assertEqual(a.instdict["98765"].cwid,expected["98765"].cwid)
        self.assertEqual(a.instdict["98765"].name,expected["98765"].name)
        self.assertEqual(a.instdict["98765"].department,expected["98765"].department)
        self.assertEqual(a.instdict["98765"].courses.keys(),expected["98765"].courses.keys())

        self.assertEqual(a.instdict["98764"].cwid,expected["98764"].cwid)
        self.assertEqual(a.instdict["98764"].name,expected["98764"].name)
        self.assertEqual(a.instdict["98764"].department,expected["98764"].department)
        self.assertEqual(a.instdict["98764"].courses.keys(),expected["98764"].courses.keys())
        
        self.assertEqual(a.instdict["98763"].cwid,expected["98763"].cwid)
        self.assertEqual(a.instdict["98763"].name,expected["98763"].name)
        self.assertEqual(a.instdict["98763"].department,expected["98763"].department)
        self.assertEqual(a.instdict["98763"].courses.keys(),expected["98763"].courses.keys())

        self.assertEqual(a.instdict["98762"].cwid,expected["98762"].cwid)
        self.assertEqual(a.instdict["98762"].name,expected["98762"].name)
        self.assertEqual(a.instdict["98762"].department,expected["98762"].department)
        self.assertEqual(a.instdict["98762"].courses.keys(),expected["98762"].courses.keys())

        self.assertEqual(a.instdict["98761"].cwid,expected["98761"].cwid)
        self.assertEqual(a.instdict["98761"].name,expected["98761"].name)
        self.assertEqual(a.instdict["98761"].department,expected["98761"].department)
        self.assertEqual(a.instdict["98761"].courses.keys(),expected["98761"].courses.keys())

        self.assertEqual(a.instdict["98760"].cwid,expected["98760"].cwid)
        self.assertEqual(a.instdict["98760"].name,expected["98760"].name)
        self.assertEqual(a.instdict["98760"].department,expected["98760"].department)
        self.assertEqual(a.instdict["98760"].courses.keys(),expected["98760"].courses.keys())

    def test_filenotfounderror(self) -> None:
        """Test class to test the FileNotFoundError"""
        path:str = "C:/Users/Jeet/Jeet/SW-810/HW08JeetDivyangbhaiPatel/"
        with self.assertRaises(FileNotFoundError):
            result3 = University(path,"Stevens")

    def test_valueerror(self) -> None:
        """Test class to test the ValueError"""
        path:str = "C:/Users/Jeet/Jeet/SW-810/HW09JeetDivyangbhaiPatel/TextFiles2/"
        with self.assertRaises(ValueError):
            result3 = University(path,"Stevens")
        
    def test_different_unis(self) -> None:
        """Test class to test the Student Dictionary for NYU just by sending different path"""
        path="C:/Users/Jeet/Jeet/SW-810/HW09JeetDivyangbhaiPatel/NYUFiles/"
        try:
            a:University = University(path,"NYU")
        except FileNotFoundError as e:
            print(e)
        except ValueError as e:
            print(e)
        s1: Student = Student("10103","Baldwin, C","SFEN")
        s2: Student = Student("10115","Wyatt, X","SFEN")
        s3: Student = Student("10172","Forbes, I","SFEN")
        s4: Student = Student("10175","Erickson, D","SFEN")
        s5: Student = Student("10183","Chapman, O","SFEN")
        s6: Student = Student("11399","Cordova, I","SYEN")
        s7: Student = Student("11461","Wright, U","SYEN")
        s8: Student = Student("11658","Kelly, P","SYEN")
        s9: Student = Student("11714","Morton, A","SYEN")
        s10: Student = Student("11788","Fuller, E","SYEN")
        s1.courses["CS 501"] =  "B"
        s1.courses["SSW 564"] = "A-"
        s1.courses["SSW 567"] = "A"
        s1.courses["SSW 687"] = "B"
        s2.courses["CS 545"] = "A"
        s2.courses["SSW 564"] = "B+"
        s2.courses["SSW 567"] = "A"
        s2.courses["SSW 687"] = "A"
        s3.courses["SSW 555"] = "A"
        s3.courses["SSW 567"] = "A-"
        s4.courses["SSW 564"] = "A"
        s4.courses["SSW 567"] = "A"
        s4.courses["SSW 687"] = "B-"
        s5.courses["SSW 689"] = "A"
        s6.courses["SSW 540"] = "B"
        s7.courses["SYS 611"] = "A"
        s7.courses["SYS 750"] = "A-"
        s7.courses["SYS 800"] = "A"
        s8.courses["SSW 540"] = "F"
        s9.courses["SYS 611"] = "A"
        s9.courses["SYS 645"] = "C"
        s10.courses["SSW 540"] = "A"
        expected:Dict[str,Student]={
            '10103': s1,
            '10115': s2,
            '10172': s3,
            '10175': s4,
            '10183': s5,
            '11399': s6,
            '11461': s7,
            '11658': s8,
            '11714': s9,
            '11788': s10,
        }
        self.assertEqual(a.studict["10103"].cwid,expected["10103"].cwid)
        self.assertEqual(a.studict["10103"].name,expected["10103"].name)
        self.assertEqual(a.studict["10103"].major,expected["10103"].major)
        self.assertEqual(a.studict["10103"].courses.keys(),expected["10103"].courses.keys())

        self.assertEqual(a.studict["10115"].cwid,expected["10115"].cwid)
        self.assertEqual(a.studict["10115"].name,expected["10115"].name)
        self.assertEqual(a.studict["10115"].major,expected["10115"].major)
        self.assertEqual(a.studict["10115"].courses.keys(),expected["10115"].courses.keys())

        self.assertEqual(a.studict["10172"].cwid,expected["10172"].cwid)
        self.assertEqual(a.studict["10172"].name,expected["10172"].name)
        self.assertEqual(a.studict["10172"].major,expected["10172"].major)
        self.assertEqual(a.studict["10172"].courses.keys(),expected["10172"].courses.keys())

        self.assertEqual(a.studict["10175"].cwid,expected["10175"].cwid)
        self.assertEqual(a.studict["10175"].name,expected["10175"].name)
        self.assertEqual(a.studict["10175"].major,expected["10175"].major)
        self.assertEqual(a.studict["10175"].courses.keys(),expected["10175"].courses.keys())

        self.assertEqual(a.studict["10183"].cwid,expected["10183"].cwid)
        self.assertEqual(a.studict["10183"].name,expected["10183"].name)
        self.assertEqual(a.studict["10183"].major,expected["10183"].major)
        self.assertEqual(a.studict["10183"].courses.keys(),expected["10183"].courses.keys())

        self.assertEqual(a.studict["11399"].cwid,expected["11399"].cwid)
        self.assertEqual(a.studict["11399"].name,expected["11399"].name)
        self.assertEqual(a.studict["11399"].major,expected["11399"].major)
        self.assertEqual(a.studict["11399"].courses.keys(),expected["11399"].courses.keys())

        self.assertEqual(a.studict["11461"].cwid,expected["11461"].cwid)
        self.assertEqual(a.studict["11461"].name,expected["11461"].name)
        self.assertEqual(a.studict["11461"].major,expected["11461"].major)
        self.assertEqual(a.studict["11461"].courses.keys(),expected["11461"].courses.keys())

        self.assertEqual(a.studict["11658"].cwid,expected["11658"].cwid)
        self.assertEqual(a.studict["11658"].name,expected["11658"].name)
        self.assertEqual(a.studict["11658"].major,expected["11658"].major)
        self.assertEqual(a.studict["11658"].courses.keys(),expected["11658"].courses.keys())

        self.assertEqual(a.studict["11714"].cwid,expected["11714"].cwid)
        self.assertEqual(a.studict["11714"].name,expected["11714"].name)
        self.assertEqual(a.studict["11714"].major,expected["11714"].major)
        self.assertEqual(a.studict["11714"].courses.keys(),expected["11714"].courses.keys())

        self.assertEqual(a.studict["11788"].cwid,expected["11788"].cwid)
        self.assertEqual(a.studict["11788"].name,expected["11788"].name)
        self.assertEqual(a.studict["11788"].major,expected["11788"].major)
        self.assertEqual(a.studict["11788"].courses.keys(),expected["11788"].courses.keys())


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)