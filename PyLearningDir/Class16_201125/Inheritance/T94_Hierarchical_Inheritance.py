# Hierarchical Inheritance

class Teacher:

    def subject_math(self):
        print("We are learning Maths")

    def class_science(self):
        print("We are learning Science")

    def class_accounts(self):
        print("We are learning accounts")
print("==================================")
class classroom1(Teacher):

    def study(self):
        self.class_science()
        self.subject_math()
        self.class_accounts()
        print("We are learning all  class 1")


class classroom2(Teacher):

    def study(self):
        self.subject_math()
        self.class_science()
        self.class_accounts()
        print("We are learning all subjects class2")

cls1=classroom1()
cls1.study()
print("==================================")
cls2=classroom2()
cls2.study()
