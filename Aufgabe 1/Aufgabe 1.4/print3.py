x = 4047**4047
# Die Zahl x wird definiert, damit man Operationen ausführen kann.
y = 10**4047
# Die Zahl y dient dazu, dass man die letzen 4047 Ziffern von x durch mod finden kann.
s = 10**4043
# Die Zahl s entfernt die überflüssigen Zahlen aus dem Ergebnis von x mod y.
print((x % y) // s)
