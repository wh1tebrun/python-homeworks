from typing import Optional, Any
from dataclasses import dataclass
from enum import Enum, auto


# A1
def ask(s: str) -> Optional[bool]:
    match input(f"{s}? [Yes / No]: "):
        case "Yes" | "yes":
            return True
        case "No" | "no":
            return False
        case _:
            return None


# A2
class Operator(Enum):
    ADD = auto()
    MUL = auto()


def eval[T: (int, str)](t: tuple[Operator, T, T]) -> Optional[T]:
    match t:
        case (Operator.ADD, x, y):
            return x + y
        case (Operator.MUL, int(i), int(j)):
            return i * j
        case _:
            return None


# A3
@dataclass
class Cons[T]:
    head: T
    tail: Optional["Cons[T]"] = None
    # tail: "LList[T]"


type LList[T] = Optional[Cons[T]]

if __name__ == '__main__':
    example = Cons(1, Cons(2, None))
    assert example.head == 1
    assert example.tail == Cons(2, None)
    assert example.tail
    assert example.tail.head == (2)
    assert example.tail.tail is None


def tail[T](xs: LList[T]) -> LList[T]:
    match xs:
        case None:
            return None
        case Cons(_, tail):
            return tail


if __name__ == '__main__':
    assert tail(None) is None
    assert tail(Cons(1, None)) is None
    assert tail(Cons("1", Cons("2", None))) == Cons("2", None)
    assert tail(Cons("1", Cons("2", Cons("5", None)))) == Cons("2", Cons("5", None))


def len(xs: LList[Any]) -> int:
    match xs:
        case None:
            return 0
        case Cons(_, tail):
            return 1 + len(tail)


if __name__ == '__main__':
    assert len(None) == 0
    assert len(Cons(True, None)) == 1
    assert len(Cons(True, Cons(False, None))) == 2
    assert len(Cons(True, Cons(False, Cons(True, None)))) == 3
