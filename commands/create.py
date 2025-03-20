from shapes.line import Line
from shapes.square import Square
from shapes.circle import Circle
from shapes.point import Point


def create_shape(shape_type, shapes_list):
    if shape_type == "point":
        args = Point.input_attributes()
        new_shape = Point(*args)
    elif shape_type == "line":
        args = Line.input_attributes()
        new_shape = Line(*args)
    elif shape_type == "circle":
        args = Circle.input_attributes()
        new_shape = Circle(*args)
    elif shape_type == "square":
        args = Square.input_attributes()
        new_shape = Square(*args)
    else:
        raise ValueError("Unknown shape type")

    # Проверка коллизий
    for existing_shape in shapes_list:
        if new_shape.collides_with(existing_shape):
            print("Error: The new shape collides with an existing shape.")
            return None

    return new_shape
