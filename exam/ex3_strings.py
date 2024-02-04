# Aufgabe 3 (Strings) #########################################################

def s1_in_s2(s1: str, s2: str) -> bool:
    start_index = 0

    for char in s1:

        idx = s2.find(char, start_index)
        if idx == -1:
            return False

        else:

            start_index = idx + 1

    return True

def split_text(text: str) -> list:
    myString = ""
    myList = []

    for char in text:

        if char.isalpha():
            if not myString.isalpha():
                myList.append(myString)
                myString = ""
            myString += char

        else:
            if myString.isalpha():
                myList.append(myString)
                myString = ""
            myString += char

    myList.append(myString)

    return myList


# Tests  ######################################################################
if __name__ == "__main__":
    assert s1_in_s2("fn", "function") is True
    assert s1_in_s2("ufnction", "function") is False
    assert s1_in_s2("fnn", "function") is True
    assert s1_in_s2("fcc", "function") is False

    assert split_text("You're a lizard, Harry!") == [
        'You', "'", 're', ' ', 'a', ' ', 'lizard', ', ', 'Harry', '!'
    ]
    assert split_text("Luke! I'm your father!!") == [
        'Luke', '! ', 'I', "'", 'm', ' ', 'your', ' ', 'father', '!!'
    ]
    assert split_text("*Stay away from her, you $!#@!*") == [
        '*', 'Stay', ' ', 'away', ' ', 'from', ' ', 'her', ', ', 'you', ' $!#@!*'
    ]
    assert split_text("hello world") == ["hello", " ", "world"]