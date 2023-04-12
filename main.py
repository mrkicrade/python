import functions

while True:
    user_action = input('Type add, show, edit, complete or exit> ')
    user_action = user_action.strip()

    # if 'add' in user_action or 'new' in user_action:
    if user_action.startswith('add'):
        todo = user_action[4:]

        # file = open('files/todos.txt', 'r')
        # todos = file.readlines()
        # file.close()

        # with open('files/todos.txt', 'r') as file:
        #     todos = file.readlines()

        # todos = get_todos('files/todos.txt')
        todos = functions.get_todos()

        todos.append(todo + '\n')

        # file = open('files/todos.txt', 'w')
        # file.writelines(todos)
        # file.close()

        # with open('files/todos.txt', 'w') as file:
        #     file.writelines(todos)

        functions.write_todos(todos, 'files/todos.txt')

    # elif 'show' in user_action:
    elif user_action.startswith('show'):
        todos = functions.get_todos()

        # new_todos = [item.strip('\n') for item in todos]

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1} - {item}"
            print(row)

    # elif 'edit' in user_action:
    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = functions.get_todos()

            new_todo = input('Enter a new Todo: ')
            todos[number] = new_todo + '\n'

            funtions.write_todos(todos, 'files/todos.txt')
        except ValueError:
            print('Your command is not valid!!!')
            continue

    # elif 'complete' in user_action:
    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])

            todos = functions.get_todos()

            removed_todo = todos[number - 1].strip('\n')

            todos.pop(number - 1)

            functions.write_todos(todos, 'files/todos.txt')

            message = f"Todo {removed_todo} was remowed from the list."
            print(message)
        except IndexError:
            print('There is no item with that number')
            continue

    # elif 'exit' in user_action:
    elif user_action.startswith('exit'):
        break

    else:
        print("Command is not valid!!!")

print('Bye')