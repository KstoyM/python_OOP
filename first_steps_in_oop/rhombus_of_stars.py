size = int(input())

# for i in range(1, size + 1):
#     spaces = ' ' * (size - i)
#     stars = '* ' * i
#     print(spaces + stars)
#
# for i in range(size - 1, 0, -1):
#     spaces = ' ' * (size - i)
#     stars = '* ' * i
#     print(spaces + stars)

for x in range(size):
    space_data = size - x - 1
    stars_data = x + 1
    print(' ' * space_data + '* ' * stars_data)