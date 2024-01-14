from typing import Generator, Iterator


def collatz(n: int) -> Generator:

    if n > 1:
        yield n

        while True:

            if n > 1:

                match n % 2:
                    case 0:
                        n = n // 2
                        yield n

                    case 1:
                        n = 3 * n + 1
                        yield n

            elif n == 1:
                break

    else:
        return


assert list(collatz(11)) == [
    11, 34, 17, 52, 26, 13, 40,
    20, 10, 5, 16, 8, 4, 2, 1
]
assert list(collatz(0)) == list(collatz(-4)) == []

assert len(list(collatz(97))) == 119


def random(seed: int, a: int, b: int, m: int) -> Generator:
    y = seed
    yield y
    while True:

        y = (a * y + b) % m
        yield y

        if y == seed:
            break


assert list(zip(range(17), random(11, 5, 0, 64))) == list(zip(range(17), [
    11, 55, 19, 31, 27, 7, 35, 47, 43, 23, 51, 63, 59, 39, 3, 15, 11
]))


def chunks(iter: Iterator, n: int) -> Generator[list, None, None]:

    chunk = []

    for i in iter:
        chunk.append(i)

        if len(chunk) == n:
            yield chunk
            chunk = []

    if chunk and n:

        yield chunk

    elif n == 0:
        yield []


assert list(chunks(iter(range(1, 9)), 3)) == [
    [1, 2, 3], [4, 5, 6], [7, 8]
]
assert list(chunks(iter(range(1, 5)), 2)) == [[1, 2], [3, 4]]
assert list(chunks(iter([]), 1)) == []
assert next(chunks(iter([]), 0)) == next(chunks(iter([1, 2]), 0)) == []


def flatten(iter: Iterator[list]) -> Generator:

    for i in iter:
        for item in i:
            yield item


assert list(flatten(iter([[1, 2, 3], [4, 5], [6]]))) == list(range(1, 7))
assert list(flatten(iter([[]]))) == []
