BaseGeometry = __import__('7-base_geometry').BaseGeometry

"""_summary_

    Raises:
        Exception: _description_
        TypeError: _description_
        ValueError: _description_
    """
class BaseGeometry:
    """_summary_
    """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

class Rectangle(BaseGeometry):
    """_summary_

    Args:
        BaseGeometry (_type_): _description_
    """
    def __init__(self, width, height):
        self.__width = 0
        self.__height = 0
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
        


print(issubclass(Rectangle,BaseGeometry))
