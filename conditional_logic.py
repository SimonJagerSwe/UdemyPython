########## CONDITIONAL LOGIC ##########

# Buggy program
'''
is_old = False
is_licensed = True

if is_old:
    print('You are old enough to drive!')

elif is_licensed:
    print('You can drive now!')

else: 
    print('You\'re not old enough to drive!')

print('Check')
'''

# Functional program

is_old = True
is_licensed = False

if is_old and is_licensed:
    print('You can drive now!')    

else: 
    print('You\'re not cleared to drive')
