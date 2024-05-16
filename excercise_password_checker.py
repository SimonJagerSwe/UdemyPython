########## EXCERCSIE: PASSWORD CHECKER ##########

user_name = input('Input your user name: ')
password = input('Input password: ')
password_length = len(password)
secret_password = '*' * password_length

print(f'{user_name}, your password, {secret_password}, is {password_length} letters long')