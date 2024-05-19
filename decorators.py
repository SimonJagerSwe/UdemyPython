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
def greet(func):
    func()

def greet2():
    def func():
        return 5
    return func