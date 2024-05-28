from functions import get_todos,write_todos
import time

now=time.strftime("%B %d %Y %H:%M:%S")
print("It is",now)
while True:
    #  get user input and strip space chars from it
    user_action = input("type add ,show ,edit ,complete or exit:")
    user_action = user_action.strip()

    if user_action.startswith("add") :
        todo = user_action[4:]

        todos=get_todos()

        todos.append(todo +'\n')

        write_todos(filepath="../venv/todos.txt", todos_arg=todos)

    elif user_action.startswith("show"):

        todos = get_todos()

        new_todos=[item.strip('\n') for item in todos]

        for index,item in enumerate(todos):
            item = item.title()
            item=item.strip('\n')

            row=f"{index + 1}-{item}"
            print(row)

    elif user_action.startswith("edit"):
        try:
            number=int (user_action[5:])
            print(number)
            number=number - 1

            todos = get_todos()


            new_todo=input("enter new todo:")
            todos[number]=new_todo +'\n'


            write_todos(todos)

        except ValueError:
            print("your command is not valid.")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            todos = get_todos()

            index=number-1
            todo_to_remove=todos[index].strip('\n')
            todos.pop(index)

            write_todos(todos)

            message=f"Todo {todo_to_remove} was removed from the list"
            print(message)
        except IndexError:
            print("there is no item with that number")
            continue

    elif user_action.startswith("exit"):
        break
    else:
        print("command is not valid")

print("Bye")
