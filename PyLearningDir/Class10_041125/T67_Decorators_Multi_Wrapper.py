#Multiple wrapper

def suzuki(func):
    def wrapper():
        print("I like suzuki Burgman")
        func()
        print("I don't like suzuki Gixxer")
    return wrapper

def honda(func):
    def wrapper1():
        print("I like honda Shine")
        func()
        print("I don't like Activa 6G")
    return wrapper1

@suzuki
@honda
def bike():
    print("I love to drive Access 125")
bike()

