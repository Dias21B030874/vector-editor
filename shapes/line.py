class Line:
    def __init__(self, start_point, end_point):
        self.start_point = start_point
        self.end_point = end_point

    def __str__(self):
        return f"Line({self.start_point}, {self.end_point})"

    @staticmethod
    def input_attributes():
        from shapes.point import Point
        print("Enter start point:")
        start_x = float(input("  x: "))
        start_y = float(input("  y: "))
        print("Enter end point:")
        end_x = float(input("  x: "))
        end_y = float(input("  y: "))
        return Point(start_x, start_y), Point(end_x, end_y)

    def collides_with(self, other):
        from shapes.square import Square
        from shapes.circle import Circle
        from shapes.point import Point
        if isinstance(other, Point):
            return other.collides_with(self)
        elif isinstance(other, Line):
            return 0
        elif isinstance(other, Circle):
            return other.collides_with(self)
        elif isinstance(other, Square):
            return other.collides_with(self)
        return False
