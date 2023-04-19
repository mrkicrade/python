# Exercises 1
temperatures = [10, 12, 14]

temperatures = [str(i) + '\n' for i in temperatures]

file = open("file.txt", 'w')
file.writelines(temperatures)

# Exercises 2
numbers = [10.1, 12.3, 14.7]
numbers = [int(number) for number in numbers]
print(numbers)