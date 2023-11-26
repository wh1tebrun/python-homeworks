import random


def remove_char(s: str, c: str) -> str:
    index = s.find(c)
    if index == -1:
        return s

    result = s[:index] + s[index + 1:]

    return result


assert remove_char("DAEAB", "A") == "DEAB"
assert remove_char("hallo", "x") == "hallo"


def perfect_chars(inp: str, sol: str) -> str:
    perfect = []
    for index, c in enumerate(inp):
        if c == sol[index]:
            perfect.append(c)
    return "".join(perfect)


assert perfect_chars("ABBBBC", "BBAAAA") == "B"
assert perfect_chars("DABACC", "AAEACD") == "AAC"


def correct_chars(inp: str, sol: str) -> str:

    inp_chars = list(inp)
    sol_chars = list(sol)
    used = set()
    correct = []
    while inp_chars:
        c = inp_chars.pop(0)
        if c in sol_chars and c not in used:
            correct.append(c)
            used.add(sol_chars.pop(sol_chars.index(c)))
    return "".join(correct)


assert correct_chars("ABBDC", "AACCD") == "ADC"
assert correct_chars("AACCD", "ABBDC") == "ACD"


def compare(inp: str, sol: str) -> tuple:
    perfect = perfect_chars(inp, sol)
    correct = correct_chars(inp, sol)

    return tuple((len(perfect), len(correct) - len(perfect)))


assert compare("BAECC", "BAAEC") == (3, 1)
assert compare("ABCDE", "EADCB") == (0, 5)


def game(length: int, symbols: str):
    solution = ''.join(random.choices(symbols, k=length))

    attempts = 0

    while True:
        guess = input("Geben Sie Ihr 5-stelliges Wort ein: ")

        if guess == solution:
            print("Herzlichen Glückwunsch! Sie haben das richtige Wort geraten.")
            break
        else:
            perfect = perfect_chars(guess, solution)
            correct = correct_chars(guess, solution)

            print(f"Richtige Position und Buchstabe: {len(perfect)}")
            print(f"Richtiger Buchstabe an der falschen Position: {len(correct)}")

        attempts += 1

    print(f"Anzahl der Versuche: {attempts}")


game(5, "ABCDE")
