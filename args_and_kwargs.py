########## *ARGS & **KWARGS  ##########

# RETURNS AN ERROR
'''
def super_func(args):
    return sum(args)

super_func(1, 2, 3, 4, 5)
'''


# ARGS
'''
def super_func(*args):
    print(args)
    return sum(args)

print(super_func(1, 2, 3, 4, 5))
'''


# KWARGS 1
'''
def super_func(*args, **kwargs):
    print(kwargs)
    return sum(args)

print(super_func(1, 2, 3, 4, 5, num1 = 5, num2 = 10))
'''

# KWARGS 2
def super_func(*args, **kwargs):
    total = 0
    for items in kwargs.values():
        total += items
    return sum(args) + total

print(super_func(1, 2, 3, 4, 5, num1 = 5, num2 = 10))

# RULE OF ORDERS
# 1. params
# 2. *args
# 3. default parameters
# 4. **kwargs