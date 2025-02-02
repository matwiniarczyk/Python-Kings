class Y:
    def __init__(self, value):
        print("__new__Y")

        self.value_y = value


class X:
    def __new__(cls, *args, **kwargs):
        print("__new__X")
        self = super().__new__(cls, *args, **kwargs)
        self.magic = 42
        return self


    def __init__(self):
        print("__init__X")
        self.value = 42


    def multiply_value(self, multiplier):
        return self.value * multiplier


x = X()
print(type(x))
# print(x.value)
# print(x.value_y)
# syntactic sugar
# result = x.multiply_value(2)

# real execution
# X.multiply_value(x, 2)
# x.new_value = 2137
# print(result)