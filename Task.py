class Task:
    def __init__(self, title, urgency, due_date):
        self.title = title
        self.urgency = urgency
        self.due_date = due_date
        self.status = "Not Started"

    def __repr__(self):
        return f"Task(title={self.title}, urgency={self.urgency}, due_date={self.due_date}, status={self.status})"
