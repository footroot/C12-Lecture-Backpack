# Create a todo list that stores tasks and their completion
# The list should be able to add, remove, mark as complete and view tasks.

class ToDoList:

    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task" : task, "complete" : False})
        print(f"Task '{task}' added to list!")

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            removed_task = self.tasks.pop(index)
            print(f"Task '{removed_task['task']}' has been removed!")
        else:
            print("Invalid task number!")

    def mark_complete(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]['complete'] = True
            print(f"Task '{self.tasks[index]['task']}' has been marked complete!")
        else:
            print("Invalid task number!")

    def display_tasks(self):
        if not self.tasks:
            print("Task list is empty please add a task!")
        else:
            print("To-Do List:")
            for i, task in enumerate(self.tasks, 1):
                status = "O" if task['complete'] else 'X'
                print(f"{i}. {task['task']: <25} [{status}]")


def main():
    todo_list = ToDoList()
    print(todo_list.tasks)

    todo_list.add_task("Take out the trash!")
    print(todo_list.tasks)

    todo_list.mark_complete(0)
    print(todo_list.tasks)

    todo_list.add_task("Clean my room!")
    todo_list.remove_task(0)
    todo_list.remove_task(0)
    print(todo_list.tasks)

    todo_list = ToDoList()
    todo_list.add_task("Take out the trash!")
    todo_list.add_task("Clean my room!")
    todo_list.add_task("Do the dishes!")
    todo_list.mark_complete(2)
    todo_list.display_tasks()

if __name__ == "__main__":
    main()