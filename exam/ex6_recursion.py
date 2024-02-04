# Aufgabe 6 (Rekursion) ######################################################

from dataclasses import dataclass
from typing import Optional, Callable, Any


@dataclass
class Node[T]:
    mark: T
    left: 'Tree[T]' = None
    right: 'Tree[T]' = None


type Tree[T] = Optional[Node[T]]  # Trees can be empty.


def filter_tree(f, tree):
    ...


def mirror_tree(tree):
    ...


# Tests  ######################################################################
if __name__ == '__main__':
    example1 = Node("zero",
                    Node("one"),
                    Node("two",
                         Node("three"),
                         Node("four")
                         )
                    )
    assert filter_tree(lambda x: 'e' in x, example1) == ['zero', 'one', 'three']
    assert filter_tree(lambda x: 'o' in x, example1) == ['zero', 'one', 'two', 'four']
    assert filter_tree(lambda _: False, example1) == []
    assert filter_tree(lambda _: True, None) == []

    example2 = Node(0, Node(5, Node(3)), Node(1))
    mirror_tree(example2)
    assert example2 == Node(0, Node(1), Node(5, None, Node(3)))
    mirror_tree(example2)
    assert example2 == Node(0, Node(5, Node(3)), Node(1))
    mirror_tree(example1)
    assert example1 == Node("zero", Node("two", Node("four"), Node("three")), Node("one"))
    mirror_tree(None)  # does nothing