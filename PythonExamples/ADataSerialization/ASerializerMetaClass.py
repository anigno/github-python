from collections import OrderedDict
from io import StringIO

little_endian = '<'


def _binary_type(format_char, default_value, should_repr=False):
    def decorator(prop):
        if not isinstance(prop, property):
            raise TypeError('decorated object is not a property')
        # prop.fget is a function, so it can have attributes
        prop.fget.__format_char__ = format_char
        prop.fget.__default_value__ = default_value
        prop.fget.__should_repr__ = should_repr
        return prop

    return decorator


binary_type_uint8 = _binary_type('B', 0)


class ASerializerMetaClass(type):

    @classmethod
    def __prepare__(mcs, name, bases, **kwargs):
        return OrderedDict()

    def __new__(mcs, name, bases, classdict, *args, **kwargs):
        result = type.__new__(mcs, name, bases, classdict, *args, **kwargs)
        result.to_buffer = mcs.to_buffer
        return result

    def to_buffer(self):
        format_str_builder = StringIO()
        format_str_builder.write(little_endian)
