########## GENERATORS ##########
# Generators are iterable

# range() is atype of generator
'''
def make_list(num):
    result = []
    for i in range(num):
        result.append(i * 2)
    return result

my_list = make_list(100)
print(my_list)

'''

# Make your own generator
def generator_function(num):
    for i in range(num):
        yield i * 2

'''
for item in generator_function(1000):
    print(item)
'''

g = generator_function(100)
next(g)
next(g)
print(next(g))
