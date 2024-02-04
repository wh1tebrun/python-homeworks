from dataclasses import dataclass, InitVar
from typing import Callable, Iterable, Generator, Optional


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


network = {
    1: {"Hauptbahnhof", "Paduaallee"},
    2: {"Hauptbahnhof", "Stadttheater"},
    3: {"Am Lindenw¨aldle", "Hauptbahnhof"},
    5: {"Europaplatz", "Stadttheater"},
}


def lines(network: dict, station: str) -> set:

    foundDict = dict()

    for myLine, mySet in network.items():
        for myStation in mySet:
            if myStation not in foundDict:
                foundDict[myStation] = set()
                foundDict[myStation].add(myLine)

            elif myStation in foundDict:
                foundDict[myStation].add(myLine)

    return foundDict[station]


def invert(network: dict) -> dict:

    foundDict = dict()

    for myLine, mySet in network.items():
        for myStation in mySet:
            if myStation not in foundDict:
                foundDict[myStation] = set()
                foundDict[myStation].add(myLine)

            elif myStation in foundDict:
                foundDict[myStation].add(myLine)

    return foundDict


print(lines(network, "Hauptbahnhof"))
print(invert(network))


def add_line(network: dict, stations: set[str]):
    myDict = dict()
    for myLine, mySet in network.items():
        for myStation in mySet:

            if myStation not in myDict:
                myDict[myLine] = set()
                myDict[myLine].add(myStation)

            elif myStation in myDict:
                myDict[myLine].add(myStation)

    for index, value in enumerate(network):
        foundNumber = 0
        if index + 1 == value:
            pass

        else:
            foundNumber = index + 1
            myDict[foundNumber] = stations
            break

    network = myDict

    return network


print(add_line(network, {"Technische Fakult¨at", "Hauptbahnhof",
                         "Stadttheater", "Europaplatz", "Hornusstraße", }
               ))


def s1_in_s2(s1: str, s2: str) -> bool:
    start_index = 0

    for char in s1:

        idx = s2.find(char, start_index)
        if idx == -1:
            return False

        else:

            start_index = idx + 1

    return True


print(s1_in_s2("fn", "function"))
print(s1_in_s2("ufnction", "function")
      )
print(s1_in_s2("fnn", "function"))
print(s1_in_s2("fcc", "function"))


def split_text(text: str) -> list:
    myString = ""
    myList = []

    for char in text:

        if char.isalpha():
            if not myString.isalpha():
                myList.append(myString)
                myString = ""
            myString += char

        else:
            if myString.isalpha():
                myList.append(myString)
                myString = ""
            myString += char

    myList.append(myString)

    return myList


print(split_text("*Stay away from her, you $!#@!*"))
print(split_text("Luke! I'm your father!!")
      )
print(split_text("You're a lizard, Harry!")
      )


# Zustandsautomat


@dataclass
class Vehicle:

    _seats: InitVar[int]
    _hp: InitVar[int]
    _ccm: InitVar[int]
    _weight: InitVar[int]

    def __post_init__(self, _seats, _hp, _ccm, _weight):

        assert 10 > _seats > 0
        assert _hp > 0
        assert _ccm > 0
        assert _weight > 0

        self.__seats = _seats
        self.__hp = _seats
        self.__ccm = _seats
        self.__weight = _weight

    def fun_factor(self):
        return 10 * self.__hp * self.__ccm / self.__weight

    def __gt__(self, other):
        return self.fun_factor() > other.fun_factor()


@dataclass
class Car(Vehicle):

    _spoiler: InitVar[bool]

    def __post_init__(self, _seats, _hp, _ccm, _weight, _spoiler):
        super().__post_init__(_seats, _hp, _ccm, _weight)

        self.__spoiler = _spoiler

    def fun_factor(self, _spoiler: bool):
        if _spoiler:
            return super().fun_factor() + 0.2

        else:
            return super().fun_factor()


@dataclass
class Motorcycle(Vehicle):

    _sidecar: InitVar[bool]

    def __post_init__(self, _seats, _hp, _ccm, _weight, _sidecar):
        super().__post_init__(_seats, _hp, _ccm, _weight)
        if not _sidecar:

            assert self.__seats == 1 or self.__seats == 2

        else:
            assert self.__seats == 2 or self.__seats == 3

        self.__sidecar = _sidecar

    def fun_factor(self):

        if not self.__sidecar:
            return (super().fun_factor() * 3)

        else:
            return (super().fun_factor() * 2.4)


# Recursion

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


print(list(split([1, 5, 3, 4, 9, 3, 5], 3)))
print(list(split("mississippi", "i")))


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


if __name__ == "__main__":
    sub = lambda x, y: x - y
    eq = lambda x, y: x == y
    print(list(apply_pairs([5, 2, 7, 9, 1], sub)))
    print(list(apply_pairs("abaabbc", eq)))
    print(list(apply_pairs([1], sub)))


def sum_0(fs: list[Callable[[float], float]]) -> float:
    return fs[0](0.0) + fs[1](0.0)


def extensionally_equal(f: Callable[[int], int], g: Callable[[int], int], dom: list[int]) -> bool:
    return False not in ([f(x) == g(x) for x in dom])


f = lambda x: x * 2 - 1
g = lambda y: y * (4 / 2) - 1
print(extensionally_equal(f, g, [1, 2, 3, 4, 5]))


def map_matrix(f: Callable[[float], float], m: list[list[float]]) -> list[list[float]]:

    return list(map(lambda row: list(map(f, row)), m))


example = [[1, 2, 3], [4, 5, 6]]
print(map_matrix(lambda x: x * 2, example))
