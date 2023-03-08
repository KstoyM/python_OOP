from to_do_list.task import Task


class Section:

    def __init__(self, name: str):
        self.name = name
        self.tasks = []

    def add_task(self, new_task: Task):
        if new_task not in self.tasks:
            self.tasks.append(new_task)
            return f"Task {Task.details(new_task)} is added to the section"
        else:
            return f"Task is already in the section {self.name}"

    def complete_task(self, task_name: str):
        try:
            task = next(filter(lambda t: task_name == t.name, self.tasks))
            task.completed = True
            return f"Completed task {task_name}"
        except StopIteration:
            return f"Could not find task with the name {task_name}"

    def clean_section(self):
        current_len = len(self.tasks)
        for task in self.tasks:
            if task.completed:
                self.tasks.remove(task)
        return f"Cleared {current_len - len(self.tasks)} tasks."

    def view_section(self):
        result = "\n".join(t.details() for t in self.tasks)
        return f"Section {self.name}: \n{result}"


