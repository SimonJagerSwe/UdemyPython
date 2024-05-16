########## GLOBAL KEYWORDS ##########
'''
a = 10

def confusion(b):
    print(b)
    a = 90

confusion(300)
'''

# Too complicated in big files
'''
total = 0

def count():
    global total
    total += 1
    return total

count()
count()
print(count())
'''

total = 0

def count(total):
    total += 1
    return total

count(total)
count(total)
print(count(count(count(total))))