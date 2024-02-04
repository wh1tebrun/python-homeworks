# Aufgabe 5 (Dataclasses) #####################################################

from dataclasses import dataclass, InitVar

# (a) Vehicle
@dataclass
class Vehicle:

    _seats: InitVar[int]
    _hp: InitVar[int]
    _ccm: InitVar[int]
    _weight: InitVar[int]

    def __post_init__(self, _seats, _hp, _ccm, _weight):

        assert 10 > _seats > 0
        assert _hp > 0
        assert _ccm > 0
        assert _weight > 0

        self.__seats = _seats
        self.__hp = _seats
        self.__ccm = _seats
        self.__weight = _weight

    def fun_factor(self):
        return 10 * self.__hp * self.__ccm / self.__weight

    def __gt__(self, other):
        return self.fun_factor() > other.fun_factor()

# (b) Car
@dataclass
class Car(Vehicle):

    _spoiler: InitVar[bool]

    def __post_init__(self, _seats, _hp, _ccm, _weight, _spoiler):
        super().__post_init__(_seats, _hp, _ccm, _weight)

        self.__spoiler = _spoiler

    def fun_factor(self, _spoiler: bool):
        if _spoiler:
            return super().fun_factor() + 0.2

        else:
            return super().fun_factor()

# (c) Motorcycle
@dataclass
class Motorcycle(Vehicle):

    _sidecar: InitVar[bool]

    def __post_init__(self, _seats, _hp, _ccm, _weight, _sidecar):
        super().__post_init__(_seats, _hp, _ccm, _weight)
        if not _sidecar:

            assert self.__seats == 1 or self.__seats == 2

        else:
            assert self.__seats == 2 or self.__seats == 3

        self.__sidecar = _sidecar

    def fun_factor(self):

        if not self.__sidecar:
            return (super().fun_factor() * 3)

        else:
            return (super().fun_factor() * 2.4)