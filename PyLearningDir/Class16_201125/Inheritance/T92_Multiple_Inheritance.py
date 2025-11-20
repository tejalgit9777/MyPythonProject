# Multiple Inheritance
class Grandfather:
    def house(self):
        print("Old House")

    def farmhouse(self):
        print("Old Farm")

class  Father:

    def __init__(self):
        print("My father class")

class Children(Grandfather, Father):

    def newhouse(self):
        print("New House")
        self.house()
        self.farmhouse()

child=Children()
child.newhouse()




