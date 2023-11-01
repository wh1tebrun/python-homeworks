print("Hallo! Denke an einen Superhelden bzw. eine Superheldin aus der Universe X-Men. \nIch versuche, den Charakter zu erraten! \n\nFangen wir an:")
frage1 = ((input("Ist dein Charakter ein Mensch? [Ja/Nein]:")))
frage2 = ((input("Hat dein Charakter Haare? [Ja/Nein]:")))
frage3 = ((input("Hat dein Character Messer in seinen Händen? [Ja/Nein]:")))
frage4 = ((input("Ist dein Charakter weiblich? [Ja/Nein]:")))
frage5 = ((input("Kann dein Character seine Form ändern [Ja/Nein]:")))
frage6 = ((input("Kann dein Charakter Metallobjekte kontrollieren? [Ja/Nein]:")))
frage7 = ((input("Ist dein Character schneller als fast alles? [Ja/Nein]:")))
frage8 = ((input("Ist dein Charakter normalerweise blau? [Ja/Nein]:")))
frage9 = ((input("Kann dein Charakter Gedanken lesen? [Ja/Nein]:")))
frage10 = ((input("Ist dein Character körperlich ziemlich stark? [Ja/Nein]:")))


if frage2 == "Ja" and frage4 == "Ja" and frage5 == "Ja" and frage8 == "Ja" and frage9 == "Nein" and frage7 == "Ja":
    print("Ich hab's! Es ist Mystique")
elif frage1 == "Ja" and frage9 == "Ja" and frage4 == "Nein" and frage5 == "Nein" and frage6 == "Nein" and frage7 == "Nein":
    print("Ich hab's! Es ist Professor X")
elif frage1 == "Ja" and frage2 == "Ja" and frage3 == "Ja" and frage4 == "Nein" and frage7 == "Nein" and frage8 == "Nein":
    print("Ich hab's! Es ist Wolverine")
elif frage1 == "Ja" and frage2 == "Ja" and frage7 == "Ja" and frage4 == "Nein" and frage5 == "Nein" and frage8 == "Nein":
    print("Ich hab's! Es ist Quicksilver")
elif frage1 == "Ja" and frage2 == "Ja" and frage6 == "Ja" and frage4 == "Nein" and frage5 == "Nein" and frage8 == "Nein":
    print("Ich hab's! Es ist Magneto")
elif frage1 == "Ja" and frage5 == "Ja" and frage10 == "Ja" and frage4 == "Nein" and frage7 == "Nein":
    print("Ich hab's! Es ist Beast")
else:
    print("Es tut mir leid, Ich konnte deinen Character nicht erraten.\nDenke an einen anderen Character diesmal")
