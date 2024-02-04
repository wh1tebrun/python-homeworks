# Aufgabe 7 (Generatoren) ####################################################

from typing import Callable, Iterator, Iterable, Generator


def drop(xs: Iterable, n: int):
    if n > len(xs):
        return
    
    else:
        xs = xs[n:]
        
    for i in xs:
        yield i


def split[T](xs: Iterable[T], sep: T) -> list[Generator]:
    myList = []
    myList2 = []
    for i in xs:
        if i == sep:
            myList.append(myList2)
            myList2 = []

        else:
            myList2.append(i)

    myList.append(myList2)

    return myList


def apply_pairs(xs: Iterable, f: Callable) -> Generator:
    myList = []
    if len(xs) < 2:
        return

    for index, element in enumerate(xs):
        try:
            result = f(xs[index], xs[index + 1])
            myList.append(result)
        except IndexError:
            pass

    yield myList


# Tests  ######################################################################
if __name__ == "__main__":
    assert list(drop([2, 4, 6, 8, 10, 12], 3)) == [8, 10, 12]
    assert list(drop([True, False, False], 0)) == [True, False, False]
    assert list(drop(["a", "b", "c", "d"], 8)) == []

    assert list(split([1, 5, 3, 4, 9, 3, 5], 3)) == [[1, 5], [4, 9], [5]]
    assert list(split("mississippi", "i")) == [
        ["m"], ["s", "s"], ["s", "s"], ["p", "p"], []
    ]

    sub = lambda x, y: x - y
    eq = lambda x, y: x == y
    assert list(apply_pairs([5, 2, 7, 9, 1], sub)) == [3, -5, -2, 8]
    assert list(list(apply_pairs("abaabbc", eq))) == [False, False, True, False, True, False]
    assert list(apply_pairs([1], sub)) == []
    assert list(apply_pairs([None, None, "", None], eq)) == [True, False, False]