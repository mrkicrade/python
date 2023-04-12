date = input("Enter today's date: ")
mood = input("How do you rate your mood today from1 to 10? ")
thoughts = input("Jet's your thoughts flow:\n")

with open(f"../journal/{date}.txt", "w") as file:
    file.write(mood + '\n')
    file.write(thoughts)
