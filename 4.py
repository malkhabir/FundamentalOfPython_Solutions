initialHeight = 10 #int(input("Enter the initial height: "))
numberOfBounces = 2 #int(input("Enter the number of bounces: "))
bounceIndex = 0.6 #float(input("Enter the bounce index: "))
container = 0
finalDistance = 0
newBounce = 0
i = 0

for i in range(numberOfBounces):

    container = initialHeight

    newBounce = (bounceIndex) * initialHeight

    container = container + newBounce

    finalDistance = finalDistance + container

    initialHeight = newBounce

print(finalDistance)
