import math

radius = (float(input("Please enter the radius: ")))

volume = 4/3*(math.pi*pow(radius, 3))

surface = 4*(math.pi*pow(radius, 2))

print("The total volume is {:.2f}".format(volume), "and the surface area is {:.2f}".format(surface))

