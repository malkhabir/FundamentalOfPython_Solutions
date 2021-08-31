initSalary = 30000
balance = initSalary
rate = 2
#term  = int(input("Enter the number of year: "))
#initSalary = int(input("Enter the starting salary: "))
print("Term             Salary")
for i in range(10):
    term = i
    yearTerm = 1 + term
    initSalary = balance
    balance = initSalary * (rate/100) + initSalary
    print("Year %-9d %11.3f" % (yearTerm, balance))
