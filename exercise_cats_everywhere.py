########## CATS EVERYWHERE! ##########
# MY SOLUTION

#Given the below class:
class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats
cat1 = Cat('Thomas O\'Malley', 4)
cat2 = Cat('Minnie', 15)
cat3 = Cat('Talisker', 12)
# print(cat1, cat2, cat3)
# print(cat1.age, cat2.age, cat3.age)

# 2 Create a function that finds the oldest cat
cat_ages = [(cat1.age), (cat2.age), (cat3.age)]
highest_age = max(cat_ages)
# print(highest_age)

# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
print(f'The oldest cat is {highest_age} years old.')

# UDEMY SOLUTION
# Given the below class:

class Cat:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age

#Answers:
# 1 Instantiate the Cat object with 3 cats.
cat1 = Cat('cat1', 5)
cat2 = Cat('Cat2', 7)
cat3 = Cat('Cat3', 3)


# 2 Create a function that finds the oldest cat.
def oldest_cat(*args):
    return max(args)


# 3 Print out: "The oldest cat is x years old.".
# x will be the oldest cat age by using the function in #2
print(f'Oldest Cat is {oldest_cat(cat1.age, cat2.age, cat3.age)} years old.')
