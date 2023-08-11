"""_summary_
 a function that return true if an object is an instance of class and flase instead
    """
def is_same_class(obj, a_class):
    """_summary_

    Args:
        obj (_type_): object
        a_class (_type_): class

    Returns:
        _type_: False or True
    """
    return type(obj) is a_class