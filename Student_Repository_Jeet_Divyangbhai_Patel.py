from typing import Iterator,List,IO,Dict
from collections import defaultdict
import os
from prettytable import PrettyTable


def file_reader(path:str, fields:int, sep: str = "," ,header: bool = False) -> Iterator[List[str]]:
    """File_Reader function from HW-08"""
    linenumber:int = 1 if header == False else 0
    try:
        fp:IO = open(path,'r')
    except FileNotFoundError:
        raise FileNotFoundError(f"FileNotFoundError: Cannot Find a File at {path}")
    else:
        with fp:
            for line in fp:
                line = line.strip("\n")
                tokens:List[str] = line.split(sep)
                if len(tokens) != fields:
                    if linenumber == 0:
                        raise ValueError(f"ValueError: {os.path.basename(path)} has {len(tokens)} fields on Header Line but expected {fields}")
                    raise ValueError(f"ValueError: {os.path.basename(path)} has {len(tokens)} fields on line {linenumber} but expected {fields}")
                if linenumber == 0:
                    linenumber+=1
                    continue
                yield tokens
                linenumber+=1

class University:
    """Class to store instances of Different Universities"""
    def __init__(self,directory_path :str ,uni_name :str ) ->None:
        """init Method to initialize the path of the directory for Uni and read the files"""
        self.uni_name :str = uni_name
        self.directory_path :str  = directory_path
        self.studict : Dict[str,Student] = dict()
        self.instdict : Dict[str,Instructor] = dict()
        self.majDict : Dict[str,Majors] = dict()
        try:
            self.readstu()
            self.readins()
            self.readgra()
            self.readmajor()
        except FileNotFoundError as e:
            print(e)
            # raise e
        except ValueError as e:
            print(e)
            # raise e
        for student in self.studict.values():
            student.computeGpa()
            student.computeRemainingRequiredList(self.majDict[student.major])
            student.computeRemainingElectiveList(self.majDict[student.major])
    
    def readstu(self) -> None:
        """Method to store values from students.txt into Student Dictionary"""
        path :str = os.path.join(self.directory_path,"students.txt")
        for cwid, name, major in file_reader(path, 3, sep=';',header=True):  
            b: Student = Student(cwid,name,major)
            self.studict[cwid]=b

    def readins(self) -> None:
        """Method to store values from instructors.txt into Instructors Dictionary"""
        path :str = os.path.join(self.directory_path,"instructors.txt")
        for cwid, name, department in file_reader(path, 3, sep='|',header=True):  
            b: Instructor = Instructor(cwid,name,department)
            self.instdict[cwid]=b

    def readgra(self) -> None:
        """Method to store values from grades.txt into Student Dictionary and Instructor Dictionary"""
        path :str = os.path.join(self.directory_path,"grades.txt")
        for stucwid, coursename, grade, instcwid in file_reader(path, 4, sep='|',header=True):  
            if stucwid not in self.studict.keys():
                print(f" There is no Student with CWID: {stucwid}")
                continue
            if instcwid not in self.instdict.keys():
                print(f" There is no Instructor with CWID: {instcwid}")
                continue
            self.studict[stucwid].courses[coursename]=grade
            self.instdict[instcwid].courses[coursename]+=1
            
    def readmajor(self) ->None:
        path :str = os.path.join(self.directory_path,"majors.txt")
        for major,required,course in file_reader(path, 3, sep='\t',header=True):
            if not major in self.majDict:
                b:Majors = Majors(major)
                self.majDict[major] = b
            if required == "R":
                self.majDict[major].requiredCourses.append(course)
            elif required == "E":
                self.majDict[major].electiveCourses.append(course)
            


    def print_stu(self) -> None:
        """Method to print details of Students into Tables"""
        pt:PrettyTable = PrettyTable(field_names=["CWID","Name","Major","Courses","Remaining Required","Remaining Electives","GPA"])
        for cwid, student in self.studict.items():
            pt.add_row([cwid,student.name,student.major,sorted(student.courses.keys()),sorted(student.requiredRemaining),sorted(student.electiveRemaining),round(student.gpa,2)])
        print(pt)

    def print_maj(self) -> None:
        """Method to print details of Students into Tables"""
        pt:PrettyTable = PrettyTable(field_names=["Major","Required Courses","Elective Courses"])
        for major, major2 in self.majDict.items():
            pt.add_row([major2.major,sorted(major2.requiredCourses),sorted(major2.electiveCourses)])
        print(pt)
    
    def print_ins(self)-> None:
        """Method to print details of Instructors into Tables"""
        pt:PrettyTable = PrettyTable(field_names=["CWID","Name","Dept","Course","Students"])
        for cwid, ins in self.instdict.items():
            if not ins.courses:
                pt.add_row([cwid,ins.name,ins.department,"NA","NA"])
            for course , no_of_students in ins.courses.items():
                pt.add_row([cwid,ins.name,ins.department,course,no_of_students])
        # print(pt)
        return pt
    


class Student:
    __marks : Dict[str,float] ={
        "A" : 4.0,
        "A-" : 3.75,
        "B+" : 3.25,
        "B" : 3.0,
        "B-" : 2.75,
        "C+" : 2.25,
        "C" : 2.0,
        "C-" : 0,
        "D+" : 0,
        "D" : 0,
        "D-" : 0,
        "F" : 0
    }
    """Class to store values of Individual Students"""
    def __init__(self,cwid :str ,name :str ,major :str ) -> None:
        """init Method to initialize values of a Student"""
        self.cwid :str = cwid
        self.name :str = name
        self.major :str = major
        self.gpa : float = 0
        self.courses : Dict[str,str] = dict()
        self.requiredRemaining : List[str] = list()
        self.electiveRemaining : List[str] = list()

    def computeGpa(self):
        for value in self.courses.values():
            self.gpa+=Student.__marks[value]/len(self.courses)
    
    def computeRemainingRequiredList(self, major : "Majors" ) -> None:
        self.requiredRemaining = major.requiredCourses.copy()
        for key, value in self.courses.copy().items():
            if key in self.requiredRemaining:
                if Student.__marks[value] >= 2.0:
                    self.requiredRemaining.remove(key)
                else:
                    self.courses.pop(key)

    def computeRemainingElectiveList(self, major : "Majors") -> None:
        self.electiveRemaining = major.electiveCourses.copy()
        count: int = 0
        for key, value in self.courses.copy().items():
            if key in self.electiveRemaining:
                if Student.__marks[value] >= 2.0:
                    self.electiveRemaining.remove(key)
                    count+=1
                else:
                    self.courses.pop(key)
        if count >=1:
            self.electiveRemaining = list()
        

class Instructor:
    """Class to store values of Individual Instructors"""
    def __init__(self,cwid :str ,name :str ,department :str ) -> None:
        """init Method to initialize values of a Instructor"""
        self.cwid :str = cwid
        self.name :str = name
        self.department :str = department
        self.courses : DefaultDict[str,int] = defaultdict(int)

class Majors:
    """Class to store values of Individual Majors"""
    def __init__(self,major):
        self.major = major
        self.requiredCourses : List[str] = list()
        self.electiveCourses : List[str] = list()

path="C:/Users/Jeet/Jeet/SW-810/Student_Repository/StevensFiles"
a:University = University(path,"Stevens Institute of Technology")
b=a.print_ins()
print(b)
a.print_stu()
a.print_maj()