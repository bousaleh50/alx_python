"""_summary_
    """
def inherits_from(obj, a_class):
    """_summary_

    Args:
        obj (_type_): _description_
        a_class (_type_): _description_

    Returns:
        _type_: _description_
    """
    return isinstance(obj, a_class) and issubclass(type(obj), a_class) and type(obj) is not a_class

