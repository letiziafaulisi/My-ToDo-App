""" Costanti del modulo """

FILEPATH = "todos.txt"

""" elenco delle funzioni del modulo """

def get_todos():
    """funzione per ricavare la lista a partire dal file"""
    with open(FILEPATH, "r") as file:
        todos_local = file.readlines()
    return todos_local

def write_todos(arg):
    """funzione per scrivere all'interno di un file"""
    with open(FILEPATH, "w") as file:
        file.writelines(arg)