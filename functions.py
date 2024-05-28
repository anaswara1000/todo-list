def get_todos(filepath="todos.txt"):
    """read a textfile and return the list of todo items"""
    with open(filepath, 'r') as file:
        todos_local = file.readlines()
    return todos_local

def write_todos(todos_arg,filepath="todos.txt"):
    """write the todo items list in the textfile"""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


if __name__=="__main__":
    print("hello")
    print(get_todos())


