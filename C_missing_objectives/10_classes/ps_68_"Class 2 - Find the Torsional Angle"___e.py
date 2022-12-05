"""
You are given four points A, B, C and D in a 3-dimensional Cartesian coordinate system. 
"""


class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return f'({self.x}, {self.y}, {self.z})'


def distance(a, b):
    return ((a.x - b.x) ** 2 + (a.y - b.y) ** 2 + (a.z - b.z) ** 2) ** 0.5


def check_triangle(a, b, c):
    return distance(a, b) + distance(b, c) > distance(a, c)


def check_square(a, b, c, d):
    return check_triangle(a, b, c) and check_triangle(a, b, d) and check_triangle(a, c, d) and check_triangle(b, c, d)


if __name__ == '__main__':
    points = [Point(*map(int, input().split())) for _ in range(4)]
    print('yes' if check_square(*points) else 'no')