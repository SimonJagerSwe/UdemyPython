########## CLEAN CODE ##########

# MY VERSION
def is_odd_or_even(num):
    if num % 2 == 0:
        print('Number is even')
    else:
        print('Number is odd')

is_odd_or_even(3)

# UDEMY VERSION
def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False
    
print(is_even(51))