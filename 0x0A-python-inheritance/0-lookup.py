#!/usr/bin/python3


def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.

    Args:
        obj: An object.

    Returns:
        A list of attributes and methods.

    Example:
    >>> class MyClass1(object):
    ...     pass
    >>> lookup(MyClass1)
    ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__',
            '__eq__', '__format__', '__ge__', '__getattribute__',
            '__gt__', '__hash__', '__init__', '__le__', '__lt__',
            '__module__', '__ne__', '__new__', '__reduce__',
            '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__',
            '__str__', '__subclasshook__', '__weakref__']

    """
    return dir(obj)

# Example usage
# class MyClass1(object):
#    pass
#
# class MyClass2(object):
#    my_attr1 = 3
#    def my_meth(self):
#        pass

# print(lookup(MyClass1))
# print(lookup(MyClass2))
# print(lookup(int))
