from math import pi


def degrees_to_radians(D):
    R = D * (pi / 180)
    return R


def radians_to_degrees(R):
    D = R / (pi / 180)
    return D


def degrees_to_gradians(D):
    G = D * (200 / 180)
    return G


def gradians_to_degrees(G):
    D = G / (200 / 180)
    return D


def radians_to_gradians(R):
    G = R * (200 / pi)
    return G


def gradians_to_radians(G):
    R = G / (200 / pi)
    return R
