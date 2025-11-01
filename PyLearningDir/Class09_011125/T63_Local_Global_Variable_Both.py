# Local and Global variable

global_var= "Hello World!"

def outer_function():
    def inner_function1():
        message = "Shinest@r!"
        print(message)

    print(global_var)
    inner_function1()

    def inner_function2():
        message1 = "Tejal"
        print(message1)

    inner_function2()

outer_function()
