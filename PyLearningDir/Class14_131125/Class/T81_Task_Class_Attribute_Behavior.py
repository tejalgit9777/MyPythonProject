# Create a Person class where we will have five attributes and five behaviors.
# Make sure that each type of function is used, and I want you to also create the print function
# which will print all the instance variable values.

class School:
    #Attribute
    studyclass = None
    subject= None
    student= None
    meduim= None
    schoolname= None

    #behavior

    # Method without parameters & with return type
    def m_studyclass(self):
        return "Study Class: 10th"

    #  Method with one parameter & with return type
    def m_subject(self, subject):
        return "Subject:",subject

    # Method with multiple parameters & with return type
    def m_student(self, name, rollno):
        print("Student Name: ",name,"Roll No:",rollno)

    #  Method without parameters but returning a value
    def m_medium(self):
        print("Medium: English")

    #  Method with parameters & returning combined info
    def m_schoolname(self, sname, address):
        return "School:",sname, "Address:",address

LMV=School()
print(LMV.m_studyclass())                         # No parameter
print(LMV.m_subject("Science"))                   # One parameter
LMV.m_student("Siya", 21)             # Multiple parameters
LMV.m_medium()                                    # No parameter
print(LMV.m_schoolname("Bright School", "Vadodara"))  # With parameters













