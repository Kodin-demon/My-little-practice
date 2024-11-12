import math

radius = float(input("Enter radius of your circle (leave `0´ if none):"))

if radius == 0:
    diameter = float(input("Enter your diameter of your circle:"))
    print(diameter*math.pi)
else:
    print(radius*2*math.pi)