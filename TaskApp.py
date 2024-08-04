import tkinter as tk
from tkinter import messagebox
from tkcalendar import DateEntry
from datetime import datetime
from Task import Task
from TaskManager import TaskManager

class TaskApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Task Manager")
        self.task_manager = TaskManager()

        self.title_label = tk.Label(root, text="Task Title")
        self.title_label.grid(row=0, column=0)
        self.title_entry = tk.Entry(root)
        self.title_entry.grid(row=0, column=1)

        self.urgency_label = tk.Label(root, text="Urgency")
        self.urgency_label.grid(row=1, column=0)
        self.urgency_var = tk.StringVar()
        self.urgency_menu = tk.OptionMenu(root, self.urgency_var, "1", "2", "3", "4", "5")
        self.urgency_var.set("1")
        self.urgency_menu.grid(row=1, column=1)

        self.due_date_label = tk.Label(root, text="Due Date")
        self.due_date_label.grid(row=2, column=0)
        self.due_date_entry = DateEntry(root, date_pattern='dd-MM-yyyy')
        self.due_date_entry.grid(row=2, column=1)

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.grid(row=3, column=0, columnspan=2)

        self.task_listbox = tk.Listbox(root, width=50)
        self.task_listbox.grid(row=4, column=0, columnspan=2)

        self.status_label = tk.Label(root, text="Update Status")
        self.status_label.grid(row=5, column=0)
        self.status_var = tk.StringVar()
        self.status_menu = tk.OptionMenu(root, self.status_var, "Not Started", "Ongoing", "Done")
        self.status_menu.grid(row=5, column=1)

        self.update_button = tk.Button(root, text="Update Status", command=self.update_status)
        self.update_button.grid(row=6, column=0, columnspan=2)

        self.refresh_task_list()

    def add_task(self):
        title = self.title_entry.get()
        urgency = int(self.urgency_var.get())
        due_date = datetime.strptime(self.due_date_entry.get(), "%d-%m-%Y")

        new_task = Task(title, urgency, due_date)
        self.task_manager.add_task(new_task)

        self.refresh_task_list()

    def update_status(self):
        selected_index = self.task_listbox.curselection()
        if not selected_index:
            messagebox.showwarning("Warning", "No task selected")
            return

        status = self.status_var.get()
        selected_task = self.task_manager.get_tasks()[selected_index[0]]
        self.task_manager.update_status(selected_task, status)

        self.refresh_task_list()

    def refresh_task_list(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.task_manager.get_tasks():
            self.task_listbox.insert(tk.END, f"{task.title} - {task.urgency} - {task.due_date.date()} - {task.status}")
            self.color_task(self.task_listbox.size() - 1, task.urgency)

    def color_task(self, index, urgency):
        colors = {
            "1": "green",
            "2": "yellow",
            "3": "orange",
            "4": "red",
            "5": "purple"
        }
        self.task_listbox.itemconfig(index, {'bg': colors.get(str(urgency), 'white')})

