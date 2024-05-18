########## COMPREHENSIONS ##########
##### LIST COMPREHENSIONS #####

# Not using comprehension:
'''my_list = []

for char in 'Hello':
    my_list.append(char)

print(my_list)
'''

# Using comprehension:
my_list = [char for char in 'Hello']
print(my_list)

my_list2 = [num for num in range(0, 100)]
print(my_list2)

multiply_list = [num * 2 for num in range(0, 100)]
print(multiply_list)

##### SET COMPREHENSIONS #####


##### DICTIONARY COMPREHENSIONS #####