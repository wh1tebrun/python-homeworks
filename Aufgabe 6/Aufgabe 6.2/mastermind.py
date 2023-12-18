import random


def remove_char(string: str, c: str) -> str:
    for i, s in enumerate(string):
        if s == c:
            return string[:i] + string[i + 1:]
    return string


def perfect_chars(inp: str, sol: str) -> str:
    chars = ""
    for c, s in zip(inp, sol):
        if c == s:
            chars = chars + c
    return chars


def correct_chars(inp: str, sol: str) -> str:
    res = ""
    for c in inp:
        if c in sol:
            res += c
            sol = remove_char(sol, c)
    return res


def compare(inp: str, sol: str) -> tuple[int, int]:
    perfect = len(perfect_chars(inp, sol))
    correct = len(correct_chars(inp, sol))
    return perfect, correct - perfect


def compare_alt(inp: str, sol: str) -> tuple[int, int]:
    perfect = perfect_chars(inp, sol)
    for c in perfect:
        sol = remove_char(sol, c)
        inp = remove_char(inp, c)
    correct = correct_chars(inp, sol)
    return len(perfect), len(correct)


def game(length: int, symbols: str):
    solution = "".join(random.choices(symbols, k=length))
    print("Länge:", length, "Zeichen:", symbols)
    result = (0, 0)
    while result != (length, 0):
        c = input()
        if len(c) != length:
            print("Try again!")
            continue
        result = compare(c, solution)
        print("Antwort:", result[0] * "X" + result[1] * "-")


if __name__ == '__main__':
    game(5, "ABCDE")
