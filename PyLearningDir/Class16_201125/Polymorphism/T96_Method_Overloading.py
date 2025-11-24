# Method Overloading ==> Python does not supporting method overloading
# Same method with different parameter

class Person:

    def display(self,name1):
        print("Name is",name1)

    def display(self,name1,name2):
        print("Name is: ",name1,name2)

p=Person()
p.display("Teju","Patel")
