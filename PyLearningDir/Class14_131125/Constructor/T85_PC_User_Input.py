# PC User input

class   JobProfile:
    name =None
    profession = None

    def __init__(self):
        self.name= str(input("Enter Your Name: " ))
        self.profession=str(input("Enter Your Profession: "))
        print("Your Job Profile is:\n")
        print("Name:",self.name)
        print("Profession:",self.profession)

    def m_QA(self):
        print("QA Name:",self.name)
        print("QA Profession:",self.profession)

    def m_Developer(self,name2,profession2):
        print("Developer Name:",name2)
        print("Developer Profession:",profession2)

    def m_Designer(self):
        print("Designer Name:",self.name)
        print("Designer Profession:",self.profession)


jobprof=JobProfile()
jobprof.m_QA()
jobprof.m_Developer("Teju","Patel")
jobprof1=JobProfile()
jobprof1.m_Designer()