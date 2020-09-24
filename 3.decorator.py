from datetime import datetime


def time_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = datetime.now()
        new_func = func(*args, **kwargs)
        print(datetime.now()-start_time)
        return new_func
    return wrapper


@time_decorator
def per_numbers(number):
    per_numbers_list = []
    for i in range(number):
        if i % 5 == 0:
            per_numbers_list.append(i)
    return per_numbers_list


print(per_numbers(10000))
print(per_numbers(100000))




