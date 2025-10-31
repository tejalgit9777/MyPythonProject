# Using Multiple Parameter return something

#step 1
def math_function(a,b):
    return a+b, a-b, a*b, a/b

#step 2
add, sub, mul, div= math_function(10,5)
print("Addition: ",add)
print("Subtraction: ",sub)
print("Multiply: ",mul)
print("Division: ",div)

