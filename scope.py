########## SCOPE ##########
# What variables do a I have access to?
# Everything within a function is only accessible in that function (local)

# This will throw a bug as total is not in the global scope
'''def some_func():
    total = 100

print(total)'''

a = 1

def parent():
    a = 10
    def confusion():
        return a
    return confusion()

print(a)
print(parent())
print(a)


##### ORDER OF PYTHON OPERATIONS #####
# 1: local
# 2: parent local
# 3: global
# 4: built-in Python functions