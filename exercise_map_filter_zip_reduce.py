########## EXERCISE: MAP, FILTER, ZIP & REDUCE ##########
from functools import reduce

#1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']

def capitalise(name):
    capital_pets = []
    for name in my_pets:
        capital_pets.append(name.capitalize())
    return capital_pets

print(capitalise(my_pets)) 



#2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5,4,3,2,1]
my_num_reverse = sorted(my_numbers)
new_tuple = tuple(zip(my_strings, my_num_reverse))

print(new_tuple)


#3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]

def check_pass(grade):
    return grade >= 50

print(list(filter(check_pass, scores)))


#4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?
all_num = (my_numbers + scores)

def accumulator(acc, item):
    print(acc, item)
    return acc + item

total = reduce(accumulator, all_num, 0)
print(total)