class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __repr__(self):
        return f'{self.name} {self.surname}'

    def __add__(self, other):
        new_person_name = self.name
        new_person_surname = other.surname
        new_person = Person(new_person_name, new_person_surname)
        return new_person


class Group:
    def __init__(self, name, people):
        self.name = name
        self.people = people

    def __len__(self):
        return len(self.people)

    def __add__(self, other):
        new_name = f'{self.name} {other.name}'
        new_people = self.people + other.people
        new_group = Group(new_name, new_people)
        return new_group

    def __repr__(self):
        return f"Group {self.name} with members {', '.join(str(m) for m in self.people)}"

    def __getitem__(self, idx):
        return f"Person {idx}: {self.people[idx]}"


p0 = Person('Aliko', 'Dangote')
p1 = Person('Bill', 'Gates')
p2 = Person('Warren', 'Buffet')
p3 = Person('Elon', 'Musk')
p4 = p2 + p3

first_group = Group('__VIP__', [p0, p1, p2])
second_group = Group('Special', [p3, p4])
third_group = first_group + second_group

print(len(first_group))
print(second_group)
print(third_group[0])

for person in third_group:
    print(person)
