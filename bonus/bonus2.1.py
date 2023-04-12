my_password = 'Krusevac'

user_password = input('Please, enter your password?')
user_password_capitalize = user_password.capitalize()

# if, else
# if user_password == my_password:
#     print('Your password is correct.')
# else:
#     print('Your password is not correct.')

# while
while user_password_capitalize != my_password:
    user_password = input('Please, enter your password?')
    user_password_capitalize = user_password.capitalize()

print('Your password is correct.')




