########## 100 PYTHON EXERCISES ##########

# Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included).The numbers obtained should be printed in a comma-separated sequence on a single line.
list_7 = []
list_5_and_7 = []

for i in range(2000, 3201):
    if i % 7 == 0:
        list_7.append(i)
        
for i in list_7:
    if i % 5 != 0:
        list_5_and_7.append(i)

print(list_5_and_7)