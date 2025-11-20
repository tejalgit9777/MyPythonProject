# Hybrid Inheritance
class Teacher:

    def subject_math(self):
        print("We are learning Maths")

    def subject_science(self):
        print("We are learning Science")

    def subject_accounts(self):
        print("We are learning accounts")

class Teju_student(Teacher):

    def Learn(self):
        self.subject_math()
        self.subject_accounts()
        self.subject_science()
        print("Explained to 2 more students")
        print("==============================")

class Tejal_student(Teju_student):

    def Learning(self):
        self.Learn()
        print("Prepared for Exam")

class Principal(Tejal_student, Teacher):

    def Exam(self):
        self.Learning()
        print("Final Exam")

school = Principal()
school.Exam()