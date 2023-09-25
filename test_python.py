import math


# pi, sqrt, pow, hypot

def test_pi():
    assert 3.1415926 < math.pi < 3.1415927


def test_sqrt():
    assert math.sqrt(4) == 2
    assert math.sqrt(9) == 3
    assert math.sqrt(16) == 4

def test_pow():
    assert math.sqrt(4) == 2
    assert math.sqrt(9) == 3
    assert math.sqrt(16) == 4

def test_hypot():
    assert math.hypot(4,3) == 5
    assert math.hypot(8, 6) == 10
    assert math.hypot(12, 5) == 13
    assert math.hypot(3, 4) == math.sqrt(3**2+4**2)