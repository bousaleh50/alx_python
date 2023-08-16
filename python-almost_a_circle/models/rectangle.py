"""_summary_
  class rectangle inherite from class Base
"""
Base=__import__("base").Base


class Rectangle(Base):
    """_summary_

    Args:
        Base (_type_): _description_
    """
    def __init__(self,width,height,x=0,y=0,id=None):
        """_summary_

        Args:
            width (_type_): the width of the rectangle
            height (_type_): height of the rectangle
            x (int, optional): desc. Defaults to 0.
            y (int, optional): _description_. Defaults to 0.
            id (_type_, optional): _description_. Defaults to None.
        """
        super().__init__(id)
        self.__width=width
        self.__height=height
        self.__x=x
        self.__y=y