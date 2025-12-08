# User Defined Functions
"""
1. Function without parameter
2. Function with parameters
3. Function with parameters without return
4. Function with parameters with return
5. Function with multiple parameters
6. Function with multiple parameters with return

"""
print("1. Function without parameter")
def func1():
    print("Function without parameter")
    print("--------------------------")
func1()

print("2. Function with parameters")
def func2(test):
    print("Function with parameters: ",test)
    print("--------------------------")
func2("Test")

print("3. Function with parameters without return")
def func3(test1,test2="hello"):
    print("Function with parameters: ",test1,test2)
    print("--------------------------")
func3("Test3")

print("4. Function with multiple parameters")
def func4(test1,test2,test3):
    print("Function with multiple parameters: ",test1,test2,test3)
    print("--------------------------")
func4("Test4",9777,"Test4")

print("5. Function without parameters with return")
def func5():
    return print("Hello")
func5()
print("--------------------------")

print("6. Function with multiple parameters with return")
def func6(test1,test2,test3):
    return print("Hello",test1,test2,test3)
func6("Test6",9797,"Test6")


