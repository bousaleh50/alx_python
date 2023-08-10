"""_summary_

    Raises:
        TypeError: _description_
        ValueError: _description_
        TypeError: _description_
        ValueError: _description_

    Returns:
        _type_: _description_
    """
class Square:
    """_summary_
       @property is a getter that reaturn the size of the square
       @size.setter is set the size of the square to a new value
       def my_print is printing the square
    """
    def __init__(self, size=0):
        if(type(size) not in [int,float]):
            raise TypeError("size must be an integer")
        
        if(size<0):
            raise ValueError("size must be >= 0")
        self.__size=size
    
    def area(self):
        return self.__size*self.__size
    @property
    def size(self):
        return self.__size
    
    
    @size.setter
    def size(self,value):
        if(type(value) not in [int,float]):
            raise TypeError("size must be an integer")
        
        if(value<0):
            raise ValueError("size must be >= 0")
        self.__size=value
    
    def my_print(self):
        for i in range(self.__size):
            print("#"*self.__size)



