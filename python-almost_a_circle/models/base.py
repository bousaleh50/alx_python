"""_summary_
 the base class where other classes sshould inherit
"""

class Base:
    """_summary_
      id: instanse id
    """
    __nb_objects=0
    def __init__(self,id=None):
        """_summary_

        Args:
            id (_type_, optional): _description_. Defaults to None.
        """
        if(id!=None):
            self.id=id
        else:
            Base.__nb_objects+=1
            self.id=Base.__nb_objects
