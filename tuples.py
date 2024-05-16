########## TUPLES ##########
# Tuples are immutable

my_tuple = (1, 2, 3, 4, 5)
print(5 in my_tuple)

user = {
    'basket' : [1, 2, 3],
    'greet' : 'Hello',
    'age' : 20
}

print(user.items())

new_tuple = my_tuple[1:2]
print(new_tuple)