# DEKORATORY KLAS -> do przeanalizowania, bo głowa mała
import inspect


def auto_repr(cls):
    members = vars(cls)

    if "__repr__" in members:
        raise TypeError(f'{cls.__name__} already defines __repr__.')

    if "__init__" not in members:
        raise TypeError(f'{cls.__name__} does not override __init__.')

    signature = inspect.signature(cls.__init__)
    parameter_names = list(signature.parameters)[1:]

    if not all([members.get(name, None) for name in parameter_names]):
        raise TypeError(f'Cannot apply auto_repr to {cls.__name__} because not all '
                        f'_init__ parameters have matching properties.')

    def synthesized_repr(self):
        return "{type_class}({args})".format(
            type_class=type(self).__name__,
            args=', '.join(f'{name}={getattr(self, name)!r}' for name in parameter_names)
        )

    setattr(cls, "__repr__", synthesized_repr)

    return cls


@auto_repr
class Location:
    def __init__(self, name, position):
        self._name = name
        self._position = position


    @property
    def name(self):
        return self._name


    @property
    def position(self):
        return self._position


    # def __repr__(self):
    #     return f"{type(self).__name__}(name={self.name!r}, position={self.position!r})"


    def __str__(self):
        return self.name


@auto_repr
class Position:
    def __init__(self, latitude, longitude):
        self._latitude = latitude
        self._longitude = longitude


    @property
    def latitude(self):
        return self._latitude


    @property
    def longitude(self):
        return self._longitude


    @property
    def latitude_hemisphere(self):
        return "N" if self._latitude >= 0 else "S"


    @property
    def longitude_hemisphere(self):
        return "E" if self._longitude >= 0 else "W"


    # def __repr__(self):
    #     return f"{type(self).__name__}(latitude={self._latitude}, longitude={self._longitude})"


    def __str__(self):
        return format(self)


    def __format__(self, format_spec):
        component_format_spec = ".2f"

        prefix, dot, suffix = format_spec.partition(".")

        if dot:
            num_decimal_places = int(suffix)
            component_format_spec = f".{num_decimal_places}f"

        latitude = format(abs(self._latitude), component_format_spec)
        longitude = format(abs(self._longitude), component_format_spec)

        return f"{latitude}° {self.latitude_hemisphere}, {longitude}°{self.longitude_hemisphere}"


class EarthPosition(Position):
    pass



#--------------------------------------------------------------------------------#

hong_kong = Location("Hong Kong", EarthPosition(22.29, 114.16))
cape_town = Location("Cape Town", EarthPosition(-33.93, 18.42))
ep = EarthPosition(22.29, 114.26)
# print(p)
# print(dir(object))
# print(hong_kong)
print(f'{hong_kong!r}')
print(f'{ep!r}')