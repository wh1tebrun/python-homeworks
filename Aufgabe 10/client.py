from dataclasses import dataclass
from getpass import getpass
from sys import argv
from textwrap import wrap
from datetime import datetime, UTC
from prelude import Session


def main():
    session = Session()

    @dataclass
    class Yeet(object):

        def __init__(self, date: float, content: str, author: str, id: int) -> None:
            self.date = date
            self.content = content
            self.author = author
            self.id = id

        def timestamp_to_string(self) -> str:
            date_time = datetime.fromtimestamp(self.date, UTC)

            return date_time.strftime("%d.%m.%Y %H:%M:%S")

    def yeet_from_dict(yeet_as_dict: dict[str, float | str | int]) -> Yeet:

        match yeet_as_dict:

            case {"date": float(), "content": str(), "author": str(), "id": int()}:
                yeet = Yeet(yeet_as_dict["date"], yeet_as_dict["content"],  # type: ignore
                            yeet_as_dict["author"], yeet_as_dict["id"])  # type: ignore

                return yeet

            case _:
                raise KeyError

    def authenticate(session: Session):
        if not session.authenticated:

            isLoggedIn = session.login(getpass("username: "), getpass("password: "))
            if isLoggedIn is False:
                print("Username or password you entered isn’t connected to an account.")
                authenticate(session)

            else:
                print("You have logged in successfully")

    authenticate(session)


if __name__ == "__main__":
    main()
