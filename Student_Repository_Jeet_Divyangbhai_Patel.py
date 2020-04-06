from typing import Iterator,List,IO
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
        self.studict : Dict[cwid,Student] = dict()
        self.instdict : Dict[cwid,Instructor] = dict()
        try:
            self.readstu()
            self.readins()
            self.readgra()
        except FileNotFoundError as e:
            print(e)
            raise e
        except ValueError as e:
            print(e)
            raise e
    
    def readstu(self) -> None:
        """Method to store values from students.txt into Student Dictionary"""
        path :str = os.path.join(self.directory_path,"students.txt")
        for cwid, name, major in file_reader(path, 3, sep='\t'):  
            b: Student = Student(cwid,name,major)
            self.studict[cwid]=b

    def readins(self) -> None:
        """Method to store values from instructors.txt into Instructors Dictionary"""
        path :str = os.path.join(self.directory_path,"instructors.txt")
        for cwid, name, department in file_reader(path, 3, sep='\t'):  
            b: Instructor = Instructor(cwid,name,department)
            self.instdict[cwid]=b

    def readgra(self) -> None:
        """Method to store values from grades.txt into Student Dictionary and Instructor Dictionary"""
        path :str = os.path.join(self.directory_path,"grades.txt")
        for stucwid, coursename, grade, instcwid in file_reader(path, 4, sep='\t'):  
            if stucwid not in self.studict.keys():
                print(f" There is no Student with CWID: {stucwid}")
                continue
            if instcwid not in self.instdict.keys():
                print(f" There is no Instructor with CWID: {instcwid}")
                continue
            self.studict[stucwid].courses[coursename]=grade
            self.instdict[instcwid].courses[coursename]+=1
            

    def print_stu(self) -> None:
        """Method to print details of Students into Tables"""
        pt:PrettyTable = PrettyTable(field_names=["CWID","Name","Major","Courses"])
        for cwid, student in self.studict.items():
            pt.add_row([cwid,student.name,student.major,sorted(student.courses.keys())])
        print(pt)
    
    def print_ins(self)-> None:
        """Method to print details of Instructors into Tables"""
        pt:PrettyTable = PrettyTable(field_names=["CWID","Name","Dept","Course","Students"])
        for cwid, ins in self.instdict.items():
            if not ins.courses:
                pt.add_row([cwid,ins.name,ins.department,"NA","NA"])
            for course , no_of_students in ins.courses.items():
                pt.add_row([cwid,ins.name,ins.department,course,no_of_students])
        print(pt)
    


class Student:
    """Class to store values of Individual Students"""
    def __init__(self,cwid :str ,name :str ,major :str ) -> None:
        """init Method to initialize values of a Student"""
        self.cwid :str = cwid
        self.name :str = name
        self.major :str = major
        self.courses : Dict[str,str] = dict()
    
class Instructor:
    """Class to store values of Individual Instructors"""
    def __init__(self,cwid :str ,name :str ,department :str ) -> None:
        """init Method to initialize values of a Instructor"""
        self.cwid :str = cwid
        self.name :str = name
        self.department :str = department
        self.courses : DefaultDict[str,int] = defaultdict(int)


# path="C:/Users/Jeet/Jeet/SW-810/HW09JeetDivyangbhaiPatel/"
# a:University = University(path,"Stevens Institute of Technology")
# a.print_ins()
# a.print_stu()
# print(a.studict)