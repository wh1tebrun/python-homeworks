from typing import Optional, Union
from dataclasses import dataclass


@dataclass
class Node[T]:
    mark: T
    left: Optional['Node[T]'] = None
    right: Optional['Node[T]'] = None


type BTree[T] = Optional[Node[T]]


def contains[T](tree: BTree[T], val: int) -> bool:
    if tree is None:
        return False
    elif tree.mark == val:
        return True
    else:
        return contains(tree.left, val) or contains(tree.right, val)


tree = Node(5, Node(4), Node(1, Node(0), Node(2)))
assert contains(tree, 5)
assert contains(tree, 2)
assert not contains(tree, 3)
assert not contains(None, 42)


def leaves[T](tree: BTree[T]) -> list[T]:
    if tree is None:
        return []
    elif tree.left is None and tree.right is None:
        return [tree.mark]
    else:
        return leaves(tree.left) + leaves(tree.right)


assert leaves(Node(5, Node(4), Node(1, Node(0), Node(2)))) == [4, 0, 2]
assert leaves(Node(1, Node(2, Node(3, Node(4, Node(5)))))) == [5]
assert leaves(None) == []


def evaluate(tree: BTree[Union[int, str]]) -> Optional[int]:

    if tree is None:
        return None
    elif isinstance(tree.mark, int):
        return tree.mark
    elif tree.mark == "+":
        return evaluate(tree.left) + evaluate(tree.right)
    elif tree.mark == "*":
        return evaluate(tree.left) * evaluate(tree.right)
    else:
        return None


example = Node("+", Node(4), Node("*", Node("+", Node(1), Node(2)), Node(2)))
assert evaluate(example) == 10

example2 = Node("+", Node(4), Node("*", Node("+", Node(1), None), Node(2)))
assert evaluate(example2) is None

example3 = Node("+", Node(4), Node("*", Node("-", Node(2), Node(1)), Node(2)))
assert evaluate(example3) is None
