from typing import Optional


def head[T](xs: list[T]) -> Optional[T]:
    if not xs:
        return None
    return xs[0]


def tail[T](xs: list[T]) -> Optional[list[T]]:
    if not xs:
        return None
    return xs[1:]


def concat[T](xss: list[list[T]]) -> list[T]:
    outer = list()
    for xs in xss:
        outer += xs
    return outer


def zip[T, U](xs: list[T], ys: list[U]) -> list[tuple[T, U]]:
    out = list()
    for i, x in enumerate(xs):
        if i >= len(ys):
            return out
        else:
            out += [(x, ys[i])]
    return out


def assoc[T, U, V](t: tuple[tuple[T, U], V]) -> tuple[T, tuple[U, V]]:
    (x, y), z = t
    return (x, (y, z))
