########## 100 PYTHON EXERCISES ##########

# TASK 1: Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included).The numbers obtained should be printed in a comma-separated sequence on a single line.
'''
list_7 = []
list_5_and_7 = []

for i in range(2000, 3201):
    if i % 7 == 0:
        list_7.append(i)

for i in list_7:
    if i % 5 != 0:
        list_5_and_7.append(i)

print(list_5_and_7)

'''


# TASK 2: Write a program which can compute the factorial of a given numbers.The results should be printed in a comma-separated sequence on a single line.Suppose the following input is supplied to the program: 8 Then, the output should be:40320

def factorial(num):
    a = 1
    b = 2
    c = a * b
    result = []
    for i in range(num):   
        result.append(c)
    return result

print(factorial(8))
