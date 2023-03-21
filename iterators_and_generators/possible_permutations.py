from itertools import permutations

def possible_permutations(numbers):
    for el in list(permutations(numbers)):
        yield list(el)


[print(n) for n in possible_permutations([1, 2, 3])]