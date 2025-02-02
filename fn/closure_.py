def sentence(name):
    class Yolo:
        pass
    def full_sentence(city):
        return f"My name is {name} and I live in {city}.", Yolo

    return full_sentence


message = sentence("Mateusz")

# print(message("Gdańsk"))
# print(message.__closure__[0].cell_contents)
# print(message.__closure__[1].cell_contents)

# def power10(base):
#     return base ** 10
#
# def power5(base):
#     return base ** 5

def power_factory(exponent):
    def power(base):
        return base ** exponent
    return power

power10=power_factory(10)
power5 = power_factory(5)

# print(power10(2))

# generowanie ID (1, 2, ...)

def gen_id(idx=0):
    def next_id(new_value=None):
        nonlocal idx

        if new_value is not None:
            idx = new_value
        result = idx
        idx += 1

        return result

    # def next_id():
    #     result = next_id.idx
    #     next_id.idx += 1
    #     return result

    next_id.idx = 0
    return next_id

next_id_ = gen_id(42)
print(next_id_())
print(next_id_())
print(next_id_(200))
print(next_id_())
