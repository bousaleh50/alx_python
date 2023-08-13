"""_summary_

    Raises:
        Exception: _description_
        TypeError: _description_
        ValueError: _description_

    Returns:
        _type_: _description_
    """

Rectangle=__import__("7-rectangle.py").Rectangle


class Square(Rectangle):
    """_summary_

    Args:
        Rectangle (_type_): _description_
    """
    def __init__(self, size):
        self.__size = 0
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        return f"[Square] {self.__size}/{self.__size}"
