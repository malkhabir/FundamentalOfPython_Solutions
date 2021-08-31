
ans = 1
while True:
    num = int(input("Enter number: "))
    if num < 0:
        print("Please enter a positive number that is more than 0")
    elif num == 0:
        print("Enter a number bigger than 0: ")
    else:
        while num >= 1:
            ans = ans * num
            num = num - 1
        print(ans)
        break
