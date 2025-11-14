# Constructor

class MyClass:
    a=None
    b=None

    def __init__(self):
        print("Default Constructor")

    def m_sum(self,a,b):
        return a+b

    def m_sub(self,a,b):
        return a-b

    def m_mul(self,a,b):
        return a*b

    def m_div(self,a,b):
        return a/b

cal=MyClass()
print(cal.m_sum(12,11))
print(cal.m_sub(11,11))
print(cal.m_mul(18,3))
print(cal.m_div(10,5))


