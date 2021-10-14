"""
Date: 9/16/21
Author: Patrick Williamson

"""

pi = 3.14

# uses inputed varibales and outputs the answers from the given formula
def getSurfaceArea(r, h):
    surfaceArea = (2 * pi * r * h) + (2 * pi * r ** 2)
    return surfaceArea


def getVolume(r, h):
    volume = pi * r ** 2 * h
    return volume


def getLateralArea(r, h):
    lateralArea = 2 * pi * r * h
    return lateralArea

def getBaseArea(r):
    baseArea = pi*r**2
    return baseArea



# get the input
r = int(input("Radius: "))
h = int(input("Height: "))

#output the formulas

print("Surface Area: "+str(getSurfaceArea(r,h)))
print("Volume: "+str(getVolume(r,h)))
print("Lateral Area: "+str(getLateralArea(r,h)))
print("Base Area: "+str(getBaseArea(r)))