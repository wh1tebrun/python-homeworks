from math import sqrt
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

s = sqrt(b ** 2 - 4 * a * c)
a2 = a * 2

x1 = (-b + s) / a2
x2 = (-b - s) / a2

print("x1 =", x1)
print("x2 =", x2)
