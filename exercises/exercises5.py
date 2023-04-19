# Exercise 1

filenames = ['document', 'report', 'presentation']

for index, filename in enumerate(filenames):
    print(f'{index}-{filename.capitalize()}.txt')

# Exercise 2

ips = ['100.122.133.105', '100.122.133.111']

input_user = int(input('Enter the index of the IP you want (0 or 1): '))

print(f"Tou choose {ips[input_user]}")
