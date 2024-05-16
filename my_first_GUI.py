########## MY FIRST GUI ##########

picture = [
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0]
]


'''
for _ in picture[0]:
    if _ == 0:
        print(' ')
    else:
        print('*')

for _ in picture[1]:
    if _ == 0:
        print(' ')
    else:
        print('*')
'''

for row in picture:
    for pixel in row:
        if (pixel == 0):
            print(' ', end='')
        else:
            print('*', end='')

    print('')
        