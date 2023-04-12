# Exercises 1
country = input('Enter your country: ')

match country:
    case 'USA':
        print('Hello')
    case 'India':
        print('Namaste')
    case 'Germany':
        print('Hallo')

# Exercise 2
ingredients = ["john smith", "sen plakay", "dora ngacely"]

for ingredient in ingredients:
    print(ingredient.title())

