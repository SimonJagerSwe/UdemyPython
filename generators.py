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
'''
def generator_function(num):
    for i in range(num):
        yield i * 2


for item in generator_function(1000):
    print(item)

g = generator_function(100)
next(g)
next(g)
print(next(g))
'''


# Under the hood
def special_for(iterable):
    iterator = iter(iterable)
    while True:
        try:
            print(iterator)
            print(next(iterator))
        except StopIteration:
            break

special_for([1, 2, 3])


# Creating our own range()
class MyGen():
    current = 0
    def __init__(self, first, last):
        self.first = first
        self.last = last
        MyGen.current = self.first

    def __iter__(self):
        return self
    
    def __next__(self):
        if MyGen.current < self.last:
            num = MyGen.current
            MyGen.current += 1
            return num
        raise StopIteration

gen = MyGen(0, 100)
for i in gen:
    print(i)