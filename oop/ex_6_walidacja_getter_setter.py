# # 2 < value < 10
#
# class X:
#     def __init__(self, value: str):
#         self.value = value
#
#
#     def get_value(self):
#         return self._value
#
#
#     def set_value(self, value):
#         if not  (2 < len(value) < 10):
#             raise ValueError("Something is no yes")
#         self._value = value
#
#
#     value = property(get_value, set_value)  # nakładam swoje customowe property, żeby zwykłe x.value nie działo i nie psuło walidacji
#     # JEŻELI PRZYPISUJEMY TO SETTER
#     # JEŻELI ODCZYTUJEMY TO GETTER
#     # URUCHAMIA SIĘ JE PO NAZWIE WIĘC MUSI BYĆ TAKA SAMA JAK W INIT
#
#
#
# x = X('Roman')
# x.value = 'Ala ma '
# print(x.value)



# ------------------------------------------------------------------------#

class X:
    def __init__(self, value: str):
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if not  (2 < len(value) < 10):
            raise ValueError("Something is no yes")
        self._value = value


    # TE DWA DEKORATORY TO JEST TO SAMO CO TEN ZAPIS Z PROPERTY



x = X('Roman')
x.value = 'Ala ma'
print(x.value)
print(vars(x))
print(vars(X))
