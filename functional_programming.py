########## FUNCTIONAL PROGRAMMING ##########

##### PURE FUNCTIONS #####
# A function that does not produce side effects or impacts the outside world

# Does not impact the outside world
'''
def multiply_by2(list):
    new_list = []
    for item in list:
        new_list.append(item*2)
    return new_list
    
print(multiply_by2([1, 2, 3]))
'''

'''
# Impacts the outside world, but gives the same result for now
new_list = []
def multiply_by2(list):    
    for item in list:
        new_list.append(item*2)
    return new_list
    
print(multiply_by2([1, 2, 3]))
'''


##### MAP #####
'''
def multiply_by2(list):
    new_list = []
    for item in list:
        new_list.append(item*2)
    return new_list
'''

'''
def multiply_by2(item):
    return item*2

print(list(map(multiply_by2, [1, 2, 3])))
'''


##### FILTER #####
'''
my_list = [1, 2, 3]
def check_odd(item):
    return item % 2 != 0

print(list(filter(check_odd, my_list)))
'''


##### ZIP #####
'''
my_list = [1, 2, 3]
your_list = [10, 20, 30]

print(list(zip(my_list, your_list)))
'''


##### REDUCE #####
from functools import reduce

my_list = [1, 2, 3]

def accumulator(acc, item):
    print(acc, item)
    return acc + item


print(reduce(accumulator, my_list, 0))