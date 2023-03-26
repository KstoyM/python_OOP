class Person:
    def __init__(self,  name, age):
        self.name = name
        self.age = age


lst = [Person('Ivan', 25), Person('Gosho', 30)]

# max_age = 0
# winner = None
# for person in lst:
#     if person.age > max_age:
#         max_age = person.age
#         winner = person

winner = sorted(lst, key= lambda x: x.age)[0]

print(winner.name)