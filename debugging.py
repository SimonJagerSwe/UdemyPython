########## JOKES ##########

# Linting
# num + 4       VSC will tell us that num is not defined, this is linting

# Always use an IDE or editor, they will have built in linting tools, autoformatting

# Always read your errors
# 4 + 'random string           Will throw a syntax error

##### PDB/PYTHON DEBUGGER #####
import pdb
def add(num1, num2):
    pdb.set_trace()
    return num1, num2

add(4, 'asdasd')