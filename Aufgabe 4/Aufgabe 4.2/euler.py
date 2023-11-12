import math
n = int(input("Geben Sie eine nicht negative Zahl ein! : "))


def fac(zahl):
    fak = 1
    while (zahl > 1):
        fak *= zahl
        zahl -= 1
    return fak


def approx_e(n):
    circa_e = 1
    for x in range(1, n + 1):
        circa_e += 1 / fac(x)
    return circa_e


if n >= 0:
    print(approx_e(n))

else:
    print("Sie haben eine negative Zahl eingegeben!")


assert approx_e(0) == 1
assert approx_e(1) == 2
assert math.isclose(approx_e(2), 2.5)
assert math.isclose(approx_e(3), 8 / 3)
assert math.isclose(approx_e(100), math.e)
