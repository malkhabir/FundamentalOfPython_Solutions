side1 = float(input("Enter a value for the length of the first side: "))
side2 = float(input("Enter a value for the length of the second side: "))
side3 = float(input("Enter a value for the length of the third side: "))


if side1**2 == side2**2 + side3**2 or side2**2 == side1**2 + side2**2 or side3**2 == side2**2 + side1**2:
    print("We have a right triangle")
else:
    print("We do not have a right triangle")
