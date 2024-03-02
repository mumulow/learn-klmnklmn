from typing import Any

# Про SOLID - https://ru.wikipedia.org/wiki/SOLID_(программирование)


class AbstractDot:
    def find_distance_to_dot(self, dot: "AbstractDot"):
        """Метод нахождения расстояния до точки"""
        raise NotImplementedError()

    def ensure_dot_type(self, dot: Any):
        if not isinstance(dot, self.__class__):
            raise TypeError("Могу находить расстояния до точки того же типа!")


class Dot2D(AbstractDot):
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"{self.__class__.__name__}{self.x, self.y}"

    def find_distance_to_dot(self, dot: "Dot2D") -> float:
        self.ensure_dot_type(dot)
        dist1 = self.x - dot.x
        dist2 = self.y - dot.y

        return (dist1 ** 2 + dist2 ** 2) ** 0.5


class Dot3D(AbstractDot):
    def __init__(self, x: float, y: float, z: float):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return f"{self.__class__.__name__}{self.x, self.y, self.z}"

    def find_distance_to_dot(self, dot: "Dot3D") -> float:
        self.ensure_dot_type(dot)
        xdist = self.x - dot.x
        ydist = self.y - dot.y
        zdist = self.z - dot.z

        return (xdist ** 2 + ydist ** 2 + zdist ** 2) ** 0.5


def play_wit_dots():
    dot_a = Dot2D(1, 1)
    dot_b = Dot2D(4, 5)

    assert dot_a.find_distance_to_dot(dot_b) == 5
    dot_c = Dot3D(1, 1, 1)
    dot_d = Dot3D(4, 5, 6)

    assert round(dot_c.find_distance_to_dot(dot_d)) == 7, dot_c.find_distance_to_dot(dot_d)


if __name__ == "__main__":
    play_wit_dots()
