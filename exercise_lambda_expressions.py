########## EXERCISE: LAMBDA EXPRESSIONS ##########
# 1: Square
my_list = [5, 4, 3]

# My solution
print(list(map(lambda num : num ** 2, my_list)))


# Udemy solution
print(list(map(lambda item : item * item, my_list)))

# 2: List sorting
a = [(0, 2), (3, 4), (10, -1), (9.9)]

a.sort(key = lambda x : x[1])
print(a)