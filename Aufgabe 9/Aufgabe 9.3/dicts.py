def find_age(d: dict[str, int], age: int) -> list[str]:
    names = []
    for k, v in d.items():
        if v == age:
            names.append(k)
    return names


def same_age(d: dict[str, int]) -> bool:
    names = []
    for v in d.values():
        names.append(v)

    return len(names) > len(set(names))
