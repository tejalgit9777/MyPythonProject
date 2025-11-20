# Encapsulation Example 3
import random
class Bank:
    bank_name = None
    __balance = random.randint(1,1000)
    AC_Number = None

    def __init__(self):
        print("Initializing Bank")
        self.AC_Number = int(input("Enter AC Number: ").strip())

    def m_balance(self):
        if self.AC_Number == 123456789:
            print("Valid account!!","Balance: ",self.__balance,"Account Number: ",self.AC_Number)
        else:
            print("Invalid account!!",self.AC_Number)

my_bank = Bank()
my_bank.m_balance()