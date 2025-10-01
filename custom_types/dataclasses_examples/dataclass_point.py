from dataclasses import dataclass


@dataclass
class Point:
    x: float
    y: float

    def is_origin(self) -> bool:
        return self.x == 0 and self.y == 0


p1 = Point(x=3, y=3)
p2 = Point(x=3, y=3)
p3 = Point(x=10, y=0)

is_p1_equal_p2 = p1 == p2
is_p1_equal_p3 = p1 == p3

id_p1 = id(p1)
id_p2 = id(p2)
id_p3 = id(p3)

print(is_p1_equal_p2)
