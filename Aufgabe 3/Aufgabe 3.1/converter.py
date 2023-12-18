import conversion


if __name__ == '__main__':
    source_unit = input("Enter source unit [D / R / G]: ")
    source_value = float(input("Enter source value: "))
    target_unit = input("Enter target unit [D / R / G]: ")

    angle = source_value

    if source_unit == "D":
        angle = conversion.degrees_to_gradians(angle)
    elif source_unit == "R":
        angle = conversion.radians_to_gradians(angle)

    if target_unit == "D":
        angle = conversion.gradians_to_degrees(angle)
    elif target_unit == "R":
        angle = conversion.gradians_to_radians(angle)

    print()
    print(source_value, source_unit, "corresponds to", angle, target_unit)
