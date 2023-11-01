def quadratic(a, b, c, sol):
    delta = (b * b) - (4 * a * c)

    if delta < 0:
        return None
    elif delta == 0:
        return -b / (2 * a)

    if sol:
        if (-b + (delta ** 0.5)) / (2 * a) > (-b - (delta ** 0.5)) / (2 * a):

            return (-b + (delta ** 0.5)) / (2 * a)
        else:
            return (-b - (delta ** 0.5)) / (2 * a)
    else:
        if (-b + (delta ** 0.5)) / (2 * a) < (-b - (delta ** 0.5)) / (2 * a):

            return (-b + (delta ** 0.5)) / (2 * a)
        else:
            return (-b - (delta ** 0.5)) / (2 * a)


print(quadratic(1, 2, 1, True))
