"""Test File for Student Repository"""

import unittest
from Student_Repository_Jeet_Divyangbhai_Patel import University,Student,Instructor,Majors

class HW09Test(unittest.TestCase):
    """Test Class for Student Repository"""
    def test_studict(self) -> None:
        """Test class to test the Student Dictionary for Stevens"""
        path="C:/Users/Jeet/Jeet/SW-810/Student_Repository/StevensFiles"
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

        s1.set_courses("CS 501", "B")
        s1.set_courses("SSW 564", "A-")
        s1.set_courses("SSW 567", "A")
        s1.set_courses("SSW 687", "B")
        s2.set_courses("CS 545","A")
        s2.set_courses("SSW 564", "B+")
        s2.set_courses("SSW 567", "A")
        s2.set_courses("SSW 687", "A")
        s3.set_courses("SSW 555", "A")
        s3.set_courses("SSW 567", "A-")
        s4.set_courses("SSW 564", "A")
        s4.set_courses("SSW 567", "A")
        s4.set_courses("SSW 687", "B-")
        s5.set_courses("SSW 689", "A")
        s6.set_courses("SSW 540", "B")
        s7.set_courses("SYS 611", "A")
        s7.set_courses("SYS 750", "A-")
        s7.set_courses("SYS 800", "A")
        s8.set_courses("SSW 540", "F")
        s9.set_courses("SYS 611", "A")
        s9.set_courses("SYS 645", "C")
        s10.set_courses("SSW 540", "A")

        s1.computeGpa()
        s2.computeGpa()
        s3.computeGpa()
        s4.computeGpa()
        s5.computeGpa()
        s6.computeGpa()
        s7.computeGpa()
        s8.computeGpa()
        s9.computeGpa()
        s10.computeGpa()

        s1.computeRemainingRequiredList(a.majDict[s1.major])
        s2.computeRemainingRequiredList(a.majDict[s2.major])
        s3.computeRemainingRequiredList(a.majDict[s3.major])
        s4.computeRemainingRequiredList(a.majDict[s4.major])
        s5.computeRemainingRequiredList(a.majDict[s5.major])
        s6.computeRemainingRequiredList(a.majDict[s6.major])
        s7.computeRemainingRequiredList(a.majDict[s7.major])
        s8.computeRemainingRequiredList(a.majDict[s8.major])
        s9.computeRemainingRequiredList(a.majDict[s9.major])
        s10.computeRemainingRequiredList(a.majDict[s10.major])
        
        s1.computeRemainingElectiveList(a.majDict[s1.major])
        s2.computeRemainingElectiveList(a.majDict[s2.major])
        s3.computeRemainingElectiveList(a.majDict[s3.major])
        s4.computeRemainingElectiveList(a.majDict[s4.major])
        s5.computeRemainingElectiveList(a.majDict[s5.major])
        s6.computeRemainingElectiveList(a.majDict[s6.major])
        s7.computeRemainingElectiveList(a.majDict[s7.major])
        s8.computeRemainingElectiveList(a.majDict[s8.major])
        s9.computeRemainingElectiveList(a.majDict[s9.major])
        s10.computeRemainingElectiveList(a.majDict[s10.major])

        self.assertEqual(s1.getStudentDetails(),a.studict["10103"].getStudentDetails())
        self.assertEqual(s2.getStudentDetails(),a.studict["10115"].getStudentDetails())
        self.assertEqual(s3.getStudentDetails(),a.studict["10172"].getStudentDetails())
        self.assertEqual(s4.getStudentDetails(),a.studict["10175"].getStudentDetails())
        self.assertEqual(s5.getStudentDetails(),a.studict["10183"].getStudentDetails())
        self.assertEqual(s6.getStudentDetails(),a.studict["11399"].getStudentDetails())
        self.assertEqual(s7.getStudentDetails(),a.studict["11461"].getStudentDetails())
        self.assertEqual(s8.getStudentDetails(),a.studict["11658"].getStudentDetails())
        self.assertEqual(s9.getStudentDetails(),a.studict["11714"].getStudentDetails())
        self.assertEqual(s10.getStudentDetails(),a.studict["11788"].getStudentDetails())

    def test_instdict(self) -> None:
        """Test class to test the Instructor Dictionary for Stevens"""
        path="C:/Users/Jeet/Jeet/SW-810/Student_Repository/StevensFiles"
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

        i2.set_courses("SSW 564")
        i2.set_courses("SSW 687")
        i2.set_courses("CS 501")
        i1.set_courses("SSW 567")
        i1.set_courses("SSW 567")
        i2.set_courses("SSW 564")
        i2.set_courses("SSW 687")
        i2.set_courses("CS 545")
        i3.set_courses("SSW 555")
        i1.set_courses("SSW 567")
        i1.set_courses("SSW 567")
        i2.set_courses("SSW 564")
        i2.set_courses("SSW 687")
        i3.set_courses("SSW 689")
        i1.set_courses("SSW 540")
        i6.set_courses("SYS 800")
        i6.set_courses("SYS 750")
        i6.set_courses("SYS 611")
        i1.set_courses("SSW 540")
        i6.set_courses("SYS 611")
        i6.set_courses("SYS 645")
        i1.set_courses("SSW 540")

        self.assertEqual(i1.getInstructorDetails(),a.instdict["98765"].getInstructorDetails())
        self.assertEqual(i2.getInstructorDetails(),a.instdict["98764"].getInstructorDetails())
        self.assertEqual(i3.getInstructorDetails(),a.instdict["98763"].getInstructorDetails())
        self.assertEqual(i4.getInstructorDetails(),a.instdict["98762"].getInstructorDetails())
        self.assertEqual(i5.getInstructorDetails(),a.instdict["98761"].getInstructorDetails())
        self.assertEqual(i6.getInstructorDetails(),a.instdict["98760"].getInstructorDetails())

    def test_fileNotFoundError(self) -> None:
        """Test class to test the FileNotFoundError"""
        path:str = "C:/Users/Jeet/Jeet/SW-810/Student_Repository/"
        with self.assertRaises(FileNotFoundError):
            result3 = University(path,"Stevens")

    def test_valueerror(self) -> None:
        """Test class to test the ValueError"""
        path:str = "C:/Users/Jeet/Jeet/SW-810/Student_Repository/StevensErrorFiles"
        with self.assertRaises(ValueError):
            result3 = University(path,"Stevens")
        
    def test_different_unis(self) -> None:
        """Test class to test the Student Dictionary for NYU just by sending different path"""
        path="C:/Users/Jeet/Jeet/SW-810/Student_Repository/NYUFiles/"
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

        s1.set_courses("CS 501", "B")
        s1.set_courses("SSW 564", "A-")
        s1.set_courses("SSW 567", "A")
        s1.set_courses("SSW 687", "B")
        s2.set_courses("CS 545","A")
        s2.set_courses("SSW 564", "B+")
        s2.set_courses("SSW 567", "A")
        s2.set_courses("SSW 687", "A")
        s3.set_courses("SSW 555", "A")
        s3.set_courses("SSW 567", "A-")
        s4.set_courses("SSW 564", "A")
        s4.set_courses("SSW 567", "A")
        s4.set_courses("SSW 687", "B-")
        s5.set_courses("SSW 689", "A")
        s6.set_courses("SSW 540", "B")
        s7.set_courses("SYS 611", "A")
        s7.set_courses("SYS 750", "A-")
        s7.set_courses("SYS 800", "A")
        s8.set_courses("SSW 540", "F")
        s9.set_courses("SYS 611", "A")
        s9.set_courses("SYS 645", "C")
        s10.set_courses("SSW 540", "A")

        s1.computeGpa()
        s2.computeGpa()
        s3.computeGpa()
        s4.computeGpa()
        s5.computeGpa()
        s6.computeGpa()
        s7.computeGpa()
        s8.computeGpa()
        s9.computeGpa()
        s10.computeGpa()

        s1.computeRemainingRequiredList(a.majDict[s1.major])
        s2.computeRemainingRequiredList(a.majDict[s2.major])
        s3.computeRemainingRequiredList(a.majDict[s3.major])
        s4.computeRemainingRequiredList(a.majDict[s4.major])
        s5.computeRemainingRequiredList(a.majDict[s5.major])
        s6.computeRemainingRequiredList(a.majDict[s6.major])
        s7.computeRemainingRequiredList(a.majDict[s7.major])
        s8.computeRemainingRequiredList(a.majDict[s8.major])
        s9.computeRemainingRequiredList(a.majDict[s9.major])
        s10.computeRemainingRequiredList(a.majDict[s10.major])
        
        s1.computeRemainingElectiveList(a.majDict[s1.major])
        s2.computeRemainingElectiveList(a.majDict[s2.major])
        s3.computeRemainingElectiveList(a.majDict[s3.major])
        s4.computeRemainingElectiveList(a.majDict[s4.major])
        s5.computeRemainingElectiveList(a.majDict[s5.major])
        s6.computeRemainingElectiveList(a.majDict[s6.major])
        s7.computeRemainingElectiveList(a.majDict[s7.major])
        s8.computeRemainingElectiveList(a.majDict[s8.major])
        s9.computeRemainingElectiveList(a.majDict[s9.major])
        s10.computeRemainingElectiveList(a.majDict[s10.major])

        self.assertEqual(s1.getStudentDetails(),a.studict["10103"].getStudentDetails())
        self.assertEqual(s2.getStudentDetails(),a.studict["10115"].getStudentDetails())
        self.assertEqual(s3.getStudentDetails(),a.studict["10172"].getStudentDetails())
        self.assertEqual(s4.getStudentDetails(),a.studict["10175"].getStudentDetails())
        self.assertEqual(s5.getStudentDetails(),a.studict["10183"].getStudentDetails())
        self.assertEqual(s6.getStudentDetails(),a.studict["11399"].getStudentDetails())
        self.assertEqual(s7.getStudentDetails(),a.studict["11461"].getStudentDetails())
        self.assertEqual(s8.getStudentDetails(),a.studict["11658"].getStudentDetails())
        self.assertEqual(s9.getStudentDetails(),a.studict["11714"].getStudentDetails())
        self.assertEqual(s10.getStudentDetails(),a.studict["11788"].getStudentDetails())

    def test_majors(self) ->None:
        """Method to test all majors"""
        path="C:/Users/Jeet/Jeet/SW-810/Student_Repository/StevensFiles"
        try:
            a:University = University(path,"Stevens Institute of Technology")
        except FileNotFoundError as e:
            print(e)
        except ValueError as e:
            print(e)
        m1: Majors = Majors("SFEN")
        m2: Majors = Majors("SYEN")

        m1.setCourses("R","SSW 540")		
        m1.setCourses("R","SSW 564")		
        m1.setCourses("R","SSW 555")		
        m1.setCourses("R","SSW 567")		
        m1.setCourses("E","CS 501")	    	
        m1.setCourses("E","CS 513")	    	
        m1.setCourses("E","CS 545")	    	
        m2.setCourses("R","SYS 671")		
        m2.setCourses("R","SYS 612")		
        m2.setCourses("R","SYS 800")		
        m2.setCourses("E","SSW 810")		
        m2.setCourses("E","SSW 565")		
        m2.setCourses("E","SSW 540")		

        self.assertEqual(m1.getMajorDetails(),a.majDict["SFEN"].getMajorDetails())
        self.assertEqual(m2.getMajorDetails(),a.majDict["SYEN"].getMajorDetails())

    
if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)