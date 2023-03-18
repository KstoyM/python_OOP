# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
# person_list = [Person("Gosho", 13), Person("Ivan", 10)]
# try:
#     curr_person = next(filter(lambda x: x.name == "Bo", person_list))
# except StopIteration:
#     raise Exception("Blabla")
# print(curr_person)

lst = [1, 2, 3, 4]

for num in lst:
    if num == 3:
        print(num)
else:
    print('Eat dick')