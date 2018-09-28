"""
Homework 8.

Create metaclass that generates properties automatically. Using this
metaclass for your class will give you explicit accessor methods.
A method called set_x, will automatically create a property x that uses
set_foo as a setter method. Same for get_x and del_x.
"""

from collections.abc import Callable
from collections import defaultdict

GET = 'get'
SET = 'set'
DEL = 'del'


class YourMetaClass(type):
    def __new__(cls, name, bases, namespace, **kwds):
        result = type.__new__(cls, name, bases, namespace)
        descr = defaultdict(dict)

        for name, attribute in namespace.items():
            if not isinstance(attribute, Callable):
                continue

            try:
                method, property_name = name.split('_', 1)
            except ValueError:
                continue

            if method not in (GET, SET, DEL):
                continue

            descr[property_name][method] = attribute

        for property_name, mapping in descr.items():
            new_property = property(
                mapping.get(GET, None),
                mapping.get(SET, None),
                mapping.get(DEL, None),
            )
            setattr(result, property_name, new_property)

        return result


class Example(metaclass=YourMetaClass):
    def __init__(self):
        self._x = None

    def get_x(self):
        return -self._x

    def set_x(self, value):
        self._x = value + 1

    def get_y(self):
        return 'y'

    def test(self):
        return True


if __name__ == '__main__':
    ex = Example()
    ex.x = 255

    print(ex.x)
    print(ex.y)
