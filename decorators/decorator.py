import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = end.end()
        print(f"{func.__name__} ran in {end-start} time")
        return result
    return wrapper


@timer
def example_function(n):
    time_.sleep(n)
    
example_function(2)    