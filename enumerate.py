########## ENUMERATE ##########

for char in enumerate('Helloooooo!'):
    print(char)

for i, char in enumerate('Helloooooo!'):
    print(i, char)

for i, char in enumerate([1, 2, 3]):
    print(i, char)

for i, char in enumerate((1, 2, 3)):
    print(i, char)

##### EXERCISE ######
for i, char in enumerate(list(range(100))):
    if char == 50:
        print(f'Index of 50 is: {i}')