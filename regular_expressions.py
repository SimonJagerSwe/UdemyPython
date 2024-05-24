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


# Search pattern
pattern = re.compile('inside')
b = pattern.search(string)
print(b.group())
c = pattern.findall(string)
print(c)
d = pattern.fullmatch(string)
print(d)
e = pattern.match(string)
print(e)