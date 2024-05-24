########## REGULAR EXPRESSIONS ##########
import re

string = 'Search inside of this text please'
# This will work
'''
print('Search' in string)
'''

# print(re.search('this', string))

# Single search
a = re.search('this', string)
print(a.span())
print(a.start())
print(a.end())
print(a.group())