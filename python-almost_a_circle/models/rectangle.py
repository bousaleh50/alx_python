"""_summary_
  class rectangle inherite from class Base
  
"""
Base=__import__("base").Base


class Rectangle(Base):
    """_summary_

    Args:
        Base (_type_): class Base
    """
    def __init__(self,width,height,x=0,y=0,id=None):
        super().__init__(id)
        self.__width=width
        self.__height=height
        self.__x=x
        self.__y=y