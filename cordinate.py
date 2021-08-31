from random import random

x = []
y = []
z = []

for i in range(101):
    x.append(random())
    y.append(random())
    z.append(random())
print("%21s%6s%6s" % ("x", "y", "z"))
for j in range(len(x)):
    print("The cordinates are %6.3f%6.3f%6.3f" % (x[j], y[j], z[j]))
