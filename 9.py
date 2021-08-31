y = 0
final = 0

while True:
    x = input("Enter your numbers: ")
    if x == '':
        break
    else:
        y = int(x)
        final = y + final
print(final)
