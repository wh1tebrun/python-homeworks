from typing import Optional


# a
def even(xs: list[int]) -> list[tuple[int, bool]]:
    ys = list()
    for x in xs:
        ys += [(x, x % 2 == 0)]
    return ys


# b
def min(xs: list[int]) -> Optional[int]:
    if not xs:
        return None
    minimum = xs[0]
    for x in xs:
        if x < minimum:
            minimum = x
    return minimum


# c
def max(xs: list[int]) -> Optional[int]:
    ys = list()
    for x in xs:
        ys += [-x]
    maximum = min(ys)
    if maximum is None:
        return None
    else:
        return -maximum


if __name__ == "__main__":
    # a
    assert even([1, 3, 2, -6]) == [(1, False), (3, False), (2, True), (-6, True)]

    # b
    assert min([1, 2, 3]) == 1
    assert min([-1, 2, -3]) == -3
    assert min([]) is None

    # c
    assert max([1, 2, 3]) == 3
    assert max([-1, -2, -3]) == -1
    assert max([]) is None
