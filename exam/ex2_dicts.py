# Aufgabe 2 (Dictionaries und Sets) ###########################################


def lines(network: dict, station: str) -> set:

    foundDict = dict()

    for myLine, mySet in network.items():
        for myStation in mySet:
            if myStation not in foundDict:
                foundDict[myStation] = set()
                foundDict[myStation].add(myLine)

            elif myStation in foundDict:
                foundDict[myStation].add(myLine)

    return foundDict[station]


def invert(network: dict) -> dict:

    foundDict = dict()

    for myLine, mySet in network.items():
        for myStation in mySet:
            if myStation not in foundDict:
                foundDict[myStation] = set()
                foundDict[myStation].add(myLine)

            elif myStation in foundDict:
                foundDict[myStation].add(myLine)

    return foundDict


def add_line(network: dict, stations: set[str]):
    myDict = dict()
    for myLine, mySet in network.items():
        for myStation in mySet:

            if myStation not in myDict:
                myDict[myLine] = set()
                myDict[myLine].add(myStation)

            elif myStation in myDict:
                myDict[myLine].add(myStation)

    for index, value in enumerate(network):
        foundNumber = 0
        if index + 1 == value:
            pass

        else:
            foundNumber = index + 1
            myDict[foundNumber] = stations
            break

    network = myDict

    return network



# Tests  ######################################################################
if __name__ == "__main__":
    example = {
        1: {"Hauptbahnhof", "Paduaallee", "Stadttheater"},
        2: {"Hauptbahnhof", "Stadttheater", "Hornusstraße", "Johanneskirche"},
        3: {"Am Lindenwäldle", "Hauptbahnhof", "Stadttheater", "Johanneskirche"},
        5: {"Europaplatz", "Stadttheater", "Am Lindenwäldle"},
    }

    assert lines(example, "Hauptbahnhof") == {1, 2, 3}
    assert lines(example, "Europaplatz") == {5}
    assert lines(example, "Paris") == set()

    assert invert(example) == {'Stadttheater': {1, 2, 3, 5},
                               'Hauptbahnhof': {1, 2, 3},
                               'Paduaallee': {1},
                               'Johanneskirche': {2, 3},
                               'Hornusstraße': {2},
                               'Am Lindenwäldle': {3, 5},
                               'Europaplatz': {5}}

    add_line(
        example,
        {
            "Technische Fakultät",
            "Hauptbahnhof",
            "Stadttheater",
            "Europaplatz",
            "Hornusstraße",
        },
    )
    assert example[4] == {
        "Technische Fakultät",
        "Hauptbahnhof",
        "Stadttheater",
        "Europaplatz",
        "Hornusstraße",
    }

    add_line(example, {"nowhere"})
    assert example[6] == {"nowhere"}
