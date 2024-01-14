print("Hallo! Denke an einen Superhelden bzw. eine Superheldin von Marvel oder DC-Comics \nIch versuche, den Charakter zu erraten! \n\nFangen wir an:")
frage1 = ((input("Ist dein Charakter ein Mensch? [Ja/Nein]:")))
frage2 = ((input("Hat dein Charakter Haare? [Ja/Nein]:")))
frage3 = ((input("Kann dein Charakter fliegen? [Ja/Nein]: ")))
frage4 = ((input("Ist dein Charakter weiblich? [Ja/Nein]:")))
frage5 = ((input("Ist dein Character sehr schnell? [Ja/Nein]:")))
frage6 = ((input("ist dein Charakter rot oder grün angezogen? [Ja/Nein]:")))
frage7 = ((input("Hat dein Charakter Superkräfte? [Ja/Nein]:")))
frage8 = ((input("Hat dein Character Messer in seinen Händen? [Ja/Nein]:")))
frage9 = ((input("Ist dein Character körperlich ziemlich stark? [Ja/Nein]:")))
frage10 = ((input("Kann dein Charakter magische Schilde erschaffen? [Ja/Nein]:")))
frage11 = ((input("Kann dein Charakter sich teleportieren? [Ja/Nein]:")))
frage12 = ((input("Hat dein Charakter magnetische Kräfte? [Ja/Nein]:")))
frage13 = ((input("Ist dein Charakter aus dem DC-Universum? [Ja/Nein]:")))
frage14 = ((input("Hat dein Charakter kybernetische Verbesserungen? [Ja/Nein]:")))
frage15 = ((input("Benutzt dein Charakter sein Auge als Waffe? [Ja/Nein]:")))
frage16 = ((input("Hat dein Charakter tierähnliche Merkmale? [Ja/Nein]:")))


def akinator():
    if frage1 == "Ja":  # ist ein Mensch
        if frage2 == "Ja":  # Hat Haare
            if frage5 == "Ja":  # ist sehr schnell
                if frage6 == "Ja":  # ist rot oder grün
                    return ("The Flash")
                elif frage6 == "Nein":
                    if frage9 == "Ja":  # ist sehr stark
                        return ("Beast")
                    if frage9 == "Nein":
                        if frage11 == "Ja":  # kann teleportieren
                            return ("Nightcrawler")
                        elif frage11 == "Nein":
                            return ("Quicksilver")
            elif frage5 == "Nein":
                if frage7 == "Ja":  # hat superkräfte
                    if frage4 == "Ja":  # ist weiblich
                        return ("Shadowcat")
                    elif frage4 == "Nein":
                        if frage8 == "Ja":  # Messer als Hände
                            return ("Wolverine")
                        elif frage8 == "Nein":
                            if frage10 == "Ja":  # Teleportationsfähigkeit
                                return ("Doctor Strange")
                            elif frage10 == "Nein":
                                if frage12 == "Ja":  # Magnetische Kräfte
                                    return ("Magneto")
                                elif frage12 == "Nein":
                                    if frage14 == "Ja":   # Cyberkinetik?
                                        if frage15 == "Ja":
                                            return ("Bishop")
                                        elif frage15 == "Nein":
                                            return ("Cable")
                                    elif frage14 == "Nein":
                                        if frage15 == "Ja":  # Auge als Waffe
                                            return ("Cyclops")
                                        elif frage15 == "Nein":
                                            if frage16 == "Ja":
                                                return ("Beast")
                                            elif frage16 == "Nein":
                                                return ("Professor X")
                if frage7 == "Nein":  # hat Superkräfte
                    if frage6 == "Ja":  # ist rot oder grün
                        return ("Green Arrow")
                    elif frage6 == "Nein":
                        return ("Batman")
        elif frage2 == "Nein":
            return ("Professor X")
    elif frage1 == "Nein":  # ist kein Mensch
        if frage3 == "Ja":  # kann fliegen
            if frage4 == "Ja":  # ist weiblich
                return ("Wonder Woman")
            elif frage4 == "Nein":
                if frage15 == "Ja":  # benutzt Auge als Waffe
                    return ("Superman")
                elif frage15 == "Nein":
                    return ("Angel")
        elif frage3 == "Nein":
            if frage4 == "Ja":  # ist weiblich
                return ("Mystique")
            elif frage4 == "Nein":
                return ("Aquaman")
    else:
        print("Es tut mir leid, Ich konnte deinen Character nicht erraten.\nDenke an einen anderen Character diesmal")
        return


if akinator() is not None:
    print("Der Charakter an den du denkst ist: " + str(akinator()))
