from dataclasses import dataclass


@dataclass
class User:
    def __init__(self, name: str, age: int, password: str):
        self.__name = name
        self.__age = age
        self.__password = password

    @property
    def name(self) -> str:
        return self.__name

    @property
    def age(self) -> int:
        return self.__age

    def login(self, p: str) -> bool:
        return self.__password == p

    def __eq__(self, other) -> bool:
        if isinstance(other, User):
            if other.__name == self.__name:
                return True

        return False


@dataclass
class Network:
    users: list[User] = []

    def add_user(self, new_user: User) -> bool:
        for user in self.users:
            if user.__name == new_user.__name:
                return False
        self.users.append(new_user)
        return True

    def update_user(self, name: str, password: str, new_user: User) -> bool:
        for user in self.users:
            if user.__name == name and user.__password == password:
                self.users.remove(user)
                self.users.append(new_user)
                return True
        return False
