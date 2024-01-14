import math


def degrees_to_radians(degrees: float) -> float:
    return (degrees % 360) / 180 * math.pi


def radians_to_degrees(radians: float) -> float:
    return (radians % (2 * math.pi)) / math.pi * 180


def degrees_to_gradians(degrees: float) -> float:
    return (degrees % 360) * 400 / 360


def gradians_to_degrees(gradians: float) -> float:
    return (gradians % 400) * 360 / 400


def gradians_to_radians(gradians: float) -> float:
    return degrees_to_radians(gradians_to_degrees(gradians))


def radians_to_gradians(radians: float) -> float:
    return degrees_to_gradians(radians_to_degrees(radians))


if __name__ == '__main__':
    assert math.isclose(degrees_to_radians(45), math.pi / 4)
    assert math.isclose(radians_to_degrees(math.pi), 180)
    assert math.isclose(radians_to_degrees(3 * math.pi), 180)
    assert math.isclose(degrees_to_gradians(270.0), 300.0)
    assert math.isclose(gradians_to_degrees(100.0), 90.0)
    assert math.isclose(gradians_to_degrees(500.0), 90.0)
    assert math.isclose(gradians_to_degrees(-300.0), 90.0)
    assert math.isclose(gradians_to_radians(300), 3 * math.pi / 2)
    assert math.isclose(radians_to_gradians(math.pi / 2), 100)
