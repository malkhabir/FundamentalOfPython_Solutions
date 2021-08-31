larger = int(input("Enter the larger number: "))
smaller = int(input("ENter the smaller number: "))
remainder = 1
while remainder != 0:
    remainder = larger % smaller
    larger = smaller
    smaller = remainder
print(larger)
