from dataclasses import dataclass, InitVar


@dataclass
class Time:
    _hours: InitVar[int]
    _minutes: InitVar[int]

    def __post_init__(self, _hours: int, _minutes: int):
        self.__time = _hours * 60 + _minutes

    @property
    def hours(self) -> int:
        return (self.__time // 60) % 24

    @hours.setter
    def hours(self, hours: int):
        self.__post_init__(hours, self.minutes)

    @property
    def minutes(self) -> int:
        return self.__time % 60

    @minutes.setter
    def minutes(self, minutes: int):
        self.__post_init__(self.hours, minutes)

    def __str__(self) -> str:
        # with f-Strings
        return f'{self.hours:02d}:{self.minutes:02d}'
        # without f-Strings
        h_str = str(self.hours)
        if len(h_str) == 1:
            h_str = "0" + h_str
        h_min = str(self.minutes)
        if len(h_min) == 1:
            h_min = "0" + h_min
        return h_str + ":" + h_min

    def __eq__(self, other: 'Time') -> bool:
        return self.minutes == other.minutes and self.hours == other.hours

    def __lt__(self, other: 'Time') -> bool:
        if self.hours == other.hours:
            return self.minutes < other.minutes
        return self.hours < other.hours

    def __le__(self, other: 'Time') -> bool:
        if self.hours == other.hours:
            return self.minutes <= other.minutes
        return self.hours <= other.hours

    def __add__(self, other: 'Time') -> 'Time':
        return Time(self.hours + other.hours, self.minutes + other.minutes)

    def __sub__(self, other: 'Time') -> 'Time':
        return Time(self.hours - other.hours, self.minutes - other.minutes)
