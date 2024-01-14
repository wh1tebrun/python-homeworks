import math


def fac(n: int) -> int:
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res


def approx_e(n: int) -> float:
    res = 0
    for i in range(0, n + 1):
        res += 1 / (fac(i))
    return res


if __name__ == "__main__":
    assert approx_e(0) == 1
    assert approx_e(1) == 2
    assert math.isclose(approx_e(2), 2.5)
    assert math.isclose(approx_e(3), 8 / 3)
    assert math.isclose(approx_e(100), math.e)
