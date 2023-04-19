# Exercise 1
file = open("exercises6/essay.txt", 'r')
content = file.read()
print(content.title())

# Exercise 2
file = open("exercises6/essay.txt", 'r')
content = file.read()
print(len(content))

# Exercise 3
member = input("Add a new member: ")

file = open("members.txt", 'r')
existing_members = file.readlines()
file.close()

existing_members.append(member + "\n")

file = open("members.txt", 'w')
existing_members = file.writelines(existing_members)
file.close()

# Exercise 4
filenames = ['doc.txt', 'report.txt', 'presentation.txt']

for filename in filenames:
    file = open(filename, 'w')
    file.write("Hello")
    file.close()

# Exercise 5
filenames = ['a.txt', 'b.txt', 'c.txt']

for filename in filenames:
    file = open(filename, 'r')
    content = file.read()
    print(content)
