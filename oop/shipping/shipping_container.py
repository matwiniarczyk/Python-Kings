from oop.shipping import iso6346


class ShippingContainer:
    HEIGHT_FT = 8.6
    WIDTH_FT = 8.0

    next_serial = 1

    # @staticmethod
    # def _generate_serial():
    #     result = ShippingContainer.next_serial
    #     ShippingContainer.next_serial += 1
    #     return result
    # *zamiast ShippingContainer - type(self) zwraca nam klasę i można się z tym bawić i manipulować klasą, mimo że __init__ to classic method do obiektów

    @classmethod
    def _generate_serial(cls):
        result = cls.next_serial
        cls.next_serial += 1
        return result


    @staticmethod
    def _make_bic_code(owner_code, serial):
        return iso6346.create(
            owner_code=owner_code,
            serial=str(serial).zfill(6)
        )


    @classmethod    #custom konstruktor
    def create_empty(cls,owner_code, length_ft, **kwargs):
        return cls(owner_code, length_ft, contents=[], **kwargs)


    @classmethod    #custom konstruktor
    def create_with_items(cls, owner_code, length_ft, items, **kwargs):
        return cls(owner_code, length_ft, contents=list(items), **kwargs)


    @property   # WZÓR/TEMPLATE
    def volume_ft3(self):
        return self._calc_volume()

    def _calc_volume(self): # A TU JEST KROK DO ALGORYTMU DO WZORU KTÓRE POTEM ZMIENIĘ NA POTRZEBĘ INNEGO KONTENERA
        return ShippingContainer.HEIGHT_FT * ShippingContainer.WIDTH_FT * self.length_ft


    def __init__(self, owner_code, length_ft, contents, **kwargs):
        self.length_ft = length_ft
        self.owner_code = owner_code
        self.contents = contents
        self.bic = self._make_bic_code(
            owner_code=owner_code,
            serial=ShippingContainer._generate_serial()
        )


class RefrigeratedShippingContainer(ShippingContainer):
    MAX_CELSIUS = 4.0
    FRIDGE_VOLUME_FT3 = 100


    @staticmethod
    def _make_bic_code(owner_code, serial):
        return iso6346.create(
            owner_code=owner_code,
            serial=str(serial).zfill(6),    # zfill wypełnia mi zmienną zerami
            category='R'
        )


    @property
    def celsius(self):
        return f'{self._celsius}°C'


    @celsius.setter     # WZÓR/TEMPLATE
    def celsius(self, value):
        self._set_celsius(value)

    def _set_celsius(self, value):  # ALGORYTM DO EWENTUALNEJ ZMIANY PÓŹNIEJ
        if value > RefrigeratedShippingContainer.MAX_CELSIUS:
            raise ValueError("Temperature too hot!")
        self._celsius = value


    @property
    def fahrenheit(self):
        return self._celsius * 9 / 5 + 32


    @fahrenheit.setter
    def fahrenheit(self, value):
        self.celsius = (value - 32) * 5 / 9 # tu się uruchomi setter do celsius więc tam się value zwaliduje


    def _calc_volume(self): # NADPISALIŚMY METODĘ (POLYMORPHISM) - krok do wzoru (properties) zmieniłem
        return super()._calc_volume() - RefrigeratedShippingContainer.FRIDGE_VOLUME_FT3


    def __init__(self, owner_code, length_ft, contents, *, celsius, **kwargs):
        super().__init__(owner_code, length_ft, contents, **kwargs)
        self.celsius = celsius


class HeatedRefrigeratedShippingContainer(RefrigeratedShippingContainer):
    MIN_CELSIUS = -20


    def _set_celsius(self, value):  # NADPISAŁEM KROK ALGORYTMU DO WZORU ŻEBY DZIAŁAŁ MI NA HEATED CONTAINER
        if value < HeatedRefrigeratedShippingContainer.MIN_CELSIUS:
            raise ValueError("Temperature too cold!")
        super()._set_celsius(value)




s1 = ShippingContainer.create_with_items('YML', 20, ['ice', 'snow'], celsius=2.0)
r1 = RefrigeratedShippingContainer.create_empty('YML', 20, celsius=2.0)
h1 = HeatedRefrigeratedShippingContainer('YML', 20, ['onion'], celsius=2.0)
r1.celsius = -50
