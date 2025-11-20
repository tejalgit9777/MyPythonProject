#Encapsulation example 2

class Family:
    mom = None
    dad = None
    husband = None

    def __init__(self,mom1,dad1,husband1):
        self.mom = mom1
        self.dad = dad1
        self.__husband = husband1

    def m_mom(self):
        print("Hello",self.__husband)
        print("Hi papa", self.dad)
        print("Helllooo mummy", self.mom)
        self.__m_husband()

    def __m_husband(self):
        print("=================")
        print("Hello",self.__husband)
        print("Hi",self.dad)
        print("Helllooo",self.mom)


fam = Family("Mom...","Dad...","Husband....")
fam.m_mom()




