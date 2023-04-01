class Person:
    def __init__(self,  name, age):
        self.name = name
        self.age = age



ivan = Person('Ivan', 25)

lst = [ivan, Person('Gosho', 30)]

if ivan in lst:
    print('Yes')