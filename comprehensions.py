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

my_list3 = [num * 2 for num in range(0, 100)]
print(my_list3)

my_list4 = [num ** 2 for num in range(0, 100) if num % 2 == 0]
print(my_list4)


##### SET COMPREHENSIONS #####
my_set = {char for char in 'Hello'}
print(my_set)


##### DICTIONARY COMPREHENSIONS #####
simple_dict = {
    'A' : 1, 
    'B' : 2
}

my_dict = {key : value ** 2 for key, value in simple_dict.items() if value % 2 == 0}
print(my_dict)

my_dict2 = {num : num *2 for num in [1, 2, 3]}
print(my_dict2)