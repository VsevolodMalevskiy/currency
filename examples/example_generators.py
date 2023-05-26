# students = 'STRING'
# students_iterator = iter(students)
#
# print(id(students))
# print(id(students_iterator))

"""
__next__
__iter__
"""
from contextlib import suppress  # noqa
from functools import wraps

# while True:
#     try:
#         print(students_iterator.__next__())
#     except StopIteration:
#         break

# for student in students:
#     print(student)

# gen = [i for i in 'STRING']  # list
# gen = {i for i in 'STRING'}  # set
# gen = {i: i for i in 'STRING'}  # dict

# gen = (i for i in 'STRING')
#
# for i in gen:
#     print(i)
#
# for i in gen:
#     print(i)


# def square():
#     counter = 0
#     while True:
#         print('GEN')
#         yield counter
#         counter += 1
#
#         if counter == 10:
#             return


# s = square()
# print(s.__next__())
# print(s.__next__())
# print(s.__next__())
# for i in square():
#     print(i)

"""
= - __add__
== - __eq__

__enter__
__exit__

"""


# class Connection:
#     def open(self):
#         print('OPEN')
#         return 'CONNECTION'
#
#     def close(self):
#         print('CLOSE')
#
#     def __enter__(self):
#         return self.open()
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self.close()
#         return False


# c = Connection()
#
# try:
#     obj = c.open()
#
#     print(obj)
#
#     print(1 + '1')
# finally:
#     c.close()
#
#
# with Connection() as obj:
#     print(obj)
#     # print(1 + '1')
#
# with suppress(Exception):
#     print('Suppressed')
#     print(1 + '1')

from time import sleep, time  # noqa


def timenew(param):
    def timeit(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start = time()

            result = func(*args, **kwargs)

            end = time()
            print(f'Total: {end - start}')  # noqa
            return result
        return wrapper
    return timeit


@timenew(3)
def foo(a):
    sleep(a)
    result = a
    return result


@timenew(4)
def bar():
    sleep(2)
    result = 2
    return result


# foo = timeit(3)(foo)
# bar = timeit(bar)

# foo(3)
# bar()
print(foo.__name__)  # noqa


class MyDecorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        # Code to be executed before the decorated function is called
        print("Before function execution")  # noqa

        # Call the decorated function
        result = self.func(*args, **kwargs)

        # Code to be executed after the decorated function is called
        print("After function execution")  # noqa

        return result

    def __enter__(self):
        # Code to be executed when entering the context
        print("Entering context")  # noqa

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Code to be executed when exiting the context
        print("Exiting context")  # noqa

        # You can handle exceptions within the context if needed
        if exc_type is not None:
            print(f"Exception: {exc_type}, {exc_val}, {exc_tb}")  # noqa
            # Return True to suppress the exception, or False to propagate it

        # Return False to propagate exceptions or True to suppress them
        return False
