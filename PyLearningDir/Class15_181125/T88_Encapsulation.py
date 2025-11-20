#Encapsulation

class Car:
    make = None
    model = None
    year = None
    def __init__(self, make1, model1, year1):
        self.make = make1
        self.__model = model1
        self.__year = year1

    def method_car(self):
        print(self.make, self.__model, self.__year)

car = Car("Ford", "Mustang", 1999)
print(car.make)
# print(car.__model)
# print(car.__year)

car.method_car()


