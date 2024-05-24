########## FILE I/O ##########
with open('test.txt') as my_file:
    print(my_file.readlines())


##### WRITING TO A FILE #####
# THIS OVERWRITES EXISTING TEXT IN FILE
'''
with open('test.txt', mode = 'r+') as my_file:
    text = my_file.write('Haha! Sneaking in and adding new text!')
    print(text)
'''

with open('test.txt', mode = 'a') as my_file:
    text = my_file.write('Haha! Sneaking in and adding new text!')
    print(text)


# Creating and writing in a new file
with open('sad.txt', mode = 'w') as my_file2:
    text = my_file2.write(':(')
    print(text)