from math import sqrt
a = float((input("a: ")))
b = float((input("b: ")))
c = float((input("c: ")))

delta = (b * b) - (4 * a * c)

x1 = ((-b + sqrt(delta)) / (2 * a))
x2 = ((-b - sqrt(delta)) / (2 * a))
print("x1:", x1)
print("x2:", x2)
