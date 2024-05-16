########## FORMATTED STRINGS ##########

name = 'Johnny'
age = 55

print('Welcome, ' + name)
print(f'Welcome, {name}')

print('Hi, ' + name + ' you are ' + str(age) + ' years old!')
print(f'Hi, {name} you are {age} years old!')

print('Hi {}, you are {} years old!'.format('Johnny', '55'))
print('Hi {}, you are {} years old!'.format(name, age))