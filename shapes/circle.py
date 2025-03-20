class Circle:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    def __str__(self):
        return f"Circle({self.center}, Radius={self.radius})"

    @staticmethod
    def input_attributes():
        from shapes.point import Point
        print("Enter center point:")
        x = float(input("  x: "))
        y = float(input("  y: "))
        radius = float(input("Enter radius: "))
        return Point(x, y), radius

    def collides_with(self, other):
        from shapes.line import Line
        from shapes.square import Square
        from shapes.point import Point
        if isinstance(other, Point):
            distance_sq = (self.center.x - other.x) ** 2 + (self.center.y - other.y) ** 2
            return distance_sq <= self.radius ** 2
        elif isinstance(other, Line):
            return other.collides_with(self)
        elif isinstance(other, Circle):
            distance_sq = (self.center.x - other.center.x) ** 2 + (self.center.y - other.center.y) ** 2
            return distance_sq <= (self.radius + other.radius) ** 2
        elif isinstance(other, Square):
            pass
        return False
