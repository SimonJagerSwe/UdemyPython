########## FILE I/O ##########
with open('test.txt') as my_file:
    print(my_file.readlines())


##### WRITING TO A FILE #####

with open('test.txt', mode = 'r+') as my_file:
    text = my_file.write('Haha! Sneaking in and adding new text!')
    print(text)