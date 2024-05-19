########## DECORATORS ##########

def hello():
    print('Helloooooooooo!')

greet = hello

print(greet())

del hello

print(greet)