"""_summary_

    Raises:
        TypeError: _description_
        ValueError: _description_

    Returns:
        _type_: _description_
    """
class Square:
    """_summary_
     function area calculat and return the area of the square
    """
    def __init__(self, size=0):
        if(type(size) not in [int,float]):
            raise TypeError("size must be an integer")
        
        if(size<0):
            raise ValueError("size must be >= 0")
        self.__size=size
    
    def area(self):
        return self.__size*self.__size
