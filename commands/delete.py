def delete_shape(shapes_list, index):
    if 0 <= index < len(shapes_list):
        shapes_list.pop(index)
    else:
        raise IndexError("Invalid index")