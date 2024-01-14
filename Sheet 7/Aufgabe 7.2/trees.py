from dataclasses import dataclass
from typing import Optional


@dataclass
class Node[T]:
    mark: T
    left: Optional["Node[T]"] = None
    right: Optional["Node[T]"] = None


type BTree[T] = Optional[Node[T]]


def contains[T](tree: BTree[T], val: T) -> bool:
    match tree:
        case None:
            return False
        case Node(m, left, right):
            if m == val:
                return True
            return contains(left, val) or contains(right, val)


def leaves[T](tree: BTree[T]) -> list[T]:
    match tree:
        case None:
            return []
        # case Node(m, None, None):
        #     return [m]
        case Node(mark, left, right):
            if left is right is None:
                return [mark]
            else:
                return leaves(left) + leaves(right)


type AST = BTree[int | str]


def evaluate(tree: AST) -> Optional[int]:
    match tree:
        case Node(int(i), None, None):
            return i
        case Node("*" | "+", left, right):
            left = evaluate(left)
            right = evaluate(right)
            if left is None or right is None:
                return None
            if tree.mark == "+":
                return left + right
            else:
                return left * right
        case _:
            return None


def infix_str(tree: AST) -> str:
    match tree:
        case Node(int(i), _, _):
            return str(i)
        case Node(str(s), left, right):
            return f"({infix_str(left)} {s} {infix_str(right)})"
        case _:
            return ""


def prefix_str(tree: AST) -> str:
    match tree:
        case Node(int(i), _, _):
            return str(i)
        case Node(str(s), left, right):
            return f"({s} {prefix_str(left)} {prefix_str(right)})"
        case _:
            return ""


def postfix_str(tree: AST) -> str:
    match tree:
        case Node(int(i), _, _):
            return str(i)
        case Node(str(s), left, right):
            return f"({postfix_str(left)} {postfix_str(right)} {s})"
        case _:
            return ""


def test_contains():
    tree = Node(5, Node(4), Node(1, Node(0), Node(2)))
    assert contains(tree, 5)
    assert contains(tree, 2)
    assert not contains(tree, 3)
    assert not contains(None, 42)


def test_leaves():
    assert leaves(Node(5, Node(4), Node(1, Node(0), Node(2)))) == [4, 0, 2]
    assert leaves(Node(1, Node(2, Node(3, Node(4, Node(5)))))) == [5]
    assert leaves(None) == []


def test_evaluate():
    example = Node("+", Node(4), Node("*", Node("+", Node(1), Node(2)), Node(2)))
    assert evaluate(example) == 10
    example2 = Node("+", Node(4), Node("*", Node("+", Node(1), None), Node(2)))
    assert evaluate(example2) is None
    example3 = Node("+", Node(4), Node("*", Node("-", Node(2), Node(1)), Node(2)))
    assert evaluate(example3) is None


def test_strs():
    example = Node("+", Node(4), Node("*", Node("+", Node(1), Node(2)), Node(2)))
    assert prefix_str(example) == "(+ 4 (* (+ 1 2) 2))"
    assert infix_str(example) == "(4 + ((1 + 2) * 2))"
    assert postfix_str(example) == "(4 ((1 2 +) 2 *) +)"
    assert prefix_str(Node(0)) == infix_str(Node(0)) == postfix_str(Node(0)) == "0"
    assert prefix_str(None) == infix_str(None) == postfix_str(None) == ""


if __name__ == '__main__':
    test_contains()
    test_leaves()
    test_evaluate()
    test_strs()
