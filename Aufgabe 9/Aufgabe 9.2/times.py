from dataclasses import dataclass


@dataclass
class Time:
    """
    Datenklasse für Zeitangaben im 24-Stunden-Format

    Attributes:
        hours: Stunden (0 bis 23)
        minutes: Minuten (0 bis 59)
    """

    hours: int = 0
    minutes: int = 0

    def __init__(self, hours: int, minutes: int):
        self.hours = hours % 24
        self.minutes = minutes % 60

    @property
    def __time(self) -> int:
        return self.hours * 60 + self.minutes

    @__time.setter
    def __time(self, value: int):
        self.hours = value // 60
        self.minutes = value % 60

    # Comparison operators
    def __eq__(self, other: "Time") -> bool:
        return self.__time == other.__time

    def __gt__(self, other: "Time") -> bool:
        return self.__time > other.__time

    def __lt__(self, other: "Time") -> bool:
        return self.__time < other.__time

    def __ge__(self, other: "Time") -> bool:
        return self.__time >= other.__time

    def __le__(self, other: "Time") -> bool:
        return self.__time <= other.__time

    # Arithmethic operators
    def __add__(self, other: "Time") -> "Time":
        return Time(self.__time + other.__time // 60, self.__time % 60 + other.__time % 60)

    def __sub__(self, other: "Time") -> "Time":
        return Time(self.__time - other.__time // 60, self.__time % 60 - other.__time % 60)

    # String representation
    def __str__(self) -> str:
        return f"{self.hours:02d}:{self.minutes:02d}"
