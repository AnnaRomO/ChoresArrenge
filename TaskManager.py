class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        self.sort_tasks()

    def remove_task(self, task):
        self.tasks.remove(task)

    def update_status(self, task, status):
        task.status = status

    def sort_tasks(self):
        self.tasks.sort(key=lambda x: (x.urgency, x.due_date))

    def get_tasks(self):
        return self.tasks
