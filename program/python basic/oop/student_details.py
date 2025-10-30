# student_details.py
from college import College

class StudentDetails(College):
    def __init__(self, rollno, sname, n1, n2, n3, ccode, cname):
        # direct call avoids MRO issues when used in multiple inheritance
        College.__init__(self, ccode, cname)
        self.__rollno = rollno
        self.__sname = sname
        self.__n1 = n1
        self.__n2 = n2
        self.__n3 = n3

    @property
    def rollno(self):
        return self.__rollno

    @rollno.setter
    def rollno(self, rollno):
        self.__rollno = rollno

    def get_sname(self):
        return self.__sname

    def set_sname(self, sname):
        self.__sname = sname

    def calc_tot(self):
        return self.__n1 + self.__n2 + self.__n3

    def calc_avg(self):
        return self.calc_tot() / 3

