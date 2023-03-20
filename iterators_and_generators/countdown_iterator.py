class countdown_iterator:

    def __init__(self, value):
        self.value = value + 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.value <= 0:
            raise StopIteration

        self.value -= 1
        return self.value

iterator = countdown_iterator(10)
for item in iterator:
    print(item, end=" ")