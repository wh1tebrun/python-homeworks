# a
def to_num(bits: str) -> int:
    res = 0
    if len(bits) < 2:
        return res
    sign = bits[0]
    bits = bits[1:]
    for index, bit in enumerate(bits[::-1]):
        res += int(bit) * 2 ** index
    # More efficient alternative
    # for bit in bits:
    #     res = int(bit) + 2 * res
    if sign == "1":
        return -res
    return res


# b
# In dieser Aufgabe durften Sie 'split()' benutzen.
# Wenn Sie split selbst implementieren, ist es ein großer Unterschied, ob Sie split
# für einen Seperator mit Länge 1 oder länger implementieren.
# Es folgt eine Implementierung von split für einen beliebig langen Seperator

def own_split(stream: str, sep: str) -> list[str]:
    if sep == "":
        return [stream]

    sep_len = len(sep)
    skip = 0
    buffer = ""
    out = list()
    is_last_sep = False
    for index, char in enumerate(stream):
        if skip > 0:
            skip -= 1
            continue

        if (char == sep[0]) and (stream[index:index + sep_len] == sep):
            out += [buffer]
            buffer = ""
            skip = sep_len - 1
            is_last_sep = True
        else:
            buffer += char
            is_last_sep = False

    if buffer or is_last_sep:
        out += [buffer]

    return out


def stream_to_nums(stream: str, sep: str) -> list[int]:
    res = list()
    for bits in own_split(stream, sep):
        res += [to_num(bits)]
    return res


if __name__ == "__main__":
    # a
    assert to_num("01") == 1
    assert to_num("11") == -1
    assert to_num("111") == -3
    assert to_num("0101") == 5
    assert to_num("10") == -0
    assert to_num("00") == 0
    assert to_num("") == 0

    # b
    assert stream_to_nums("01", "#") == [1]
    assert stream_to_nums("01#11", "#") == [1, -1]
    assert stream_to_nums("01#11#000", "#") == [1, -1, 0]
    assert stream_to_nums("01#11#000#", "#") == [1, -1, 0, 0]
    assert stream_to_nums("01#11#000#1111", "#") == [1, -1, 0, -7]
