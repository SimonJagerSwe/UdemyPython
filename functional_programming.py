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
def multiply_by2(list):
    new_list = []
    for item in list:
        new_list.append(item*2)
    return new_list

print(map(multiply_by2, [1, 2, 3]))

##### FILTER #####

##### ZIP #####

##### REDUCE #####