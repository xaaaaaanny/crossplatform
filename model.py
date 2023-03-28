import math


class CircleModel:
    def __init__(self):
        self._radius = 0

    def set_radius(self, radius):
        self._radius = radius

    def get_radius(self):
        return self._radius

    def get_area(self):
        return math.pi * self._radius ** 2