class Dot:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Dot{self.x, self.y}"

    def find_distance_to(self, dot: "Dot") -> float:
        return


def play_wit_dots():
    dot_a = Dot(1, 1)
    dot_b = Dot(4, 5)

    assert dot_a.find_distance_to(dot_b) == 5


if __name__ == "__main__":
    play_wit_dots()