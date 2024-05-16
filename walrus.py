########## WALRUS OPERATOR ##########

'''
a = 'Hellooooooo'

if (len(a) > 10):
    print(f'Too long {len(a)} elements')
    '''

a = 'Hellooooooo'

if ((n := len(a)) > 10):
    print(f'Too long: {n} elements')


while ((n := len(a)) > 1):
    print(n)
    a = a[:-1]

print(a)