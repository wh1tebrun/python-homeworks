from dataclasses import dataclass, InitVar
import string


@dataclass
class User:
    """
    Invariants:
        * len(name) >= 2
        * age >= 13
        * len(password) >= 6
        * digits(password) >= 2
        * uppercase(password) >= 1
    """
    _name: InitVar[str]
    _age: InitVar[int]
    _password: InitVar[str]

    def __post_init__(self, _name: str, _age: int, _password: str):
        assert len(_name) >= 2, "username must be at least 2 characters long"
        assert _age >= 13, "user must be at least 13 years old"
        assert len(_password) >= 6, "password must be at least 6 characters long"
        caps = 0
        digits = 0
        for c in _password:
            if c in string.ascii_uppercase:
                caps += 1
            elif c in string.digits:
                digits += 1
        assert caps >= 1, "password must contain at least one capital letter"
        assert digits >= 2, "password must contain at least two digits"
        self.__name = _name
        self.__age = _age
        self.__password = _password

    @property
    def name(self) -> str:
        return self.__name

    @property
    def age(self) -> int:
        return self.__age

    def login(self, password: str) -> bool:
        return self.__password == password

    def __eq__(self, other: 'User') -> bool:
        return self.name == other.name


@dataclass
class Network:

    def __post_init__(self):
        self.__users: list[User] = []

    def add_user(self, new_user: User) -> bool:
        for user in self.__users:
            if user.name == new_user.name:
                return False
        self.__users.append(new_user)
        return True

    def update_user(self, name: str, password: str, new_user: User) -> bool:
        if new_user.name != name:
            return False
        for user in self.__users:
            if user.name != name or not user.login(password):
                continue
            self.__users.remove(user)
            self.add_user(new_user)
            return True
        return False
