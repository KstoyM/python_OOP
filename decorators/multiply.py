# def multiply(times):
#
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             result = func(*args, **kwargs)
#             return times * result
#         return wrapper
#     return decorator
#
# @multiply(5)
# def add_ten(number):
#     return number + 10
#
# print(add_ten(6))

def multiply(times):
    return lambda f: lambda *args, **kwargs: times * f(*args, **kwargs)

@multiply(5)
def add_ten(number):
    return number + 10

print(add_ten(6))