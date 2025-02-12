class ShippingContainer:
    next_serial = 1337

    def __init__(self, owner_code, contents):
        self.owner_code = owner_code
        self.contents = contents
        self.serial = type(self).next_serial
        type(self).next_serial += 1
class YoloShippingContainer(ShippingContainer):
    pass


class Y:
    pass


class X(ShippingContainer, Y):
    pass

ysc = YoloShippingContainer("MAE", ['A', 'B', 'C', 'D'])
ysc2 = YoloShippingContainer("MAE2", ['A', 'B', 'C', 'D'])


print(X.__mro__)
print(X.__bases__)
print(YoloShippingContainer.__name__)
print(type(ysc).__name__)
print(YoloShippingContainer.__dict__)
print(vars(YoloShippingContainer))