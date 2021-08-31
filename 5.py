startingPop = int(input("Enter the initial pop size: "))
rateofGrowth = int(input("Enter the rate of growth: "))
takenTimeTo = int(input("Enter the growth period: "))
FinalTime = int(input("Enter the time you allow the organism to growth for: "))
endingPop = 0


for i in range(int(FinalTime/takenTimeTo)):
    container = startingPop * rateofGrowth
    endingPop = container + endingPop
print("We have %d organism" % endingPop)
