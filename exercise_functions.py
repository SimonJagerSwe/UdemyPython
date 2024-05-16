########## EXERCISE: FUNCTIONS ##########
'''
##### MY SOLUTION #####
li = [10, 2, 3, 4, 8, 11]
even_list = []

for i in li:
    if i % 2 == 0:
        even_list.append(i)


def highest_even():
    for i in li:
        if i % 2 == 0:
            even_list.append(i)


# print(li)
even_list.sort()
print(even_list[-1])
# print(highest_even[10, 2, 3, 4, 8, 11])
'''

##### UDEMY SOLUTION #####
def highest_even(li):
    evens = []
    for item in li:
        if item % 2 == 0:    
            evens.append(item)
    return max(evens)

print(highest_even([10,2,3,4,8,11]))