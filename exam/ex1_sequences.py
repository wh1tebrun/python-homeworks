# Aufgabe 1 (Sequence) ########################################################

def count_iterations(a: int, b: int) -> int:
    n = 0
    c = a

    def func(x: int, y: int) -> int:

        if x % 2 == 0:
            return x // 2

        else:
            return (2 * y) + y - 1

    while c >= b:
        c = func(c, a)
        n += 1

    return n



# Tests  ######################################################################
if __name__ == '__main__':
    assert count_iterations(7, 6) == 3
    assert count_iterations(3, 2) == 4
    assert count_iterations(13, 9) == 18
    assert count_iterations(13, 10) == 8
    assert count_iterations(3, 4) == 0