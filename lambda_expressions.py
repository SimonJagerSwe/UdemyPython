########## EXERCISE: MAP, FILTER, ZIP & REDUCE ##########
# A function only used once

# lambda param : action(param)
from functools import reduce
my_list = [1, 2, 3]

# Instead of making a function to only be used once:
'''
def multiply_by2(list):
    new_list = []
    for item in list:
        new_list.append(item*2)
    return new_list
'''
# Make a lambda function:
print(list(map(lambda item : item * 2, my_list)))
print(list(filter(lambda item : item % 2 != 0, my_list)))
print(reduce(lambda acc, item : acc + item, my_list ))