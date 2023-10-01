###Backend of the Web version of TO_DO LIST APP
##Importing...
from datetime import datetime as dt

##FILEPATH
FILEPATH = "todo_list.txt"


##Defining
# Reading TO-DO LIST
def read_todos(filepath=FILEPATH):
    try:
        with open(filepath, "r") as file:
            local_todo = file.readlines()
            return local_todo
        # Creating an empty TO-DO LIST
    except FileNotFoundError:
        print(f"The {filepath} file was not found.")
        return []


# Modifying TO-DO LIST
def modifying_todo(todo_arg, filepath=FILEPATH):
    with open(filepath, "w") as file:
        file.writelines(todo_arg)


# Time
def time():
    now = dt.now()
    a = now.strftime("%c")
    return a
