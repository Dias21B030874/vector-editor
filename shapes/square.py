class Square:
    def __init__(self, top_left, side_length):
        self.top_left = top_left
        self.side_length = side_length

    def __str__(self):
        return f"Square({self.top_left}, Side={self.side_length})"

    @staticmethod
    def input_attributes():
        from shapes.point import Point
        print("Enter top-left point:")
        x = float(input("  x: "))
        y = float(input("  y: "))
        side_length = float(input("Enter side length: "))
        return Point(x, y), side_length

    def collides_with(self, other):
        from shapes.line import Line
        from shapes.circle import Circle
        from shapes.point import Point
        if isinstance(other, Point):
            x1, y1 = self.top_left.x, self.top_left.y
            x2, y2 = x1 + self.side_length, y1 + self.side_length
            return x1 <= other.x <= x2 and y1 <= other.y <= y2
        elif isinstance(other, Line):
            pass
        elif isinstance(other, Circle):
            pass
        elif isinstance(other, Square):
            x1, y1 = self.top_left.x, self.top_left.y
            x2, y2 = x1 + self.side_length, y1 + self.side_length
            ox1, oy1 = other.top_left.x, other.top_left.y
            ox2, oy2 = ox1 + other.side_length, oy1 + other.side_length
            return not (x2 < ox1 or x1 > ox2 or y2 < oy1 or y1 > oy2)
        return False
