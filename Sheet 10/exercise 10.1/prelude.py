from dataclasses import dataclass, field
from os import remove
from typing import Any
from os.path import isfile


from requests import Session as RequestsSession, Response

UNIVERSITY_AUTHENTICATION_SERVER_URL = "https://auth.laurel.informatik.uni-freiburg.de"
SOCIAL_NETWORK_SEVER_URL = "https://courses.laurel.informatik.uni-freiburg.de"

SERVER_ERROR = (
    lambda response: f"whoops, this actually should never happen! please send a message in the chat and include this error in your message:\n{response.status_code}: {response.text}"
)
BAD_REQUEST = (
    lambda message: f"ooh, something was wrong with your request!\nserver says: {message}"
)
TOO_MANY_REQUESTS = "woah, you are sending too many requests to the server!\nwait a little and try again."
METHOD_NOT_ALLOWED = "hoppla, you used the wrong method to access this route!\ndid you maybe tried to `session.get` something that you should `session.post` to, or the other way around?"
NOT_FOUND = f"hmm, this endpoint does not exist!\nsee `{SOCIAL_NETWORK_SEVER_URL}/yee` for a list of all valid endpoints."
UNAUTHORIZED = "uuh, looks like you are not yet authenticated to access the network!\nmake sure `session.authenticated` is `True` before using `session.get` or `session.post`."


@dataclass
class RequestException(Exception):
    status_code: int
    message: str


@dataclass
class Session:
    username: str = field(init=False)

    def __post_init__(self):
        self.__authenticated: bool = False
        self.__session = RequestsSession()
        if isfile(".token"):
            with open(".token", "r") as f:
                token = f.read()
            self.__session.cookies.set("proglang-auth", token.replace("\n", ""))

            response = self.__session.get(f"{SOCIAL_NETWORK_SEVER_URL}/yee/login")
            if "auth.laurel" in response.url or response.status_code != 200:
                remove(".token")
                return

            data = response.json()
            assert "username" in data, SERVER_ERROR(response)
            self.username = data["username"]
            self.__authenticated = True

    def __validate_response(self, response: Response, ignore401: bool = False):
        match response.status_code:
            case 200:
                return
            case 400:
                message = BAD_REQUEST(response.json()["message"])
            case 401 if ignore401:
                return
            case 401:
                message = UNAUTHORIZED
            case 404:
                message = NOT_FOUND
            case 405:
                message = METHOD_NOT_ALLOWED
            case 422:
                details = response.json()["detail"][0]
                message = BAD_REQUEST(
                    f"invalid input `{details['input']} to path parameter `{details['loc'][1]}`."
                    + details["msg"].lower()
                )
            case 429:
                message = TOO_MANY_REQUESTS
            case _:
                message = SERVER_ERROR(response)
        raise RequestException(response.status_code, message)

    def login(self, username: str, password: str) -> bool:
        assert not isfile(
            ".token"
        ), "tried to login, but session is already valid!\ncheck that the `session.authenticated` field is set to `False` before calling `session.login`."

        if "proglang-auth" in self.__session.cookies:
            self.__session.cookies.pop("proglang-auth")

        response = self.__session.post(
            f"{UNIVERSITY_AUTHENTICATION_SERVER_URL}/auth/login?silent=true",
            json={"username": username, "password": password},
        )

        self.__validate_response(response, ignore401=True)

        if response.status_code == 200:
            with open(".token", "x") as f:
                f.write(self.__session.cookies.get("proglang-auth"))

            response = self.__session.get(f"{SOCIAL_NETWORK_SEVER_URL}/yee/login")
            self.__validate_response(response)

            data = response.json()
            assert "username" in data, SERVER_ERROR(response)
            self.username = data["username"]
            self.__authenticated = True
            return True

        return False

    @property
    def authenticated(self) -> bool:
        return self.__authenticated

    def get(self, path: str) -> Any:
        response = self.__session.get(
            f"{SOCIAL_NETWORK_SEVER_URL}{'' if path.startswith('/') else '/'}{path}"
        )
        self.__validate_response(response)
        return response.json()

    def post(self, path: str, data: dict[str, Any]):
        response = self.__session.post(
            f"{SOCIAL_NETWORK_SEVER_URL}{'' if path.startswith('/') else '/'}{path}",
            json=data,
        )
        self.__validate_response(response)
