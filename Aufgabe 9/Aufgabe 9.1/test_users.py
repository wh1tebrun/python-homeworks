from users import *
from typing import Optional


@dataclass
class Raises:
    err: type[Exception]
    msg: Optional[str] = None

    def __enter__(self): pass

    def __exit__(self, *args):
        _, err, _ = args
        if isinstance(err, self.err):
            if self.msg:
                return err.args[0] == self.msg
            return True
        else:
            raise AssertionError(f"Test case should raise an exception of type {self.err} but didn't")


def test_user():
    u1 = User("Marco", 26, "Passwort123")
    assert u1.name == "Marco"
    assert u1.age == 26
    assert u1.login("Passwort123") and not u1.login("passwort123")
    with Raises(AttributeError):  # this checks if the expression below raises the given error
        u1.__password
    with Raises(AssertionError):
        User("", 26, "Passwort123")
    with Raises(AssertionError):
        User("Marco", 5, "Passwort123")
    with Raises(AssertionError):
        User("Marco", 26, "passwort123")
    with Raises(AssertionError):
        User("Marco", 26, "P123")
    with Raises(AssertionError):
        User("Marco", 26, "Passwort")
    assert User("Tina", 24, "Passwort1234") == User("Tina", 45, "IOVE3923d393DJ")
    assert not User("Tim", 24, "Passwort123") == User("Tina", 24, "Passwort123")


if __name__ == '__main__':
    test_user()
