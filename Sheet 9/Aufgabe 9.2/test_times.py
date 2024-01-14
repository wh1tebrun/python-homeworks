from times import Time


def test_time():
    t1 = Time(12, 23)
    assert t1.hours == 12 and t1.minutes == 23
    t2 = Time(24, 3)
    assert t2.hours == 0 and t2.minutes == 3
    t3 = Time(49, 61)
    assert t3.hours == 2 and t3.minutes == 1
    t4 = Time(-13, 61)
    assert t4.hours == 12 and t4.minutes == 1
    t5 = Time(4, 49)
    assert t5.hours == 4 and t5.minutes == 49


def test_compare():
    assert Time(5, 35) == Time(5, 35)
    assert not Time(4, 29) == Time(3, 29)
    assert Time(38, 45) == Time(14, 45)
    assert Time(-15, 105) == Time(10, 45)

    assert Time(5, 42) > Time(4, 42) and not Time(5, 42) < Time(4, 42)
    assert Time(5, 42) > Time(28, 42) and not Time(5, 42) < Time(28, 42)
    assert Time(5, 32) > Time(5, 30) and not Time(5, 32) < Time(5, 30)
    assert not (Time(13, 43) > Time(13, 43)) and not (Time(13, 43) < Time(13, 43))

    assert Time(3, 32) <= Time(8, 54) and not Time(3, 32) >= Time(8, 54)
    assert Time(5, 42) <= Time(5, 42) and Time(5, 42) >= Time(5, 42)


def test_arithmetic():
    assert Time(1, 23) + Time(0, 56) == Time(2, 19)
    assert Time(12, 34) + Time(12, 32) == Time(1, 6)
    assert Time(12, 34) + Time(45, 67) == Time(10, 41)

    assert Time(10, 34) - Time(1, 23) == Time(9, 11)
    assert Time(10, 34) - Time(12, 44) == Time(21, 50)


def test_str():
    assert str(Time(14, 45)) == "14:45"
    assert str(Time(0, 0)) == "00:00"
    assert str(Time(4, 5)) == "04:05"
    assert str(Time(-15, 104)) == "10:44"


if __name__ == '__main__':
    test_time()
    test_compare()
    test_arithmetic()
    test_str()
