class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point({self.x}, {self.y})"

    @staticmethod
    def input_attributes():
        x = float(input("Enter x coordinate: "))
        y = float(input("Enter y coordinate: "))
        return x, y

    def collides_with(self, other):
        from shapes.line import Line
        from shapes.square import Square
        from shapes.circle import Circle
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        elif isinstance(other, Line):
            return other.collides_with(self)
        elif isinstance(other, Circle):
            return other.collides_with(self)
        elif isinstance(other, Square):
            return other.collides_with(self)
        return False