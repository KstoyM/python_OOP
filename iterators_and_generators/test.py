class vowels:
    def __init__(self, string):
        self.string = string
        self.start = 0

    @property
    def string(self):
        return self.__string

    @string.setter
    def string(self, value):
        result = ''
        for letter in value:
            if letter.lower() in ['a', 'e', 'i', 'u', 'y', 'o']:
                result += letter
        self.__string = result

    def __iter__(self):
        return self

    def __next__(self):
        if self.start < len(self.string):
            self.start += 1
            return self.string[self.start - 1]
        else:
            raise StopIteration


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)