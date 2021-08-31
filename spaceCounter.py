myString = input("Enter a string here: ")
count = 0

for i in myString:
    if i == ' ':
        count = 1 + count
print("This string has %d space(s)" % count)
