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

            return date_time.strftime("%d.%m.%Y")

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

    match argv[1]:

        case "yeet":
            content = input("Your message: ")
            session.post("/yee/yeets/add", {"content": content})

        case "like":

            id: int = int(argv[2])
            session.post("/yee/likes/add", {"id": id})

        case "unlike":

            id: int = int(argv[2])
            session.post("/yee/likes/remove", {"id": id})

        case "details":
            id: int = int(argv[2])
            print(session.get(f'/yee/yeets/{id}/likes'))

        case "follow":
            user: str = str(argv[2])
            session.post("/yee/follows/add", {"username": user})

        case "unfollow":
            user: str = str(argv[2])
            session.post("/yee/follows/remove", {"username": user})

        case "latest":
            amount: int = int(argv[2])
            print(session.get(f'/yee/yeets/all/{amount}'))

        case "profile":
            try:
                user: str = str(argv[2])
                print(session.get(f'/yee/users/{user}/yeets'))
                print(session.get(f'/yee/users/{user}/followers'))
                print(session.get(f'/yee/users/{user}/following'))

            except:
                user: str = "et130"
                print(session.get(f'/yee/users/{user}/yeets'))
                print(session.get(f'/yee/users/{user}/followers'))
                print(session.get(f'/yee/users/{user}/following'))

        case "feed":
            dictofMine = (session.get('/yee/users/et130/following'))
            followingOfMine = dictofMine["response"][1:]
            allYeets = session.get(f'/yee/yeets/all/{1000}')
            for i in allYeets["response"]:
                if i["author"] in followingOfMine:
                    print(i)
                    likeNumberDict = session.get(f'/yee/yeets/{i["yeet_id"]}/likes')
                    likeNumber = likeNumberDict["response"]
                    print(f'This yeet has {len(likeNumber)} likes')

        case "search":
            try:
                user: str = argv[2]
                print(session.get(f'/yee/users/{user}/yeets'))

            except:
                content = input("Your content: ")
                allYeets = (session.get(f'/yee/yeets/all/{100000}'))
                allYeets["response"]

                for i in allYeets["response"]:

                    if content.lower() in i["content"].lower():
                        print(i)


if __name__ == "__main__":
    main()
