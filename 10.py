purchasePrice = 10000
downPayment =  0.1 * (purchasePrice)
#int(input("Enter the investment amount: "))
rate = 12
monthlyPayment = (0.05 * purchasePrice) - downPayment
balance = purchasePrice - downPayment
startingBalance = balance - monthlyPayment
i = 0

print("%7s%17s%18s%18s%15s%14s" %
("Month", "Starting", "Mthly Pymt", "Interest", "Principal", "Ending Bal"))

while balance != 0:
    i = i + 1
    #interest = ((endBal * ((rate/100))))
    balance = balance + monthlyPayment
    startingBalance = balance - monthlyPayment
    interest = balance * (rate/1200)
    principal = -(monthlyPayment + interest)
    print("%4d%19.2f%16.2f%18.2f%15.2f%14.2f" %
    (i, startingBalance, monthlyPayment, interest, principal, balance))

print("You paid this loan in %d months" % i)
