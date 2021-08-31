x0 = 1
container = 0
iterationVal = int(input("Enter number of iterations: "))

for i in range(1,iterationVal + 1):
    container = ((-1)**i) * (1 / (2*i + 1))
    x0  = x0 + container
print(x0)
