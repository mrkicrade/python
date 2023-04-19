# Exercise 1
# try:
#     total = float(input("Enter total value: "))
#     value = float(input("Enter value: "))
#
#     percentage = value / total * 100
#     print(f"That is {percentage}%")
# except ValueError:
#     print("You need to enter a number. Run the program again.")

# Exercise 2
# try:
#     total = float(input("Enter total value: "))
#     value = float(input("Enter value: "))
#
#     if total == 0:
#         print('YOur total value cannot bi zero.')
#     else:
#         percentage = value / total * 100
#         print(f"That is {percentage}%")
# except ValueError:
#     print("You need to enter a number. Run the program again.")

try:
    total_value = float(input("Enter total value: "))
    value = float(input("Enter value: "))

    percentage = value / total_value * 100
    print(f"That is {percentage}%")
except ValueError:
    print("You need to enter a number. Run the program again.")
except ZeroDivisionError:
    print("Your total value cannot be zero.")
