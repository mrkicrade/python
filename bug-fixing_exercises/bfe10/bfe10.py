# Exercise 1
waiting_list = ["john", "marry"]
name = input("Enter name: ")

try:
    number = waiting_list.index(name)
    print(f"{name}'s turn is {number + 1}")
except ValueError:
    print(f"{name} is not in the list.")