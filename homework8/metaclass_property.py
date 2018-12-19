from collections import defaultdict

GET = 'get'
SET = 'set'
DEL = 'del'


class YourMetaClass(type):
    def __new__(cls, name, bases, namespace, **kwds):
        new_class = type.__new__(cls, name, bases, namespace)
        property_methods = defaultdict(dict)

        for name, attribute in namespace.items():
            if not callable(attribute):
                continue

            try:
                method, property_name = name.split('_', 1)
            except ValueError:
                continue

            if (method not in (GET, SET, DEL) or
                    not property_name.isidentifier()):
                continue

            property_methods[property_name][method] = attribute

        for property_name, methods in property_methods.items():
            constructed_property = property(
                methods.get(GET, None),
                methods.get(SET, None),
                methods.get(DEL, None),
            )
            setattr(new_class, property_name, constructed_property)

        return new_class


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
