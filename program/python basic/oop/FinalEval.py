# FinalEval.py
from StudenExtraCarcular import StudentExCurr
from TeacherDetails import TeacherDetails

class FinalEval(StudentExCurr, TeacherDetails):
    def __init__(self, ccode, cname, rollno, sname, n1, n2, n3, exm1, exm2, empid, tname, dept, feedback_from_teacher):
        # Initialize the Student side (StudentExCurr -> StudentDetails -> College)
        StudentExCurr.__init__(self, rollno, sname, n1, n2, n3, ccode, cname, exm1, exm2)
        # Initialize the Teacher side
        TeacherDetails.__init__(self, ccode, cname, empid, tname, dept)
        self.feedback_from_teacher = feedback_from_teacher

    def display_all(self):
        return {
            "college": self.display,            # College.display property (ccode, cname)
            "rollno": self.rollno,
            "sname": self.get_sname(),
            "marks_total": self.calc_tot(),
            "marks_avg": self.calc_avg(),
            "extra_total": self.calc_extot(),
            "teacher": self.display(),          # teacher tuple
            "teacher_feedback": self.feedback_from_teacher
        }
