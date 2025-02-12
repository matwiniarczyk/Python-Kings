class Yolo:
    def __init__(self):
        self.value = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.value > 5:
            raise StopIteration

        result = self.value
        self.value += 1
        return result


for element in Yolo():
    print(element)

