
class Testclass:
    fname1=None
    fname2=None
    address=None

    def __init__(self,fname,lname):
        self.fname1=fname
        self.lname1=lname

    def m_person(self):
        print("My name is: ",self.fname1,self.lname1)

    def m_address(self,address):
        print("My address is:",address)


info=Testclass('Tejal',"Patel")
info.m_person() #Value is print from default constructor as it initialized first
info.m_address("Surat")


