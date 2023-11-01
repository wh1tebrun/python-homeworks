from conversion import radians_to_degrees, degrees_to_radians, degrees_to_gradians, gradians_to_degrees, radians_to_gradians, gradians_to_radians
from math import pi
sourceUnit = ((input("Enter source unit [D / R / G]: ")))
sourceValue = float((input("Enter source value: ")))
targetUnit = ((input("Enter target unit [D / R / G]: ")))


if sourceUnit == "D" and targetUnit == "G":
    if sourceValue > 360 or sourceValue < 0:
        sourceValue %= 360
    print((sourceValue), (sourceUnit), "corresponds to", degrees_to_gradians(sourceValue), (targetUnit))

elif sourceUnit == "R" and targetUnit == "D":
    if sourceValue > 2 * pi or sourceValue < 0:
        sourceValue %= 2 * pi
    print((sourceValue), (sourceUnit), "corresponds to", radians_to_degrees(sourceValue), (targetUnit))

elif sourceUnit == "D" and targetUnit == "R":
    if sourceValue > 360 or sourceValue < 0:
        sourceValue %= 360
    print((sourceValue), (sourceUnit), "corresponds to", degrees_to_radians(sourceValue), (targetUnit))

elif sourceUnit == "G" and targetUnit == "D":
    if sourceValue > 400 or sourceValue < 0:
        sourceValue %= 400
    print((sourceValue), (sourceUnit), "corresponds to", gradians_to_degrees(sourceValue), (targetUnit))

elif sourceUnit == "R" and targetUnit == "G":
    if sourceValue > 2 * pi or sourceValue < 0:
        sourceValue %= 2 * pi
    print((sourceValue), (sourceUnit), "corresponds to", radians_to_gradians(sourceValue), (targetUnit))

elif sourceUnit == "G" and targetUnit == "R":
    if sourceValue > 400 or sourceValue < 0:
        sourceValue %= 400
    print((sourceValue), (sourceUnit), "corresponds to", gradians_to_radians(sourceValue), (targetUnit))
else:
    print(f'{sourceUnit} or {targetUnit} invalid character')
