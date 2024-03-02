class Dot:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Dot{self.x, self.y}"

    def find_distance_to(self, dot: "Dot") -> float:
        dist1 = (self.x - dot.x)
        dist2 = (self.y - dot.y)


        return (dist1 ** 2 + dist2 **2 ) ** 0.5

class spaceDot:
    def __init__(self, x: float, y: float, z: float):
        self.x = x
        self.y = y
        self.z = z

    def find_distance_to(self, dot: "spaceDot") -> float:
        xdist = (self.x - dot.x)
        ydist = (self.y - dot.y)
        zdist = (self.z - dot.z)

        return (xdist**2 + ydist**2 + zdist**2) ** 0.5


def play_wit_dots():
    dot_a = Dot(1, 1)
    dot_b = Dot(4, 5)

    assert dot_a.find_distance_to(dot_b) == 5


if __name__ == "__main__":
    play_wit_dots()

