class A:
    magic = 42

    @classmethod
    def yolo(cls):
        return 42

# print(A.magic)

# print(type(5))

def yolo(obj):
    obj.xd = 42

Magic = type('Magic', (object, ),{
    'magic': 42,
     #'__init__': yolo,   to samo co na dole
    '__init__': lambda obj: setattr(obj, 'xd', 42),
    'true_magic' : classmethod(lambda obj: setattr(obj, 'xd', 42)),
})
# nazwa klasy, po czym dziedziczy, słownik metod/properties     TO ZACHACZA O METAPROGRAMING, BIG BRAIN LUDZIE

m = Magic()
print(m.magic)
print(m.xd)