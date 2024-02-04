# Aufgabe 8 (Funktionale Programmierung) ######################################

from typing import Callable

# sum_0
def sum_0(fs: list[Callable[[float], float]]) -> float:
    return fs[0](0.0) + fs[1](0.0)

# extensionally_equal
def extensionally_equal(f: Callable[[int], int], g: Callable[[int], int], dom: list[int]) -> bool:
    return False not in ([f(x) == g(x) for x in dom])

# map_matrix
def map_matrix(f: Callable[[float], float], m: list[list[float]]) -> list[list[float]]:

    return list(map(lambda row: list(map(f, row)), m))

# Tests  ######################################################################
if __name__ == '__main__':
    f = lambda x: x + 1
    g = lambda x: x**2
    assert sum_0([f, g]) == 1

    f = lambda x: x * 2 - 1
    g = lambda y: y * (4 / 2) - 1
    assert extensionally_equal(f, g, [1, 2, 3, 4, 5])

    example = [[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]]
    assert map_matrix(lambda x: x * 2, example) == [[2, 4, 6], [8, 10, 12]]