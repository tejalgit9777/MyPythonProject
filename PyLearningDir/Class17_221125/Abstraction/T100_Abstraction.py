from abc import ABC, abstractmethod

class Father(ABC):

    @abstractmethod
    def loan_method(self):
        pass

class Child(Father):

    def loan_method(self):
        print("I will complete my All EMI of loan")

c=Child()
c.loan_method()
