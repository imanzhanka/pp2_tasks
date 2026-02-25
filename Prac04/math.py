import math

# 1
degree = float(input("Input degree: "))
radian = degree * (math.pi / 180)
print(f"Output radian: {radian:.6f}")


#2 

h  = float(input("\nHeight: "))
b1 = float(input("Base, first value: "))
b2 = float(input("Base, second value: "))
trapezoid_area = ((b1 + b2) / 2) * h
print(f"Area of trapezoid: {trapezoid_area}")


# 3
n = int(input("\nInput number of sides: "))
s = float(input("Input the length of a side: "))
polygon_area = (s ** 2 * n) / (4 * math.tan(math.pi / n))
print(f"The area of the polygon is: {polygon_area:.0f}")

# 4 Area of a Parallelogram
base   = float(input("\nLength of base: "))
height = float(input("Height of parallelogram: "))
parallelogram_area = base * height
print(f"Area of parallelogram: {parallelogram_area}")