from todo import ToDoList
from logger import LoggerFactory, TimestampDecorator, SeverityLevelDecorator

MENU = """Please select an option below:

1. Add Task
2. Complete Task
3. Remove Task
4. View All Tasks

0. Quit"""

todo_list = ToDoList()

logger = LoggerFactory.get_logger("file")
logger = TimestampDecorator(logger)
logger = SeverityLevelDecorator(logger, "INFO")

while True:
    print(MENU)
    user_input = input(": ")

    if user_input == "1":
        task = input("Please enter the task to add:\n")
        todo_list.add_task(task)
        logger.log(f"Added new task '{task}'")

    elif user_input == "2":
        print("Please select a task below:")
        todo_list.show_tasks()
        task_index = input(": ")
        if task_index.isdigit():
            task_index = int(task_index)
            todo_list.complete_task(task_index-1)
            task_name = todo_list.get_task_name(task_index-1)
            logger.log(f"Task '{task_name}' marked as complete.")
        else:
            print("Invalid option!")

    elif user_input == "3":
        print("Please select a task below:")
        todo_list.show_tasks()
        task_index = input(": ")
        if task_index.isdigit():
            task_index = int(task_index)
            task_name = todo_list.get_task_name(task_index-1)
            todo_list.remove_task(task_index-1)
            logger.log(f"Task '{task_name}' removed.")
        else:
            print("Invalid option!")

    elif user_input == "4":
        todo_list.show_tasks()
        input("Press enter to continue...")

    elif user_input == "0":
        print("Goodbye!")
        break

