########## FILE I/O ##########
my_file = open('test.txt')

print(my_file)
print(my_file.read())
print(my_file.read())
my_file.seek(0)
print(my_file.read())
print(my_file.read())
print(my_file.readline(3))