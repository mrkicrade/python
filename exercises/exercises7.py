# Exercise 1
names = ["john smith", "jay santi", "eva kuki"]

names = [name.title() for name in names]

print(names)

# Exercise 2
usernames = ["john 1990", "alberta1970", "magnola2000"]

usernames_length = [len(username) for username in usernames]

print(usernames_length)

# Exercise 3
user_entries = ['10', '19.1', '20']

user_entries = [float(user_entrie) for user_entrie in user_entries]

print(user_entries)

# Exercise 4
user_entries2 = ['10', '19.1', '20']

user_entries2 = [float(user_entrie) for user_entrie in user_entries]

sum_user_entries = sum(user_entries2)

print(sum_user_entries)