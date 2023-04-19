# Exercise 1
def get_max():
    grades = [9.6, 9.2, 9.7]
    maximum = max(grades)
    return maximum


print(get_max())

# Exercise 2
def get_max2():
    grades2 = [9.6, 9.2, 9.7]
    maximum = max(grades2)
    minimum = min(grades2)
    message = f"Max: {maximum}, Min: {minimum}"
    return message


print(get_max2())