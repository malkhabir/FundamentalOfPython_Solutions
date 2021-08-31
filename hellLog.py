m = 1
n = int(input("N = "))
quotient = 0
rest = 0

while True:
    quotien = round(n / 2)
    rest = n % 2

    if rest == 0:
        break
    else:
        n = quotien
        m = m + 1
print("M = %d" % m)
print(quotien)
