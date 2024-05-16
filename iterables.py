########## ITERABLES ##########
# list, dictionary, tuple, set or string that can be iterated on

'''
user = {
    'name' : 'Gollum',
    'age' : 5006,
    'can_swim' : False
}

for item in user:
    print(item)

for item in user.items():
    print(item)

for item in user.keys():
    print(item)

for item in user.values():
    print(item)

for item in user.items():
    key, value = item
    print(key, value)

for key, value in user.items():
    print(key, value)
'''

##### EXERCISE #####
# Counter
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
counter = 0
# final_sum = add_sum[-1]

for i in my_list:
    counter += i

print(counter)