# Aufgabe 4 (Zustandsautomat) ######################################

from dataclasses import dataclass
from typing import Callable
from enum import Enum, auto


@dataclass
class Automaton[Q]:
    E: frozenset[str]               # Eingabealphabet
    delta: Callable[[Q, str], Q]    # Übergangsfunktion
    q0: Q                           # Startzustand
    F: frozenset[Q]                 # Akzeptierende Zustände

    def accept(self, input: str) -> bool:
        state = self.q0
        for c in input:
            state = self.delta(state, c)
        return state in self.F


# State


def delta(state, input):
    ...


def automaton():
    ...

# Tests  ######################################################################


if __name__ == '__main__':
    a = automaton()
    assert a.accept("")
    assert a.accept("abbbbbba")
    assert a.accept("aabaabbba")
    assert not a.accept("aabaabaab")