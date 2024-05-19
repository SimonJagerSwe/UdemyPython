########## ERROR HANDLING ##########

# print(1 + 'Hello') This exception will cause program to crash

# Example 1
'''
while True:
    try:
        age = int(input('What\'s your age? '))
        print(age)

    except:
        print('Invalid age format')

    else:
        print('Thank you!')
        break
'''


# Example 2
def sum(num1, num2):
    try:
        return num1 + num2
    except TypeError as err:
        print(f'Please enter numbers {err}')

# print(sum('1', '2'))      WILL CONCATENATE 1 and 2 to 12
# print(sum('1', 2))        WILL THROW ERROR, CAN'T CONCATENATE INT & STR
print(sum('1', 2))
print(sum(1, 2))