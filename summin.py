lower = int(input("Enter the lower bound: "))

upper = int(input("Enter the upper bound: "))

theSum = 0

for count in range(lower, upper + 1):
    theSum = theSum + count

print(theSum)
