########## FIND THE DUPLICATES ##########

some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
duplicate_list = []

for char in some_list:
    if some_list.count(char) > 1:
        if char not in duplicate_list:            
            duplicate_list.append(char)

print(duplicate_list)