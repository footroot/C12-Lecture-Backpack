from todo import ToDoList

MENU = """Please select an option below: 

1. Add Task
2. Remove Task
3. Complete Task
4. Display Tasks

0. Quit"""

todo_list = ToDoList()

while True:

    print(MENU)
    user_option = input(": ")

    if user_option == "1":
        task = input("Enter New Task: ")
        todo_list.add_task(task)
    elif user_option == "2":
        print("Select a task to remove: ")
        todo_list.display_tasks()
        index = input(": ")
        if index.isdigit():
            index = int(index)-1
            todo_list.remove_task(index)
        else:
            print("Please use the index next to the task!")
    