a = float(input("Enter length of first side: "))
b = float(input("Enter length of second side: "))
c = float(input("Enter length of third side: "))

if a == b == c:
    print("The triangle is equilateral.")
elif a == b or b == c or a == c:
    print("The triangle is isosceles.")
else:
    print("The triangle is scalene.")
