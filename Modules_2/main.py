########## MAIN ##########
print(__name__)     # __main__ will be the name of the file we run, regardless of other circumstances
from Shopping.utility import multiply, divide
from Shopping.More_shopping.shopping_cart import buy
# from X import *       IMPORTS EVERYTHING

print(buy('Apple'))
print(divide(5, 2))
print(multiply(5, 2))
print(max([1, 2, 3]))

##### __name__ #####
if __name__ == '__main__':
    print('Please run this')

class Student():
    pass

st1 = Student()
print(type(st1))