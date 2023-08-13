BaseGeometry = __import__('5-base_geometry').BaseGeometry

"""_summary_

    Raises:
        Exception: _description_
        TypeError: _description_
        ValueError: _description_
    """

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
