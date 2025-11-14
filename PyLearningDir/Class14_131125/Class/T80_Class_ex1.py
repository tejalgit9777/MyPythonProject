# class

class MyClass:
    #attributes
    name= None
    age= None
    dob= None
    location= None

    # Behaviour
    def method_wakeup(self):
        print("Wake up")

    def method_exercise(self):
        print("Exercise")

    def method_breakfast(self):
        print("Breakfast")

    def method_lunch(self):
        print("Lunch")


#function out of class
def function_dinner():
    print("Dinner")

def function_party(self):
    print(self)

# create object
teju= MyClass()
tejal= MyClass()
teju.method_wakeup()
teju.method_exercise()
tejal.method_breakfast()
tejal.method_lunch()

function_dinner()
function_party("Party")







