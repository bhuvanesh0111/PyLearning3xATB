side1=float(input("Enter the side1: "))
side2=float(input("Enter the side2: "))
side3=float(input("Enter the side3: "))
if side1==side2 and side2==side3:
    print("The triangle is equilateral")
elif side1==side2 or side2==side3 or side1==side3:
    print("The triangle is isosceles")
else:
    print("The triangle is scalene")