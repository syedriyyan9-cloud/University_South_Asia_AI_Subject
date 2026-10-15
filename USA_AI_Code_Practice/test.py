import math

# first question ans
radius = int(input("Enter the radiuse : "))
area = math.pi * radius ** 2
print(f"Area: {round(area, 2)}")

# second ans
circum = 2 * math.pi * radius
print(f"Circumference: {round(circum, 2)}")