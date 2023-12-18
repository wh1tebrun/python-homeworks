from math import sqrt
from typing import Optional


def quadratic(a: float, b: float, c: float, sol: bool) -> Optional[float]:
    if a == 0:
        if b == c == 0:
            return 0
        elif b == 0:
            return None
        else:
            return -c / b
    det = b ** 2 - 4 * a * c
    if det < 0:
        return None
    x1 = (-b + sqrt(det)) / (2 * a)
    x2 = (-b - sqrt(det)) / (2 * a)
    if sol == (x1 > x2):
        return x1
    return x2


if __name__ == '__main__':
    assert quadratic(1, -2, -3, False) == -1.0
    assert quadratic(1, -2, -3, True) == 3.0
    assert quadratic(-1, -2, 3, False) == -3.0
    assert quadratic(-1, -2, 3, True) == 1.0
    assert quadratic(1, 2, 3, True) is None
    assert quadratic(1, 2, 3, False) is None
    assert quadratic(0, 1, 2, True) == quadratic(0, 1, 2, False) == -2.0
    assert quadratic(0, 0, 0, True) == quadratic(0, 0, 0, False) == 0
    # every other number is also a solution for 0x^2+0x+0=0. We chose 0.
    assert quadratic(1, 2, 1, True) == quadratic(1, 2, 1, False) == -1.0
