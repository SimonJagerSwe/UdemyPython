########## LIST METHODS ##########

basket = [1,2, 3, 4, 5]
basket_2 = ['a', 'b', 'c', 'd', 'e']
basket_3 = [1, 2, 4, 3, 5]
basket_4 = ['x', 'a', 'b', 'c', 'd', 'e', 'd']

# print(len(basket))


##### ADDING ITEMS TO LISTS #####
# APPEND
# basket.append(100)
# new_list = basket
# print(new_list)

# INSERT
# basket.insert(4, 100)
# new_list = basket
# print(new_list)

# EXTEND
# new_list = basket.extend([100, 101])
# print(basket)
# print(new_list)


##### REMOVING ITEMS FROM LISTS #####
# POP
# basket.pop()
# basket.pop(0)
 #print(basket)

# REMOVE
# basket.remove(4)
# print(basket)

# CLEAR
# basket.clear()
# print(basket)


##### MORE METHODS #####
# print(basket.index(2))
# print(basket_2.index('d'))

# print('x' in basket_2)
# print('i' in 'Hi, my name is Simon')

# print(basket_2.count('d'))

# basket_3.sort()
# print(basket_3)
# basket_4.sort()
# print(basket_4)
# basket_3.reverse()
# print(basket_3)
# basket_4.reverse()
# print(basket_4)

# print(list(range(100)))
# print(list(range(1,100)))
# print(list(range(1,101)))

# sentence = ' '
# new_sentence = sentence.join(['Hi', 'my', 'name', 'is', 'Simon'])
# print(new_sentence)


##### EXCERCISE #####
#fix this code so that it prints a sorted list of all of our friends (alphabetical). Scroll to see answer
# friends = ['Simon', 'Patty', 'Joy', 'Carrie', 'Amira', 'Chu']

# new_friend = ['Stanley']

# friends_list = friends
# friends_list.extend(new_friend)
# friends_list.sort()
# print(friends_list)


##### LIST UNPACKING #####
a, b, c, *other = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a)
print(b)
print(c)
print(other)