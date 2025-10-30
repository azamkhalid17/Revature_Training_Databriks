# StudenExtraCarcular.py
from student_details import StudentDetails

class StudentExCurr(StudentDetails):
    def __init__(self, rollno, sname, n1, n2, n3, ccode, cname, exm1=0, exm2=0):
        # initialize StudentDetails (which itself initializes College directly)
        StudentDetails.__init__(self, rollno, sname, n1, n2, n3, ccode, cname)
        self.exm1 = exm1
        self.exm2 = exm2

    def calc_extot(self):
        return self.exm1 + self.exm2
