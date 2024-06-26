########## SETS ##########
# Does not accept duplicates
# Not indexable

# my_set = {1, 2, 3, 4, 5, 5}
# my_set.add(100)
# my_set.add(2)
# print(my_set)


##### EXCERCISE #####
 #my_list = [1, 2, 3, 4, 5, 5]
# my_set = my_list
# print(my_set)

# print(set(my_list))


##### SET FUNCTIONS #####
my_set = {1, 2, 3, 4, 5}
your_set = {4, 5, 6, 7, 8, 9, 10}
extra_set = {4, 5}

# .difference()
# print(my_set.difference(your_set))

# .discard()
# print(my_set.discard(5))
# print(my_set)

# .difference_update()
# print(my_set.difference_update(your_set))
# print(my_set)

# .intersection()
# print(my_set.intersection(your_set))

# .isdisjoint()
# print(my_set.isdisjoint(your_set))

# .issubset()
# print(my_set.issubset(your_set))
# print(extra_set.issubset(your_set))

# .issuperset()
# print(my_set.issuperset(your_set))
# print(extra_set.issuperset(my_set))

# .union()
# print(my_set.union(your_set))
# OR
# print(my_set | your_set)


##### EXCERCISE #####
#Scroll to bottom to see solution
# You are working for the school Principal. We have a database of school students:
school = {'Bobby','Tammy','Jammy','Sally','Danny'}

#during class, the teachers take attendance and compile it into a list. 
attendance_list = ['Jammy', 'Bobby', 'Danny', 'Sally']

#using what you learned about sets, create a piece of code that the school principal can use to immediately find out who missed class so they can call the parents. (Imagine if the list had 1000s of students. The principal can use the lists generated by the teachers + the school database to use python and make his/her job easier): Find the students that miss class!

print(school.difference(attendance_list))