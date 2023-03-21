from time import sleep, time

def measure_time(func):
    def wrapper(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        end = time()
        print(f'Executime time of {func.__name__}: {end - start} seconds')
        return result
    return wrapper

@measure_time
def slow_function(n):
    sleep(n)

slow_function(2)