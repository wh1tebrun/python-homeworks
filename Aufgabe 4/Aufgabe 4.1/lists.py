from typing import Optional


def even(numbers: list[int]) -> list[tuple[int, bool]]:
    result = []
    for num in numbers:
        isEven = num % 2 == 0
        result.append((num, isEven))
    return result


numbersList = [1, 3, 2, -6]
print(even(numbersList))


def min(numbers: list[int]) -> Optional[int]:
    if len(numbers) == 0:
        return None

    else:
        dieKleinsteZahl = numbers[0]
        for n in numbers:

            if dieKleinsteZahl > n:
                dieKleinsteZahl = n

        return dieKleinsteZahl


def max(numbers: list[int]) -> Optional[int]:
    if len(numbers) == 0:
        return None

    else:
        i = 0
        while i < len(numbers):
            numbers[i] = numbers[i] * -1
            i += 1

        x = -1 * min(numbers)

        return x


assert min([1, 2, 3]) == 1
assert min([-1, 2, -3]) == -3
assert min([]) is None
assert max([1, 2, 3]) == 3
assert max([-1, -2, -3]) == -1
assert max([]) is None
