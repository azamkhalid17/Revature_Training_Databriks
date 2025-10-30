from student_details import StudentDetails
from StudenExtraCarcular import StudentExCurr
from FinalEval import FinalEval
from TeacherDetails import TeacherDetails

def main():
    # collect college info
    ccode = input('Enter ccode: ')
    cname = input('Enter cname: ')

    # student info
    rollno = input("Enter rollno: ")
    name = input("Enter name: ")
    try:
        n1 = int(input("Mark 1: "))
        n2 = int(input("Mark 2: "))
        n3 = int(input("Mark 3: "))
        exm1 = int(input("Extra Mark 1: "))
        exm2 = int(input("Extra Mark 2: "))
    except ValueError:
        print("Invalid marks entered. Please enter integer values.")
        return

    # Note the constructor order for StudentDetails: rollno, sname, n1, n2, n3, ccode, cname
    stud = StudentDetails(rollno, name, n1, n2, n3, ccode, cname)

    # display basic student/college info
    college_info = stud.display  # tuple (ccode, cname)
    print(f"College Code: {college_info[0]} \t College Name: {college_info[1]}")
    print(f"Roll No: {stud.rollno}")
    print(f"Student Name: {stud.get_sname()}")
    print(f"Total Marks: {stud.calc_tot()}")
    print(f"Average Marks: {stud.calc_avg():.2f}")

    # teacher info
    empid = input('Enter empid: ')
    tname = input('Enter tname: ')
    dept = input('Enter department: ')
    teacher = TeacherDetails(ccode, cname, empid, tname, dept)
    print("\nTeacher Info:")
    teacher.print_display()

    # final evaluation combining student extras and teacher info
    feedbackfromteacher = input('Enter feedback from teacher: ')
    # FinalEval __init__: ccode,cname,rollno,sname,n1,n2,n3,exm1,exm2,empid,tname,dept,feedback
    finaleval = FinalEval(ccode, cname, rollno, name, n1, n2, n3, exm1, exm2, empid, tname, dept, feedbackfromteacher)

    print("\nFinal Evaluation Summary:")
    info = finaleval.display_all()
    print(f"College: {info['college']}")
    print(f"Roll No: {info['rollno']}")
    print(f"Student Name: {info['sname']}")
    print(f"Marks Total: {info['marks_total']}")
    print(f"Marks Average: {info['marks_avg']:.2f}")
    print(f"Extra-curricular Total: {info['extra_total']}")
    print(f"Teacher Info: {info['teacher']}")
    print(f"Teacher Feedback: {info['teacher_feedback']}")

if __name__ == "__main__":
    main()



