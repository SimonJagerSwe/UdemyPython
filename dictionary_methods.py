########## DICTIONARY METHODS ##########
'''
user = {
    'basket' : [1, 2, 3],
    'greet' : 'Hello',
    'age' : 20
}

print(user.get('age', 55))      # IF AGE IS MISSING IN user, 55 WILL BE THE DEFAULT

user_2 = dict(name = 'John', age = 55)
print(user_2)

print('size' in user)
print('age' in user.keys())
print('Hello' in user.keys())
print('Hello' in user.values())


user_3 = user.copy()
print(user.clear())
print(user_3)
print(user_3.pop('age'))
print(user_3)'''


# Exercise Dictionary Methods
# Scroll to see answers.

# 1 Create a user profile for your new game.
# This user profile will be stored in a dictionary with keys: 'age', 'username', 'weapons', 'is_active' and 'clan'
user = {
    'age' : '',
    'username' : '',
    'weapons' : '',
    'is_active' : True,
    'clan' : 'Hell\'s Satans'
}

# 2 iterate and print all the keys in the above user.
print(user.keys())

# 3 Add a new weapon to your user
user['weapons'] = 'Sword'

# 4 Add a new key to include 'is_banned'. Set it to false
user['is_banned'] = False
print(user)

# 5 Ban the user by setting the previous key to True
user['is_banned'] = True
print(user)

# 6 create a new user2 my copying the previous user and update the age value and username value.
user2 = user.copy()
print(user2)
user2['age'] = 20
user2['username'] = 'Steve'
print(user2)