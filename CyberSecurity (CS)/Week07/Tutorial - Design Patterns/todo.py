class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        """Adds a task to the to-do list."""
        self.tasks.append(Task(task))
        print(f'Task "{task}" added.')

    def complete_task(self, task_number):
        """Marks a task as completed by its task number."""
        if 0 <= task_number < len(self.tasks):
            self.tasks[task_number].mark_complete()
            print(f'Task "{self.tasks[task_number].get_task()}" marked as completed.')
        else:
            print("Invalid task number.")

    def remove_task(self, task_number):
        """Deletes a task by its task number."""
        if 0 <= task_number < len(self.tasks):
            removed_task = self.tasks.pop(task_number)
            print(f'Task "{removed_task.get_task()}" deleted.')
        else:
            print("Invalid task number.")

    def show_tasks(self):
        """Displays all tasks with their status."""
        if not self.tasks:
            print("No tasks in the to-do list.")
        else:
            print("To-Do List:")
            for i, task in enumerate(self.tasks, 1):
                status = "✓" if task.get_complete_status() else "✗"
                print(f'{i}. {task.get_task(): <25} [{status}]')

    def get_task_name(self, task_number):
        """Return task name of given task index."""
        if 0 <= task_number < len(self.tasks):
            return self.tasks[task_number].get_task()
        print("Invalid task number.")
        return None


class Task:

    def __init__(self, task) -> None:
        self._task = task
        self._is_complete = False

    def get_complete_status(self):
        return self._is_complete

    def mark_complete(self):
        self._is_complete = True

    def get_task(self):
        return self._task
