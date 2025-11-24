class MathOperations:

    @staticmethod
    def add(a,b):
        return a+b

    @staticmethod
    def sub(a,b):
        return a-b

    @staticmethod
    def mul(a,b):
        return a*b

m = MathOperations()
print(m.add(1,2))
print(m.sub(1,2))
print(m.mul(2,3))


print(MathOperations.add(20,10))
print(MathOperations.sub(20,10))
print(MathOperations.mul(20,10))
