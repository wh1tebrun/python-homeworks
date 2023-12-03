from enum import Enum
from typing import Union, Optional
from dataclasses import dataclass


def ask(question: str):
    answer = input(f'{question}? [Yes / No]: ')
    match answer:
        case "Yes":
            return True

        case "yes":
            return True

        case "No":
            return False

        case "no":
            return False


class Operator(Enum):
    ADD = 'ADD'
    MUL = 'MUL'


def eval[T](t: tuple[Enum, T, T]) -> Union[str, int, None]:
    operator, element1, element2 = t
    if type(element1) != type(element2):
        return None
    if operator == Operator.ADD and isinstance(element1, (int, str)):
        return element1 + element2
    elif operator == Operator.MUL and isinstance(element1, int):
        return element1 * element2
    else:
        return None


assert eval((Operator.ADD, 2, 5)) == 7
assert eval((Operator.MUL, 2, 5)) == 10
assert eval((Operator.ADD, "2", "5")) == "25"
assert eval((Operator.MUL, "2", "5")) is None


@dataclass
class Cons[T]:
    def __init__(self, head: T, tail: Optional["T"] = None):
        self.head = head
        self.tail = tail


LList = Optional[Cons]

example = Cons(1, Cons(2, None))
assert example.head == 1
assert example.tail == Cons(2, None)
assert example.tail is not None
assert example.tail.head == 2
assert example.tail.tail is None


def tail(xs: LList) -> LList:
    if xs is None or xs.tail is None:
        return None
    return xs.tail


assert tail(None) is None
assert tail(Cons(1, None)) is None
assert tail(Cons("1", Cons("2", None))) == Cons("2", None)
assert tail(Cons("1", Cons("2", Cons("5", None)))) == Cons("2", Cons("5", None))


def len(xs: LList) -> int:
    count = 0
    current = xs

    while current is not None:
        count += 1
        current = current.tail

    return count


assert len(None) == 0
assert len(Cons(True, None)) == 1
assert len(Cons(True, Cons(False, None))) == 2
assert len(Cons(True, Cons(False, Cons(True, None)))) == 3
