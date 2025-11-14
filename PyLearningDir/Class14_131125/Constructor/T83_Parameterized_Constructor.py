# Constructor

class MyClass:
    a=None
    b=None

    def __init__(self,a1,b1):
        self.a=a1
        self.b=b1
        print("Sum from constructor: ",a1+b1)

    def m_sum(self,a,b):
        return a+b

    def m_sub(self,a,b):
        return a-b

    def m_mul(self,a,b):
        return a*b

    def m_div(self,a,b):
        return a/b

    def m_module(self):
        return self.a % self.b

cal=MyClass(21,5)
print("Sum: ",cal.m_sum(12,11)) # pass value in method itself
print("Subtraction: ",cal.m_sub(11,11))
print("Multiplication: ",cal.m_mul(18,3))
print("Division: ",cal.m_div(10,5))
print(cal.m_module()) # take value from constructor


