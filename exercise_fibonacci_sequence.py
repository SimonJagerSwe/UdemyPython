########## EXERCISE: FIBONACCI SEQUENCE ##########

# My solution
def fib(num):
    a = 0
    b = 1
    for i in range(num):
        yield a
        a = b
        b = a + b

print(fib(20))