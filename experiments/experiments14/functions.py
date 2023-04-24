FILEPATH = '../files/todos.txt'


def get_todos(filepath=FILEPATH):
    """ Read a text file and return the list of
    to-do items.
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
        return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """ Write to-do items list in the text file. """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

# print(__name__)

"""
Kada se pokrene Python program, sam interpreter postavlja neke variajble i dodeljuje im određene vrednosti pre samog čitanja naših fajlova.
Jedna od tih varijabli je __name__ i njoj se dodeljuje vrednost __main__. Ova varijabla imaće ovu vrednost samo ako inpetreter pokrene baš taj modul.
Ako je ovaj modul importovan u drugi modul, vrednost ove varijable će biti naziv samog modula.
"""

if __name__ == '__main__':
    print('Hello')

print('hello from functions')