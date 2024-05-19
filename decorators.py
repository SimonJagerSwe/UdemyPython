########## DECORATORS ##########
'''
def hello():
    print('Helloooooooooo!')

greet = hello
print(greet())

del hello
print(greet)
'''
# Higher order functions
# Functions that accept other functions as parameters
'''
def greet(func):
    func()

def greet2():
    def func():
        return 5
    return func
    '''


# Actual decorators (at last)
'''
def my_decorator(func):
    def wrap_func():
        print('*************')
        func()
        print('*************')
    return wrap_func

@my_decorator
def hello():
    print('Helloooooooo!')

@my_decorator
def bye():
    print('See ya later!')

hello()
bye()

a = my_decorator(hello)
a()
'''


# More complex decorator
'''
def my_decorator(func):
    def wrap_func(*args, **kwargs):
        func(*args, **kwargs)
    return wrap_func

@my_decorator
def hello(greeting, emoji = ':('):
    print(greeting, emoji)

hello('Hiiiiiii!')
hello('Hiiiiiii!', ':)')
'''

# Performance decorator
from time import time
def performance(func):
    def wrapper(*args, **kwargs):
        time1 = time()
        result = func(*args, **kwargs)
        time2 = time()
        print(f'It took {time2 - time1} ms')
        return result
    return wrapper

@performance
def long_time():
    for i in range(100000000):
        i*5

long_time()