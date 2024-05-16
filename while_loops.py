########## WHILE LOOPS ##########

# while condition == True:
#    run loop

# Infinite loop:
'''
i = 0
while 0 < 50:
    print(i)
'''

##### EXERCISE #####
'''
i = 0
while i <= 50:
    print(i)
    i += 1

print('Done!')
'''

my_list = [1, 2, 3]

'''
# Do it with for

for item in my_list:
    print(item)

'''


# Do it with while
'''
i = 0
while i < len(my_list):
    print(my_list[i])
    i += 1
'''


'''
while True:
    input('Say something: ')
    break
'''

while True:
    response = input('Say Something: ')
    if (response == 'Bye!'):
        break

# Other tools for while loops:
# continue
# pass (skips this loop for the time being, good for development purposes)