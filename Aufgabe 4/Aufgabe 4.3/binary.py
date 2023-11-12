def to_num(binärStr: str) -> int:

    if binärStr == "":
        return 0

    dezimalInt = 0
    binärStr = binärStr[::-1]
    x = binärStr[-1]
    binärStr = binärStr[:-1]
    for i in range(len(binärStr)):
        if binärStr[i] == '1':
            dezimalInt += 2 ** i

    if (x == "1"):
        dezimalInt = dezimalInt * -1

    return dezimalInt


assert to_num("01") == 1
assert to_num("11") == -1
assert to_num("111") == -3
assert to_num("0101") == 5
assert to_num("10") == -0
assert to_num("00") == 0
assert to_num("") == 0


def stream_to_nums(stream: str, sep: str) -> list[int]:
    binärStrings = stream.split(sep)
    ergebnis = []

    for binärStr in binärStrings:
        num = to_num(binärStr)
        ergebnis.append(num)

    return ergebnis


assert stream_to_nums("01", "#") == [1]
assert stream_to_nums("01#11", "#") == [1, -1]
assert stream_to_nums("01#11#000", "#") == [1, -1, 0]
assert stream_to_nums("01#11#000#", "#") == [1, -1, 0, 0]
assert stream_to_nums("01#11#000#1111", "#") == [1, -1, 0, -7]
