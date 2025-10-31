# Q - Create a function which will take the 3 values from the user,
# which are length of the triangle.  side1, side2, side2
# i/p - int side1 == side2 =side3 → isosceles
# o/p = result in string - iso, eq, scalene

#Equilateral
#isosceles
#Scalene

def triangle(side1,side2,side3):
    if side1<=0 and side2 <=0 and side3 <=0:
        return "The triangle is empty"
    elif side1==side2==side3:
        return "eq"
    elif side1==side2 or side1==side3 or side2==side3:
        return "iso"
    else:
        return "Scalene"

side1=int(input("Enter a number for triangle side1: ").strip())
side2=int(input("Enter a number for triangle side2: ").strip())
side3=int(input("Enter a number for triangle side3: ").strip())
print("The Triangle Length is: ",triangle(side1,side2,side3))
