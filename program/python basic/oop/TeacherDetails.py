# TeacherDetails.py
from college import College

class TeacherDetails(College):
    def __init__(self, ccode, cname, empid, tname, dept):
        # direct call avoids interfering with StudentDetails when used in FinalEval
        College.__init__(self, ccode, cname)
        self.empid = empid
        self.tname = tname
        self.dept = dept

    def display(self):
        return (self._ccode, self._cname, self.empid, self.tname, self.dept)

    def print_display(self):
        print(f"{self._ccode} \t {self._cname}")
        print(f"EmpID: {self.empid}, Name: {self.tname}, Dept: {self.dept}")
