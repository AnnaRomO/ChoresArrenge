import json
from Task import Task
from datetime import datetime

class TaskManager:
    def __init__(self):
        self.tasks = []
        self.load_tasks()

    def add_task(self, task):
        self.tasks.append(task)
        self.sort_tasks()
        self.save_tasks()

    def remove_task(self, task):
        self.tasks.remove(task)
        self.save_tasks()

    def update_status(self, task, status):
        task.status = status
        self.save_tasks()

    def sort_tasks(self):
        self.tasks.sort(key=lambda x: (x.urgency, x.due_date))

    def get_tasks(self):
        return self.tasks

    def save_tasks(self):
        with open('tasks.json', 'w') as f:
            json_tasks = [task.__dict__ for task in self.tasks]
            json.dump(json_tasks, f, default=str)

    def load_tasks(self):
        try:
            with open('tasks.json', 'r') as f:
                json_tasks = json.load(f)
                self.tasks = [Task(**task) for task in json_tasks]
        except FileNotFoundError:
            self.tasks = []
