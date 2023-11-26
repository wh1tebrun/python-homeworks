from typing import Optional


def head[T](xs: list[T]) -> Optional[T]:
    if len(xs) != 0:
        return xs[0]
    return None


def tail[T](xs: list[T]) -> Optional[list[T]]:
    if len(xs) != 0:
        return xs[1:]
    return None


def concat[T](xss: list[list[T]]) -> Optional[list[T]]:

    if len(xss) != 0:
        concatenated = []
        for xs in xss:
            concatenated += xs
        return concatenated
    return None


def zip[T](xs: list[T], ys: list[T]) -> Optional[list[tuple[T]]]:
    paired = []
    len_x = len(xs)
    len_y = len(ys)
    if len_x == 0 or len_y == 0:
        return paired

    for index, y in enumerate(ys):
        if len_x == index:
            break
        paired.append((xs[index], y))

    return paired


def assoc[T](t: tuple[tuple[T], T]) -> tuple[tuple[T], T]:
    return (t[0][0], (t[0][1], t[1]))
