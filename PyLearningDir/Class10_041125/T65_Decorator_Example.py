# Decorators Example

def test1(func):
    def wrapper():
        print("Shinest@r")
        func()
        print("Tejal")
    return wrapper()

@test1
def test():
    print("Star!!!")