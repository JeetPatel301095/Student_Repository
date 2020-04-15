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
        s1: Student = Student("10103","Jobs, S","SFEN")
        s2: Student = Student("10115","Bezos, J","SFEN")
        s3: Student = Student("10183","Musk, E","SFEN")
        s4: Student = Student("11714","Gates, B","CS")

        s1.set_courses("SSW 810","A-")
        s1.set_courses("CS 501","B")	
        s2.set_courses("SSW 810","A")	
        s2.set_courses("CS 546","F")	
        s3.set_courses("SSW 555","A")	
        s3.set_courses("SSW 810","A")	
        s4.set_courses("SSW 810","B-")
        s4.set_courses("CS 546","A")	
        s4.set_courses("CS 570","A-")

        s1.computeGpa()
        s2.computeGpa()
        s3.computeGpa()
        s4.computeGpa()
        
        s1.computeRemainingRequiredList(a.majDict[s1.major])
        s2.computeRemainingRequiredList(a.majDict[s2.major])
        s3.computeRemainingRequiredList(a.majDict[s3.major])
        s4.computeRemainingRequiredList(a.majDict[s4.major])
        
        s1.computeRemainingElectiveList(a.majDict[s1.major])
        s2.computeRemainingElectiveList(a.majDict[s2.major])
        s3.computeRemainingElectiveList(a.majDict[s3.major])
        s4.computeRemainingElectiveList(a.majDict[s4.major])

        self.assertEqual(s1.getStudentDetails(),a.studict["10103"].getStudentDetails())
        self.assertEqual(s2.getStudentDetails(),a.studict["10115"].getStudentDetails())
        self.assertEqual(s3.getStudentDetails(),a.studict["10183"].getStudentDetails())
        self.assertEqual(s4.getStudentDetails(),a.studict["11714"].getStudentDetails())

    def test_instdict(self) -> None:
        """Test class to test the Instructor Dictionary for Stevens"""
        path="C:/Users/Jeet/Jeet/SW-810/Student_Repository/StevensFiles"
        try:
            a:University = University(path,"Stevens Institute of Technology")
        except FileNotFoundError as e:
            print(e)
        except ValueError as e:
            print(e)
        i1 : Instructor = Instructor("98764","Cohen, R","SFEN")
        i2 : Instructor = Instructor("98763","Rowland, J","SFEN")
        i3 : Instructor = Instructor("98762","Hawking, S","CS")
        
        i2.set_courses("SSW 810")
        i3.set_courses("CS 501")
        i2.set_courses("SSW 810")
        i3.set_courses("CS 546")
        i2.set_courses("SSW 555")
        i2.set_courses("SSW 810")
        i2.set_courses("SSW 810")
        i1.set_courses("CS 546")
        i3.set_courses("CS 570")

        self.assertEqual(i1.getInstructorDetails(),a.instdict["98764"].getInstructorDetails())
        self.assertEqual(i2.getInstructorDetails(),a.instdict["98763"].getInstructorDetails())
        self.assertEqual(i3.getInstructorDetails(),a.instdict["98762"].getInstructorDetails())
        
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
        s1: Student = Student("10103","Jobs, S","SFEN")
        s2: Student = Student("10115","Bezos, J","SFEN")
        s3: Student = Student("10183","Musk, E","SFEN")
        s4: Student = Student("11714","Gates, B","CS")

        s1.set_courses("SSW 810","A-")
        s1.set_courses("CS 501","B")	
        s2.set_courses("SSW 810","A")	
        s2.set_courses("CS 546","F")	
        s3.set_courses("SSW 555","A")	
        s3.set_courses("SSW 810","A")	
        s4.set_courses("SSW 810","B-")
        s4.set_courses("CS 546","A")	
        s4.set_courses("CS 570","A-")

        s1.computeGpa()
        s2.computeGpa()
        s3.computeGpa()
        s4.computeGpa()
        
        s1.computeRemainingRequiredList(a.majDict[s1.major])
        s2.computeRemainingRequiredList(a.majDict[s2.major])
        s3.computeRemainingRequiredList(a.majDict[s3.major])
        s4.computeRemainingRequiredList(a.majDict[s4.major])
        
        s1.computeRemainingElectiveList(a.majDict[s1.major])
        s2.computeRemainingElectiveList(a.majDict[s2.major])
        s3.computeRemainingElectiveList(a.majDict[s3.major])
        s4.computeRemainingElectiveList(a.majDict[s4.major])

        self.assertEqual(s1.getStudentDetails(),a.studict["10103"].getStudentDetails())
        self.assertEqual(s2.getStudentDetails(),a.studict["10115"].getStudentDetails())
        self.assertEqual(s3.getStudentDetails(),a.studict["10183"].getStudentDetails())
        self.assertEqual(s4.getStudentDetails(),a.studict["11714"].getStudentDetails())

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
        m2: Majors = Majors("CS")

        m1.setCourses("R","SSW 540")
        m1.setCourses("R","SSW 810")
        m1.setCourses("R","SSW 555")
        m1.setCourses("E","CS 501")
        m1.setCourses("E","CS 546")
        m2.setCourses("R","CS 570")
        m2.setCourses("R","CS 546")
        m2.setCourses("E","SSW 810")
        m2.setCourses("E","SSW 565")

        self.assertEqual(m1.getMajorDetails(),a.majDict["SFEN"].getMajorDetails())
        self.assertEqual(m2.getMajorDetails(),a.majDict["CS"].getMajorDetails())

    def test_db_content(self):
        expected : List[Tuple[str]] = [('Jobs, S', '10103', 'SSW 810', 'A-', 'Rowland, J'), ('Jobs, S', '10103', 'CS 501', 'B', 'Hawking, S'), ('Bezos, J', '10115', 'SSW 810', 'A', 'Rowland, J'), ('Bezos, J', '10115', 'CS 546', 'F', 'Hawking, S'), ('Musk, E', '10183', 'SSW 555', 'A', 'Rowland, J'), ('Musk, E', '10183', 'SSW 810', 'A', 'Rowland, J'), ('Gates, B', '11714', 'SSW 810', 'B-', 'Rowland, J'), ('Gates, B', '11714', 'CS 546', 'A', 'Cohen, R'), ('Gates, B', '11714', 'CS 570', 'A-', 'Hawking, S')]
        path="C:/Users/Jeet/Jeet/SW-810/Student_Repository/StevensFiles"
        db_path = "C:/Users/Jeet/Jeet/SW-810/Student_Repository/810_startup.db"
        try:
            a:University = University(path,"Stevens Institute of Technology")
        except FileNotFoundError as e:
            print(e)
        except ValueError as e:
            print(e)
        returned = a.student_grades_table_db(db_path)
        self.assertEqual(expected,returned)
    
if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)