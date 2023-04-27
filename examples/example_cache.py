from time import sleep, time

# словарь для хранения кэша (ускорение вывода повторных запросов)
CACHE = {}


def cache_func(function):
    def wrapper(*args, **kwargs):
        key = f'{function.__name__}::{args}::{kwargs}'  # создание ключа
        print(key)

        if key in CACHE:
            return CACHE[key]  # проврка был ли ранее подобный запрос

        sleep(5)

        result = function(*args, **kwargs)  # если запроса не было, то выполняеются вычисления

        CACHE[key] = result
        return result

    return wrapper


@cache_func
def add(x, y):
    return x + y


@cache_func
def foo():
    return 1


start = time()
print(add(12, 3))
print(add(12, 3))
print(foo())
print(foo())


print(CACHE)
print(f'time: {time()-start}')
